import Load
import Error
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression

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
    
    # long distance charge fixed
    data_train = Load.FixLongDistanceCharge( data_train )
    data_test  = Load.FixLongDistanceCharge( data_test  )

    # separate the category label to binary label
    data_train, extra_category = Load.Category2Binary( data_train )
    data_test,  extra_category = Load.Category2Binary( data_test  )
    #print(extra_category) 

    # Churn or not
    data_train = Load.FixChurn( data_train, learn_type, DoCopy=True )
    data_test  = Load.FixChurn( data_test,  learn_type, DoCopy=True )

    # ====================================================================================================
    # Select the training data
    # ====================================================================================================
    # Select the parameter
    # ***For the classification, the last parameter should be "Churn Category" which is "y"***
    """
    train_parameter = [ 'Offer None', 'Offer A', 'Offer B', 'Offer C', 'Offer D', 'Offer E',\
                        'Phone Service', 'Avg Monthly Long Distance Charges', 'Multiple Lines',\
                        'Internet None', 'Internet DSL', 'Internet Fiber Optic', 'Internet Cable',\
                        'Online Security', 'Online Backup', 'Device Protection Plan',\
                        'Premium Tech Support', 'Streaming TV', 'Streaming Movies', 'Streaming Music',\
                        'Unlimited Data', 'Paperless Billing', 'Monthly Charge']
    """
    train_parameter = [ 'Tenure in Months', 'Churn Category' ]

    # Take the data
    x_train, y_train, missing_train = Load.DataSelect( data_train, train_parameter, missing_array=True )
    x_test,  y_test,  missing_test  = Load.DataSelect( data_test,  train_parameter, False, True, 0.0, True )
    
    
    
    # ====================================================================================================
    # Learning
    # ====================================================================================================
    #reg = LogisticRegression(random_state=0).fit( x_train, y_train )
    reg = LinearRegression().fit( x_train, y_train )

    
    # ====================================================================================================
    # Predicting
    # ====================================================================================================
    y_predict = reg.predict( x_test )

    print(reg.score( x_train, y_train ))

    for i in range(len(train_parameter)):
        if i == 0 :
            print('%35s \t %.5f'%('x0', reg.coef_[i]))
            continue
        print('%35s \t %.5f'%(train_parameter[i-1], reg.coef_[i]))
    
    print(reg.intercept_)

    
    # ====================================================================================================
    # Write to file
    # ====================================================================================================
    Load.WriteData( write_file, data_test, y_predict, y_test )
    

    
    # ====================================================================================================
    # Write to file
    # ====================================================================================================
    err = Error.Error( x_train, y_train, reg.coef_, 1 )
    print(err)
    err = Error.Error_withTrue( y_predict, y_test, 1 )
    print(err)
