import numpy as np 


SCALE_NONE  = 0
SCALE_CONST = 1
SCALE_NORM  = 2


def sign( y_in ):
    N = len(y_in)
    y = np.zeros(N)
    for i in range(N):
        y[i] = 1.0 if y_in[i] > 0 else -1
    return y

def OneDRay( x_in, y_in, D_in, missing=None ):
    N = x_in.shape[0]
    idxs = np.argsort(x_in)
    
    x = x_in[idxs]
    y = y_in[idxs]
    D = D_in[idxs]
    w =  np.zeros(2)

    min_errP = N
    min_idxP = 0
    min_errN = N
    min_idxN = 0
    for i in range(N):
        err_countP = 0
        err_countN = 0
        if i != 0:
            if x[i] == x[i-1]: continue

        if type(missing) != type(None):
            for j in range(0, i):
                if y[j] ==  1 or missing[j] == 1: err_countP += D[j]
                if y[j] == -1: err_countN += D[j]
            for j in range(i, N):
                if y[j] == -1: err_countP += D[j]
                if y[j] ==  1 or missing[j] == 1: err_countN += D[j]
        else:
            for j in range(0, i):
                if y[j] ==  1: err_countP += D[j]
                if y[j] == -1: err_countN += D[j]
            for j in range(i, N):
                if y[j] == -1: err_countP += D[j]
                if y[j] ==  1: err_countN += D[j]

        if err_countP <= min_errP:
            min_errP = err_countP
            min_idxP = i
        
        if err_countN <= min_errN:
            min_errN = err_countN
            min_idxN = i
        #print('%.5f %.5f %.5f %.5f'%(err_countN, min_errN, err_countP, min_errP))

    if min_errP < min_errN:
        w[0] = -0.5 * ( x[min_idxP] + x[min_idxP-1] ) if min_idxP != 0 else x[min_idxP]
        w[1] = 1
        err  = min_errP
    else:
        w[0] = 0.5 * ( x[min_idxN] + x[min_idxN-1] ) if min_idxN != 0 else x[min_idxN]
        w[1] = -1
        err  = min_errN

    return w, err

def PLA( x, y, w_0, thres, seed, scale_type, scale_size ):
    N    = x.shape[0]
    dim  = x.shape[1]
    iter_lim = int( 5*N )
    iter_num = 0
    
    # 1. initialize h and w 
    h = np.zeros( N )
    w       = np.full( (1, dim), w_0 )
    w[0, 0] = -thres

    # 2. Find correct w
    while True:
        # 2.a get h
        for i in range(N):
            temp = np.sign( np.dot(w, x[i, :]) )
            h[i] = 1 if temp > 0 else -1

        # 2.b pick one random sample
        idx = PickSample( N )

        # 2.c check mistake, update if wrong
        if CheckMistake( y[idx], h[idx] ):
            w = UpdateW( w, y[idx], x[idx, :] )
            iter_num = 1
        else:
            iter_num += 1

        # 2.d break if reach iteration limit
        if iter_num >= iter_lim: break
    
    return w


def LinearRegression( x, y ):
    # 0. Setup
    dim = x.shape[1]
    w   = np.zeros( (dim, 1) )
    
    # 1. Calculate X^{\dagger}
    x_dagger = np.linalg.pinv( x )
    
    # 2. w_{LIN} = X^{\dagger} Y
    w = x_dagger.dot( y )
    
    return w


def LogisticFunc( x ):
    return 1. / ( 1. + np.exp(-x) )


def LogisticRegression( x, y, rate, iter_num ):
    # 0. Setup
    N   = x.shape[0]
    dim = x.shape[1]
    w   = np.zeros( (dim, 1) )

    for i in range( iter_num ):
        # 1. Calculate \grad E_in
        theta = LogisticFunc( ( -y*x ).dot(w) )
        gradE = ( -y*x ).T.dot(theta) / N

        # 2. Update
        w -= rate * gradE
    
    return w


def weaklearn( x, y, D, missing=None ):
    N   = x.shape[0]
    dim = x.shape[1] # number of classifier

    err_count = np.zeros(dim)
    w_all = np.zeros( (dim, 2) )
    w = np.zeros( (dim, 1) )
    for i in range(dim):
        if type(missing) != type(None):
            w_all[i], err_count[i] = OneDRay( x[:, i], y, D, missing[:, i] )
        else:
            w_all[i], err_count[i] = OneDRay( x[:, i], y, D )
        #print(w_all[i], err_count[i])
   
    # find the minimum category
    idx  = np.argmin(err_count)
    w[0]   = w_all[idx][0]
    w[idx] = w_all[idx][1]

    return w, err_count[idx]

# current supported discrete (0/1)
def ADABoost( x, y, iter_max, missing=None ):
    N   = x.shape[0]
    dim = x.shape[1]
    
    w_tot = np.zeros( (iter_max, dim) )
    w_ada = np.zeros( (dim, 1) )
    D = np.ones(N) / N
    alpha = np.zeros(iter_max)

    learn = False
    t = 0
    while not learn:
        # weak learn
        w_temp, err = weaklearn( x, y, D, missing )

        for i in range(dim):
            w_tot[t][i] = w_temp[i]
        
        h = sign(x.dot(w_tot[t].T))

        # record error
        # err = 0
        # for i in range(N):
        #     if h[i] != y[i]: err += D[i]

        # learned
        if err < 1.e-10:
            learn = True
            # delete the empty w and alpha
            break

        # calculate alpha
        alpha[t] = 0.5 * np.log( (1-err) / err )

        # update choose weight
        D = D * np.exp( alpha[t]*y*h )

        # renormalize
        D = D / D.sum()

        #print('alpha:', alpha[t])
        #print(w_temp)
        # add iteration number
        t += 1
        print('Iteration: %03d, Error: %.5f'%(t, err))
        
        # check of reach maximum iteration number
        if t == iter_max: break
    
    w_ada = alpha.dot(w_tot)

    return w_ada 


def ValidateLearn( x, y, iter_max=None, missing=None ):
    
    return w
