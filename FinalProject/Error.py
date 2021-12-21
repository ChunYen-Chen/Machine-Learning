import numpy as np

ERROR_BIN      = 0         # binary error 0/1
ERROR_SQR      = 1         # square error
ERROR_CE       = 2         #

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

def Error_withTrue( y, y_true, mode ):
    if mode == ERROR_BIN:
        N = x.shape[0]
        error = ( y * x.dot(w) < 0 ).sum()
        error /= N
    elif mode == ERROR_SQR:
        error = np.mean( np.square( y_true - y ) )
    elif mode == ERROR_CE:
        print("Not supported mode yet.")
        error = 0.0
    else:
        print("Wrong error calculate mode.")
        exit()
    return error
