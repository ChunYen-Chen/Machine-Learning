import numpy as np

# load data
'''
Input       : file_name : 
Output      : 
Description : 
Note        :
'''
def LoadIDs( file_name ):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    
    category = lines[0].strip('\n')

    N = len(lines)-1
    
    ID_idx = {}
    data = [{} for i in range(N)]
    for i in range(N):
        lines[i+1] = lines[i+1].strip('\n')
        data[i][category] = lines[i+1]
        ID_idx[lines[i+1]] = i
    return ID_idx, data


'''
Input       : file_name : 
Output      : 
Description : 
Note        :
'''
def LoadData( ID_idx, data, file_name ):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    
    lines[0] = lines[0].strip('\n')
    category = lines[0].split(',')

    N = len(lines)-1
    
    for i in range(N):
        lines[i+1] = lines[i+1].strip('\n')
        temp       = lines[i+1].split(',')

        # check if the id exist in the current data
        idx = ID_idx.get(temp[0])
        if idx == None: continue

        for j in range(len(category)):
            #if temp[j] == '': temp[j] = 'Missing'
            data[idx][category[j]] = temp[j]
    return data


if __name__ == '__main__':
    test_data_file  = './data/Test_IDs.csv'
    train_data_file = './data/Train_IDs.csv'
    ID_idx_test, data_test   = LoadIDs( test_data_file )
    ID_idx_train, data_train = LoadIDs( train_data_file )

    all_data = ['./data/demographics.csv', './data/location.csv', './data/sample_submission.csv', \
                './data/satisfaction.csv', './data/services.csv', './data/status.csv', ]

    for i in range( len(all_data) ):
        data_train = LoadData( ID_idx_train, data_train, all_data[i] )
        data_test  = LoadData( ID_idx_test,  data_test,  all_data[i] )
    
    #data_file = './data/population.csv'
    #data_train = LoadData( ID_idx_train, data_train, data_file)
