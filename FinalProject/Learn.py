SCALE_NONE  = 0
SCALE_CONST = 1
SCALE_NORM  = 2


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
