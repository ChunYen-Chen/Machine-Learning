# ==============================
# Import modules
# ==============================
import numpy as np


# ==============================
# Define global constants
# ==============================
PROBLEM_NUM = 0         # [13/14/15/16]
EXP_TIME    = 100       # Experience times

N_TRAIN     = 200       # Training set size
N_UNIVERSE  = 5000      # Universe set size
N_NOISE     = 20        # Noise set size

ERROR_BIN   = 0         # binary error 0/1
ERROR_SQR   = 1         # square error
ERROR_CE    = 2         # 


# ==============================
# Functions
# ==============================
"""
Input  : N       : number of samples.
         var1    : the variance of the normal distribution of x. (-y case)
         mean1   : the mean of the normal distribution of x. (-y case)
         var2    : the variance of the normal distribution of x. (+y case)
         mean2   : the mean of the normal distribution of x. (+y case)
         N_noise : number of noise samples.
         var3    : the variance of the normal distribution of x. (+y noise case)
         mean3   : the mean of the normal distribution of x. (+y noise case)
Output : 
Note   : 1. The dimension of the variance and mean should be the same.
"""
def GenerateSamples( N, var1, mean1, var2, mean2, seed, N_noise = 0, var3 = None, mean3 = None ):
    # 0. Check (TODO)
    # N_noise >= 0
    # dimension should be same
    
    # 1. Setup
    dim = 3
    y = np.zeros( (N+N_noise, 1) )
    x = np.ones( (N+N_noise, dim) )
    
    # 2. Get the number of y+ and y-
    N_y_minus = np.random.binomial( N, 0.5 )
    N_y_plus  = N - N_y_minus
    
    # 3. Assign the y and x 
    y[        0:N_y_minus] = -1.0
    y[N_y_minus:N        ] =  1.0
    
    x[        0:N_y_minus, 1:3] = np.random.multivariate_normal( mean1, var1, N_y_minus )
    x[N_y_minus:N        , 1:3] = np.random.multivariate_normal( mean2, var2, N_y_plus )
    
    # 4. noise case. Same method as 2. and 3.
    if N_noise != 0:
        y[N:N+N_noise] =  1.0
        x[N:N+N_noise, 1:3] = np.random.multivariate_normal( mean3, var3, N_noise )

    return x, y


def LogisticFunc( x ):
    return 1. / ( 1. + np.exp(-x) )


def LinearRegression( x, y ):
    # 0. Setup
    dim = x.shape[1]
    w_lin = np.zeros( (dim, 1) )
    
    # 1. Calculate X^{\dagger}
    #x_dagger = np.linalg.pinv( x )
    x_dagger = x.T
    x_dagger = x_dagger.dot(x)
    x_dagger = np.linalg.inv(x_dagger)
    x_dagger = x_dagger.dot(x.T)
    
    # 2. w_{LIN} = X^{\dagger} Y
    w_lin = x_dagger.dot( y )
    
    return w_lin


def LogisticRegression( x, y, rate, iter_num ):
    # 0. Setup
    N   = x.shape[0]
    dim = x.shape[1]
    w_log = np.zeros( (dim, 1) )

    for i in range( iter_num ):
        # 1. Calculate \grad E_in
        theta = LogisticFunc( ( -y*x ).dot(w_log) )
        gradE = ( -y*x ).T.dot(theta) / N

        # 2. Update
        w_log -= rate * gradE
    
    return w_log


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
    """
    Input  : num        : Problem number.
    Output : mean_plus  : the mean of the normal distribution of x in the case of y+.
             var_plus   : the variance of the normal distribution of x in the case of y+.
             mean_minus : the mean of the normal distribution of x in the case of y-.
             var_minus  : the variance of the normal distribution of x in the case of y-.
             mean_noise : the mean of the normal distribution of x in the case of y+ noise.
             var_noise  : the variance of the normal distribution of x in the case of y+ noise.
             rate       : the learning rate of the gradient descent method.
             iter_num   : the number of iteration of the gradient desent method.
    Note   : 
    """
    def Setup_Problem( num ):
        global N_NOISE
        mean_plus   = np.array( [2., 3.] )
        mean_minus  = np.array( [0., 4.] )
        mean_noise  = np.array( [6., 0.] )
        var_plus    = np.array( [[0.6, 0.0], [0.0, 0.6]] )
        var_minus   = np.array( [[0.4, 0.0], [0.0, 0.4]] )
        var_noise   = np.array( [[0.3, 0.0], [0.0, 0.1]] )
        if   num == 13:
            N_NOISE = 0
            rate = 0.1
            iter_num = 500

        elif num == 14:
            N_NOISE = 0
            rate = 0.1
            iter_num = 500
            
        elif num == 15:
            N_NOISE = 0
            rate = 0.1
            iter_num = 500

        elif num == 16:
            N_NOISE = 20
            dim = 3
            rate = 0.1
            iter_num = 500

        else:
            print("Wrong PROBLEM_NUM. Please set it to be one of [13/14/15/16].")
            exit()

        return mean_plus, var_plus, mean_minus, var_minus, mean_noise, var_noise, rate, iter_num


    PROBLEM_NUM = 16
    seed = None
    mean_plus, var_plus, mean_minus, var_minus, \
               mean_noise, var_noise, rate, iter_num = Setup_Problem( PROBLEM_NUM )

    err_sqr   = 0.0
    err_diff  = 0.0
    err_a_out = 0.0
    err_b_out = 0.0
    
    for i in range( EXP_TIME ):
        # Generate samples
        x_in,  y_in  = GenerateSamples( N_TRAIN,    var_minus, mean_minus, var_plus, mean_plus, seed, \
                                        N_NOISE,    var_noise, mean_noise )
        x_out, y_out = GenerateSamples( N_UNIVERSE, var_minus, mean_minus, var_plus, mean_plus, seed )
        
        # Linear Regression
        w_lin = LinearRegression( x_in, y_in )
        
        # Logistic Regression
        w_log = LogisticRegression( x_in, y_in, rate, iter_num )
        
        # Square Error
        err_sqr   += Error( x_in, y_in, w_lin, ERROR_SQR )
        
        # 0/1 Error
        err_in     = Error( x_in,  y_in,  w_lin, ERROR_BIN )
        err_out    = Error( x_out, y_out, w_lin, ERROR_BIN )
        err_diff  += np.abs( err_in - err_out )
        err_a_out += Error( x_out, y_out, w_lin, ERROR_BIN )
        err_b_out += Error( x_out, y_out, w_log, ERROR_BIN )
        
    err_sqr   /= EXP_TIME
    err_diff  /= EXP_TIME
    err_a_out /= EXP_TIME
    err_b_out /= EXP_TIME
    
    print("Problem: %02d"%PROBLEM_NUM)
    if PROBLEM_NUM == 13:
        print("Linear   => Square Error  :", err_sqr)
    elif PROBLEM_NUM == 14:
        print("Linear   => |E_in - E_out|:", err_diff)
    elif PROBLEM_NUM == 15:
        print("Linear   => E_out         :", err_a_out)
        print("Logistic => E_out         :", err_b_out)
    elif PROBLEM_NUM == 16:
        print("Linear   => E_out         :", err_a_out)
        print("Logistic => E_out         :", err_b_out)
        
