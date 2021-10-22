# ==============================
# Import modules
# ==============================
import numpy as np



# ==============================
# Define global const
# ==============================
SCALE_NONE  = 0
SCALE_CONST = 1
SCALE_NORM  = 2



# ==============================
# Functions
# ==============================
"""
Input  : 
Output : 
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


"""
Input  : 
Output : 
"""
def PickSample( N, seed = None ):
    if seed != None:
        np.random.seed( seed )
        
    return np.random.randint( N )


"""
Input  : 
Output : 
"""
def CheckMistake( correct, hypothesis ):
    if hypothesis == correct:
        return False
    else :
        return True


"""
Input  : 
Output : 
"""
def UpdateW( w, y, x ):
    
    return w + y * x


"""
Input  : 
Output : 
"""
def Learning( data_file, x_0, w_0, thres, seed, scale_type, scale_size ):
    # 1. Load learning data
    x, y = LoadData( data_file, x_0, scale_type, scale_size )

    N    = x.shape[0]
    dim  = x.shape[1]
    iter_lim = int( 5*N )
    iter_num = 0
    
    # 2. initialize h and w 
    h = np.zeros( N )
    w       = np.full( (1, dim), w_0 )
    w[0, 0] = -thres

    # 3. Find correct w
    while True:
        # 3.a get h
        for i in range(N):
            temp = np.sign( np.dot(w, x[i, :]) )
            h[i] = 1 if temp > 0 else -1

        # 3.b pick one random sample
        idx = PickSample( N )

        # 3.c check mistake, update if wrong
        if CheckMistake( y[idx], h[idx] ):
            w = UpdateW( w, y[idx], x[idx, :] )
            iter_num = 1
        else:
            iter_num += 1

        # 3.d break if reach iteration limit
        if iter_num >= iter_lim: break
    
    return w



# ==============================
# Main
# ==============================
if __name__ == "__main__":
    
    """
    Input  : problem number
    OutPut : filename   : Raw data file name.
             x_0        : x_0 value.
             w_0        : Initial w_i value.
             thres      : Learning threshold (the 0th component of w).
             rate       : Learning rate.
             seed       : Random seed.
             scale_type : Method of scaling x_n.
             scale_size : The scaling magnitude of x_n.
                          ***ONLY work for SCALE_CONST***
             EXP_times  : The experiment number of PLA.
    """
    def Problem( prob_num ):
        if prob_num == 13:
            filename   = "./hw1_train.dat.txt"
            x_0        = 1.0
            w_0        = 0.0
            thres      = 0.0
            rate       = 1.0 
            seed       = None
            scale_type = SCALE_NONE
            scale_size = 1.0
            EXP_times  = 1000
            
        elif prob_num == 14:
            filename   = "./hw1_train.dat.txt"
            x_0        = 1.0
            w_0        = 0.0
            thres      = 0.0
            rate       = 1.0
            seed       = None 
            scale_type = SCALE_CONST
            scale_size = 2.0
            EXP_times  = 1000
            
        elif prob_num == 15:
            filename   = "./hw1_train.dat.txt"
            x_0        = 1.0 
            w_0        = 0.0
            thres      = 0.0 
            rate       = 1.0 
            seed       = None
            scale_type = SCALE_NORM
            scale_size = 1.0
            EXP_times  = 1000
            
        elif prob_num == 16:
            filename   = "./hw1_train.dat.txt"
            x_0        = 0.0
            w_0        = 0.0
            thres      = 0.0
            rate       = 1.0
            seed       = None
            scale_type = SCALE_NONE
            scale_size = 1.0
            EXP_times  = 1000
            
        else:
            print("WARNING: Specified not existence problem number. \
                            Setting the problem number to 13.")
            filename   = "./hw1_train.dat.txt"
            x_0        = 1.0
            w_0        = 0.0
            thres      = 0.0
            rate       = 1.0 
            seed       = None
            scale_type = SCALE_NONE
            scale_size = 1.0
            EXP_times  = 1000
        
        return filename, x_0, w_0, thres, rate, seed, \
               scale_type, scale_size, EXP_times

    PROBLEM_NUM = 16    #[ 13 / 14 / 15 / 16 ]

    raw_data_filename, x_0, w_0, threshold, rate, random_seed, \
                scale_type, scale_size, EXP_times = Problem( PROBLEM_NUM )

    w2 = 0.0 # w_PLA square length
    for i in range( EXP_times ):
        w_PLA = Learning( raw_data_filename, x_0, w_0, threshold, \
                          random_seed, scale_type, scale_size )
        w2 += np.sum( w_PLA * w_PLA )
    print( w2 / EXP_times )
    
