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

# ==============================
# Functions
# ==============================
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


def WriteData( x, y, file_name ):
    with open(file_name, 'a') as f:
        for i in range(len(y)):
            y_str = '+%1d '%y[i] if y[i] > 0 else '%1d '%y[i]
            f.write( y_str )
            for j in range(len(x[0])):
                f.write( "%d:%.6f "%(j+1, x[i, j]) )
            f.write("\n")
    return


# ==============================
# Main
# ==============================
if __name__ == '__main__':
    Q_order    = 3
    trans_type = Q_FULL
    trans_idx  = None
    
    # Set up problem
    test_file  = "./hw4_test.dat"
    train_file = "./hw4_train.dat"

    x_0 = 1.0
    scale_type = SCALE_NONE
    scale_size = 1.0
    
    
    # Load data
    x_train, y_train = LoadData( train_file, x_0, scale_type, scale_size )
    x_test,  y_test  = LoadData( test_file,  x_0, scale_type, scale_size )

    # Transform data
    x_train_trans = TransformData( x_train, Q_order, trans_type, trans_idx )
    x_test_trans  = TransformData( x_test,  Q_order, trans_type, trans_idx )

    test_trans_file  = './test_trans.txt'
    train_trans_file = './train_trans.txt'
    train_trans_120_file = './train_small_trans.txt'
    train_trans_80_file  = './train_valid_trans.txt'

    WriteData( x_test_trans,  y_test,  test_trans_file  )
    WriteData( x_train_trans, y_train, train_trans_file )
    WriteData( x_train_trans[0:120], y_train[0:120], train_trans_120_file )
    WriteData( x_train_trans[120:], y_train[120:], train_trans_80_file )
    for i in range(5):
        WriteData( np.delete(x_train_trans, [40*i + j for j in range(40)], 0), np.delete(y_train, [40*i+j for j in range(40)], 0), './train_train_cv_%d.txt'%i )
        WriteData( x_train_trans[40*i:40*(i+1)], y_train[40*i:40*(i+1)], './train_valid_cv_%d.txt'%i )

        
