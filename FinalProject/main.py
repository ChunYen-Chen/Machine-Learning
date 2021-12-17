import Load
import Error
from sklearn.linear_model import LogisticRegression

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

    # Churn or not
    data_train = Load.FixChurn( data_train, learn_type, DoCopy=True )
    data_test  = Load.FixChurn( data_test,  learn_type, DoCopy=True )

    # Select the parameter  ***The last parameter should be "Churn Category" which is "y"***
    train_parameter = [ 'Gender', 'Age', 'Under 30', 'Churn Category' ]

    # Take the data
    x_train, y_train = Load.DataSelect( data_train, train_parameter )
    x_test,  y_test  = Load.DataSelect( data_test,  train_parameter, False, True, 0.0 )
    
    
    # ====================================================================================================
    # Learning
    # ====================================================================================================
    reg = LogisticRegression(random_state=0).fit( x_train, y_train )

    
    # ====================================================================================================
    # Predicting
    # ====================================================================================================
    y_test = reg.predict( x_test )

    
    # ====================================================================================================
    # Write to file
    # ====================================================================================================
    Load.WriteData( write_file, data_test, y_test )
