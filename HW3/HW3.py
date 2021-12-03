# ==============================
# Import modules
# ==============================
import numpy as np
import math


# ==============================
# Define global constants
# ==============================
PROBLEM_NUM    = 0
EXP_TIME       = 1

Q_FULL         = 0
Q_HOMOGENEOUS  = 1
Q_LOWER        = 2
Q_LOWER_RANDOM = 3

SCALE_NONE     = 0
SCALE_CONST    = 1
SCALE_NORM     = 2

ERROR_BIN      = 0         # binary error 0/1
ERROR_SQR      = 1         # square error
ERROR_CE       = 2         # 


# ==============================
# Functions
# ==============================
"""
Input  : 
Output : 
Note   :
"""
def LoadData( data_file, x_0, scale_type, scale_size ):
    data = np.loadtxt( data_file )
    N    = data.shape[0]
    dim  = data.shape[1]
    x    = np.zeros( (N, dim) )
    y    = np.zeros( (N, 1) )

    x[:, 0]  = x_0
    x[:, 1:] = data[:, 0:-1]
    y        = data[:, -1].reshape( N )

    if scale_type == SCALE_CONST:
        x *= scale_size
    elif scale_type == SCALE_NORM:
        norm = np.linalg.norm( x, axis = 1 )
        for i in range( N ):
            x[i, :] = x[i, :] / norm[i]
    
    return x, y


def UpdatePower( power, start, tot ):
    N = len( power )
    if start == N:
        return power, start
    
    if power[-1] == tot-1:
        power[-1] = 0
        power[start] = 0
        power[start+1] = tot
        start += 1
        return power, start

    for i in range(N-1, 0-1, -1):
        if power[i] == 0:   pass
        elif i == N-1:      pass
        else:
            power[i  ] -= 1
            power[i+1] += 1
            break
    return power, start

def TransformData( x, Q, Q_mode, idx ):
    N   = x.shape[0]
    dim = x.shape[1] - 1
    
    if Q_mode == Q_FULL:
        dim_new = 1
        for i in range( Q ):
            #C^{dim+i}_dim
            dim_new += math.comb(dim-1+i+1, dim-1)
        x_new = np.ones( (N, dim_new) )

        counter = 1
        for i in range( Q ):
            power = np.zeros( dim )
            power[0] = i+1
            start = 0
            for j in range( math.comb(dim+i, dim-1) ):
                for k in range( dim ):
                    if power[k] == 0: continue
                    x_new[:, counter] *= x[:, k+1]**power[k]
                power, start = UpdatePower( power, start, i+1 )
                counter += 1

    elif Q_mode == Q_HOMOGENEOUS:
        dim_new = int( Q*dim + 1 )
        x_new = np.ones( (N, dim_new) )

        for i in range( Q ):
            for j in range( dim ):
                x_new[ :, i*dim + (j+1) ] = x[ :, (j+1) ]**(i+1)

    elif Q_mode == Q_LOWER:
        dim_new = Q + 1
        x_new = np.ones( (N, dim_new) )

        x_new[ :, 1: ] = x[ :, 1:dim_new ]

    elif Q_mode == Q_LOWER_RANDOM:
        dim_new = Q + 1
        x_new = np.ones( (N, dim_new) )
        
        for i in range( Q ):
            x_new[ :, i+1 ] = x[ :, idx[i]+1 ]

    else:
        print("Wrong mode of transforming data.")
        exit()

    return x_new


def LinearRegression( x, y ):
    # 0. Setup
    dim = x.shape[1]
    w_lin = np.zeros( (dim, 1) )
    
    # 1. Calculate X^{\dagger}
    x_dagger = np.linalg.pinv( x )
    
    # 2. w_{LIN} = X^{\dagger} Y
    w_lin = x_dagger.dot( y )
    
    return w_lin


def Error( x, y, w, mode ):
    if mode == ERROR_BIN:
        N = x.shape[0]
        error = ( y * x.dot(w) < 0 ).sum()
        error /= N
    elif mode == ERROR_SQR:
        error = np.mean( np.square( x.dot(w) - y ) )
    elif mode == ERROR_CE:
        print("Not supported mode yet.")
        error = 0.0
    else:
        print("Wrong error calculate mode.")
        exit()
    return error 


# ==============================
# Main
# ==============================
if __name__ == '__main__':
    def Setup_Problem( num ):
        global EXP_TIME
        
        if num == 12:
            Q_order    = 2
            trans_type = Q_HOMOGENEOUS
            error_type = ERROR_BIN

        elif num == 13:
            Q_order = 8
            trans_type = Q_HOMOGENEOUS
            error_type = ERROR_BIN

        elif num == 14:
            Q_order = 2
            trans_type = Q_FULL
            error_type = ERROR_BIN

        elif num == 15:
            Q_order    = 0
            EXP_TIME   = 10
            trans_type = Q_LOWER
            error_type = ERROR_BIN

        elif num == 16:
            Q_order    = 5
            EXP_TIME   = 200
            trans_type = Q_LOWER_RANDOM
            error_type = ERROR_BIN

        else:
            print("Wrong PROBLEM_NUM. Please set it to be one of [12/13/14/15/16].")
            exit()
        
        return Q_order, trans_type, error_type
    
    PROBLEM_NUM = 16
    
    # Set up problem
    test_file  = "./hw3_test.dat.txt"
    train_file = "./hw3_train.dat.txt"

    x_0 = 1.0
    scale_type = SCALE_NONE
    scale_size = 1.0
    
    Q_order, trans_type, error_type = Setup_Problem( PROBLEM_NUM )
    
    # Load data
    x_train, y_train = LoadData( train_file, x_0, scale_type, scale_size )
    x_test,  y_test  = LoadData( test_file,  x_0, scale_type, scale_size )

    err = 0.0
    trans_idx = None
    err_15 = []
    for i in range( EXP_TIME ):
    #   If random choose
        if trans_type == Q_LOWER_RANDOM:
            trans_idx = np.random.choice( 10, size = (Q_order), replace=False )

        if PROBLEM_NUM == 15: Q_order = i+1
        
    #   Transform data
        x_train_trans = TransformData( x_train, Q_order, trans_type, trans_idx )
        x_test_trans  = TransformData( x_test,  Q_order, trans_type, trans_idx )
        
    #   Linear Regression
        w_lin = LinearRegression( x_train_trans, y_train )

    #   Calculate Error
        E_in  = Error( x_train_trans, y_train, w_lin, error_type )
        E_out = Error( x_test_trans,  y_test,  w_lin, error_type )
        err  += np.abs( E_in - E_out )

        if PROBLEM_NUM == 15: err_15.append( np.abs(E_in - E_out) )

    err /= EXP_TIME

    if PROBLEM_NUM == 15:
        min_value = min(err_15)
        min_index = err_15.index(min_value)
        print( min_value, min_index+1 )
    else:
        print( err )
        


