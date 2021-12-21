import Load
import numpy as np
import matplotlib.pylab as plt

def count( data, category, category_type, refer, refer_types ):
    counter = np.zeros(len(refer_types))
    
    for i in range(len(data)):
        for j in range(len(refer_types)):
            if data[i][category] == category_type:
                if data[i][refer] == refer_types[j]: counter[j] += 1
    return counter

if __name__ == '__main__':
    # ====================================================================================================
    # Presetting
    # ====================================================================================================
    test_data_file  = './data/Test_IDs.csv'
    train_data_file = './data/Train_IDs.csv'
    write_file      = './data/result.csv'
    all_data_files  = ['./data/demographics.csv', './data/location.csv', \
                       './data/satisfaction.csv', './data/services.csv', './data/status.csv', ]
    
    ID_idx_test,  data_test  = Load.LoadIDs( test_data_file  )
    ID_idx_train, data_train = Load.LoadIDs( train_data_file )

    
    learn_type = 1      # which learn algorithm TODO
    
    # all the category in the data sets which is fixed.
    category = ['Customer ID', 'Count', 'Gender', 'Age', 'Under 30', 'Senior Citizen', 'Married', \
                'Dependents', 'Number of Dependents', 'Country', 'State', 'City', 'Zip Code', \
                'Lat Long', 'Latitude', 'Longitude', 'Satisfaction Score', 'Quarter', 'Referred a Friend', \
                'Number of Referrals', 'Tenure in Months', 'Offer', 'Phone Service', \
                'Avg Monthly Long Distance Charges', 'Multiple Lines', 'Internet Service', 'Internet Type', \
                'Avg Monthly GB Download', 'Online Security', 'Online Backup', 'Device Protection Plan', \
                'Premium Tech Support', 'Streaming TV', 'Streaming Movies', 'Streaming Music', \
                'Unlimited Data', 'Contract', 'Paperless Billing', 'Payment Method', 'Monthly Charge', \
                'Total Charges', 'Total Refunds', 'Total Extra Data Charges', 'Total Long Distance Charges', \
                'Total Revenue', 'Churn Category']
    

    # ====================================================================================================
    # Load data
    # ====================================================================================================
    for i in range( len(all_data_files) ):
        data_train = Load.LoadData( ID_idx_train, data_train, all_data_files[i] )
        data_test  = Load.LoadData( ID_idx_test,  data_test,  all_data_files[i] )
    
    #data_file = './data/population.csv'
    #data_train = LoadData( ID_idx_train, data_train, data_file )

    
    # ====================================================================================================
    # Data processes
    # ====================================================================================================
    data_train = Load.DataFillEmpty( data_train, category )
    data_test  = Load.DataFillEmpty( data_test,  category )

    # under 30 and above 65 fixed
    data_train = Load.FixAge( data_train )
    data_test  = Load.FixAge( data_test  )

    # dependent fixed
    data_train = Load.FixDependent( data_train )
    data_test  = Load.FixDependent( data_test  )
    
    # referred fixed
    data_train = Load.FixLoction( data_train )
    data_test  = Load.FixLoction( data_test  )
    
    # location fixed
    data_train = Load.FixReferred( data_train )
    data_test  = Load.FixReferred( data_test  )
    
    # internet sevice fixed
    data_train = Load.FixInetrnet( data_train )
    data_test  = Load.FixInetrnet( data_test  )

    # data usage fixed
    data_train = Load.FixDataUsage( data_train )
    data_test  = Load.FixDataUsage( data_test  )

    # separate the category label to binary label
    data_train, extra_category = Load.Category2Binary( data_train )
    data_test,  extra_category = Load.Category2Binary( data_test  )

    # Churn or not
    data_train = Load.FixChurn( data_train, learn_type, DoCopy=True )
    data_test  = Load.FixChurn( data_test,  learn_type, DoCopy=True )

    numberA = count( data_train, 'Offer', 1.0, 'Unlimited Data', [0.0, 1.0] )
    numberB = count( data_train, 'Offer', 2.0, 'Unlimited Data', [0.0, 1.0] )
    numberC = count( data_train, 'Offer', 3.0, 'Unlimited Data', [0.0, 1.0] )
    numberD = count( data_train, 'Offer', 4.0, 'Unlimited Data', [0.0, 1.0] )
    numberE = count( data_train, 'Offer', 5.0, 'Unlimited Data', [0.0, 1.0] )
    print(numberA)
    print(numberB)
    print(numberC)
    print(numberD)
    print(numberE)
    
    numberA = count( data_train, 'Dependents', 0.0, 'Multiple Lines', [0.0, 1.0] )
    numberB = count( data_train, 'Dependents', 1.0, 'Multiple Lines', [0.0, 1.0] )
    print(numberA)
    print(numberB)
