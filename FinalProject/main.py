import os
import Load
import Error
import Learn
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression

def recorded_train_parameter( num ):
    if num == 0:
        train_parameter = [ 'Offer None', 'Offer A', 'Offer B', 'Offer C', 'Offer D', 'Offer E',\
                            'Phone Service', 'Avg Monthly Long Distance Charges', 'Multiple Lines',\
                            'Internet None', 'Internet DSL', 'Internet Fiber Optic', 'Internet Cable',\
                            'Online Security', 'Online Backup', 'Device Protection Plan',\
                            'Premium Tech Support', 'Streaming TV', 'Streaming Movies', \
                            'Streaming Music', 'Unlimited Data', 'Paperless Billing', 'Payment Bank',\
                            'Payment Credit', 'Payment Mailed', 'Monthly Charge']
    elif num == 1:
        train_parameter = ['Gender', 'Married',\
                           'Under 30', 'Senior Citizen', \
                           'Dependents', 'Number of Dependents', \
                           'Satisfaction 1', 'Satisfaction 2', 'Satisfaction 3', 'Satisfaction 4', 'Satisfaction 5',
                           'Referred a Friend', 'Number of Referrals',\
                           'Tenure in Months',\
                           'Offer None', 'Offer A', 'Offer B', 'Offer C', 'Offer D', 'Offer E',\
                           'Phone Service', 'Avg Monthly Long Distance Charges', 'Multiple Lines', \
                           'Internet Service', 'Internet None', 'Internet DSL', 'Internet Fiber Optic', 'Internet Cable', \
                           'Avg Monthly GB Download', 'Online Security', \
                           'Online Backup', 'Device Protection Plan', 'Premium Tech Support', \
                           'Streaming TV', 'Streaming Movies', 'Streaming Music', 'Unlimited Data', \
                           'Contract M2M', 'Contract 1Y', 'Contract 2Y', \
                           'Paperless Billing', 'Payment Bank', 'Payment Credit', 'Payment Mailed', \
                           'Monthly Charge', \
                           'Total Charges', 'Total Refunds', 'Total Extra Data Charges', \
                           'Total Long Distance Charges', 'Total Revenue', \
                           'Churn Category']
    elif num == 2:
        train_parameter = ['Gender', 'Married',\
                           'Under 30', 'Senior Citizen', \
                           'Dependents', 'Number of Dependents', \
                           'Satisfaction 1', 'Satisfaction 2', 'Satisfaction 3', 'Satisfaction 4', 'Satisfaction 5',
                           'Referred a Friend', 'Number of Referrals',\
                           'Tenure in Months',\
                           'Offer None', 'Offer A', 'Offer B', 'Offer C', 'Offer D', 'Offer E',\
                           'Phone Service', 'Avg Monthly Long Distance Charges', 'Multiple Lines', \
                           'Internet Service', 'Internet None', 'Internet DSL', 'Internet Fiber Optic', 'Internet Cable', \
                           'Avg Monthly GB Download', 'Online Security', \
                           'Online Backup', 'Device Protection Plan', 'Premium Tech Support', \
                           'Streaming TV', 'Streaming Movies', 'Streaming Music', 'Unlimited Data', \
                           'Contract M2M', 'Contract 1Y', 'Contract 2Y', \
                           'Paperless Billing', 'Payment Bank', 'Payment Credit', 'Payment Mailed', \
                           'Monthly Charge', \
                           'Total Charges', 'Total Refunds', 'Total Extra Data Charges', \
                           'Total Long Distance Charges', 'Total Revenue', \
                           'Competitor']
    elif num == 3:
        train_parameter = ['Gender', 'Married',\
                           'Under 30', 'Senior Citizen', \
                           'Dependents', 'Number of Dependents', \
                           'Satisfaction 1', 'Satisfaction 2', 'Satisfaction 3', 'Satisfaction 4', 'Satisfaction 5',
                           'Referred a Friend', 'Number of Referrals',\
                           'Tenure in Months',\
                           'Offer None', 'Offer A', 'Offer B', 'Offer C', 'Offer D', 'Offer E',\
                           'Phone Service', 'Avg Monthly Long Distance Charges', 'Multiple Lines', \
                           'Internet Service', 'Internet None', 'Internet DSL', 'Internet Fiber Optic', 'Internet Cable', \
                           'Avg Monthly GB Download', 'Online Security', \
                           'Online Backup', 'Device Protection Plan', 'Premium Tech Support', \
                           'Streaming TV', 'Streaming Movies', 'Streaming Music', 'Unlimited Data', \
                           'Contract M2M', 'Contract 1Y', 'Contract 2Y', \
                           'Paperless Billing', 'Payment Bank', 'Payment Credit', 'Payment Mailed', \
                           'Monthly Charge', \
                           'Total Charges', 'Total Refunds', 'Total Extra Data Charges', \
                           'Total Long Distance Charges', 'Total Revenue', \
                           'Dissatisfaction']
    elif num == 4:
        train_parameter = ['Gender', 'Married',\
                           'Under 30', 'Senior Citizen', \
                           'Dependents', 'Number of Dependents', \
                           'Satisfaction 1', 'Satisfaction 2', 'Satisfaction 3', 'Satisfaction 4', 'Satisfaction 5',
                           'Referred a Friend', 'Number of Referrals',\
                           'Tenure in Months',\
                           'Offer None', 'Offer A', 'Offer B', 'Offer C', 'Offer D', 'Offer E',\
                           'Phone Service', 'Avg Monthly Long Distance Charges', 'Multiple Lines', \
                           'Internet Service', 'Internet None', 'Internet DSL', 'Internet Fiber Optic', 'Internet Cable', \
                           'Avg Monthly GB Download', 'Online Security', \
                           'Online Backup', 'Device Protection Plan', 'Premium Tech Support', \
                           'Streaming TV', 'Streaming Movies', 'Streaming Music', 'Unlimited Data', \
                           'Contract M2M', 'Contract 1Y', 'Contract 2Y', \
                           'Paperless Billing', 'Payment Bank', 'Payment Credit', 'Payment Mailed', \
                           'Monthly Charge', \
                           'Total Charges', 'Total Refunds', 'Total Extra Data Charges', \
                           'Total Long Distance Charges', 'Total Revenue', \
                           'Attitude']
    elif num == 5:
        train_parameter = ['Gender', 'Married',\
                           'Under 30', 'Senior Citizen', \
                           'Dependents', 'Number of Dependents', \
                           'Satisfaction 1', 'Satisfaction 2', 'Satisfaction 3', 'Satisfaction 4', 'Satisfaction 5',
                           'Referred a Friend', 'Number of Referrals',\
                           'Tenure in Months',\
                           'Offer None', 'Offer A', 'Offer B', 'Offer C', 'Offer D', 'Offer E',\
                           'Phone Service', 'Avg Monthly Long Distance Charges', 'Multiple Lines', \
                           'Internet Service', 'Internet None', 'Internet DSL', 'Internet Fiber Optic', 'Internet Cable', \
                           'Avg Monthly GB Download', 'Online Security', \
                           'Online Backup', 'Device Protection Plan', 'Premium Tech Support', \
                           'Streaming TV', 'Streaming Movies', 'Streaming Music', 'Unlimited Data', \
                           'Contract M2M', 'Contract 1Y', 'Contract 2Y', \
                           'Paperless Billing', 'Payment Bank', 'Payment Credit', 'Payment Mailed', \
                           'Monthly Charge', \
                           'Total Charges', 'Total Refunds', 'Total Extra Data Charges', \
                           'Total Long Distance Charges', 'Total Revenue', \
                           'Price']
    elif num == 6:
        train_parameter = ['Gender', 'Married',\
                           'Under 30', 'Senior Citizen', \
                           'Dependents', 'Number of Dependents', \
                           'Satisfaction 1', 'Satisfaction 2', 'Satisfaction 3', 'Satisfaction 4', 'Satisfaction 5',
                           'Referred a Friend', 'Number of Referrals',\
                           'Tenure in Months',\
                           'Offer None', 'Offer A', 'Offer B', 'Offer C', 'Offer D', 'Offer E',\
                           'Phone Service', 'Avg Monthly Long Distance Charges', 'Multiple Lines', \
                           'Internet Service', 'Internet None', 'Internet DSL', 'Internet Fiber Optic', 'Internet Cable', \
                           'Avg Monthly GB Download', 'Online Security', \
                           'Online Backup', 'Device Protection Plan', 'Premium Tech Support', \
                           'Streaming TV', 'Streaming Movies', 'Streaming Music', 'Unlimited Data', \
                           'Contract M2M', 'Contract 1Y', 'Contract 2Y', \
                           'Paperless Billing', 'Payment Bank', 'Payment Credit', 'Payment Mailed', \
                           'Monthly Charge', \
                           'Total Charges', 'Total Refunds', 'Total Extra Data Charges', \
                           'Total Long Distance Charges', 'Total Revenue', \
                           'Other']
    elif num == 7:
        train_parameter = ['Satisfaction 1', 'Satisfaction 2', 'Satisfaction 3', 'Satisfaction 4', 'Satisfaction 5',
                           'Churn Category']
    else:
        exit('You did not record such a train parameter: %d'%num)
    return train_parameter



def load_data( train_or_test ):
    if train_or_test == 'train':
        data_file = './data/Train_IDs.csv'
        record_data_file = './data/all_train.csv'
    
    elif train_or_test == 'test':
        data_file  = './data/Test_IDs.csv'
        record_data_file = './data/all_test.csv'
    
    else:
        exit('Wrong type')
    
    if os.path.isfile(record_data_file):
        ID_idx, data = Load.LoadIDs( data_file )
        data = Load.LoadData( ID_idx, data, record_data_file, DoneTrans=True )
        return ID_idx, data

    ID_idx, data = Load.LoadIDs( data_file )
    
    learn_type = 1      # which learn algorithm TODO

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
    
    all_data_files  = ['./data/demographics.csv', './data/location.csv', \
                       './data/satisfaction.csv', './data/services.csv', './data/status.csv', ]
    
    for i in range( len(all_data_files) ):
        data = Load.LoadData( ID_idx, data, all_data_files[i] )
    
    #data_file = './data/population.csv'
    #data_train = LoadData( ID_idx_train, data_train, data_file )
    
    data = Load.DataFillEmpty( data, category )
    
    data = Load.FixAge( data )                # under 30 and above 65 fixed
    data = Load.FixDependent( data )          # dependent fixed
    data = Load.FixLoction( data )            # referred fixed
    data = Load.FixReferred( data )           # location fixed
    data = Load.FixInetrnet( data )           # internet sevice fixed
    data = Load.FixDataUsage( data )          # data usage fixed
    data = Load.FixLongDistanceCharge( data ) # long distance charge fixed

    # separate the category label to binary label
    data, extra_category = Load.Category2Binary( data )

    # Churn or not
    data = Load.FixChurn( data, learn_type, DoCopy=True )
   
    # Record the data after transformation
    Load.WriteData( record_data_file, data )

    return ID_idx, data

if __name__ == '__main__':
    # ====================================================================================================
    # Presetting
    # ====================================================================================================
    write_file      = './data/result.csv'
    
    # all the category in the data sets which is fixed.
    category = ['Customer ID', 'Count', 'Gender', 'Age', 'Under 30', 'Senior Citizen', 'Married', \
                'Dependents', 'Number of Dependents', 'Country', 'State', 'City', 'Zip Code', \
                'Lat Long', 'Latitude', 'Longitude', 'Satisfaction score', 'Quarter', 'Referred a Friend', \
                'Number of Referrals', 'Tenure in Months', 'Offer', 'Phone Service', \
                'Avg Monthly Long Distance Charges', 'Multiple Lines', 'Internet Service', 'Internet Type', \
                'Avg Monthly GB download', 'Online Security', 'Online Backup', 'Device Protection Plan', \
                'Premium Tech Support', 'Streaming TV', 'Streaming Movies', 'Streaming Music', \
                'Unlimited Data', 'Contract', 'Paperless Billing', 'Payment Method', 'Monthly Charge', \
                'Total Charges', 'Total Refunds', 'Total Extra Data Charges', 'Total Long Distance Charges', \
                'Total Revenue', 'Churn Category']
    

    # ====================================================================================================
    # Load data & Data process
    # ====================================================================================================
    ID_idx_test,  data_test  = load_data('test')
    ID_idx_train, data_train = load_data('train')
    

    # ====================================================================================================
    # Select the training data
    # ====================================================================================================
    # Select the parameter
    # ***For the classification, the last parameter should be "Churn Category" which is "y"***
    
    #train for the monthly charge
    train_parameter = recorded_train_parameter( 0 )
    
    #train_parameter = [ 'Tenure in Months', 'Unlimited Data', 'Churn Category' ]
    #train_parameter = [ 'Unlimited Data', 'Churn Category' ]

    # Take the data
    x_train, y_train, missing_train = Load.DataSelect( data_train, train_parameter, missing_array=True )
    #x_train, y_train, missing_train = Load.DataSelect( data_train, train_parameter, False, True, 0.0, True )
    x_test,  y_test,  missing_test  = Load.DataSelect( data_test,  train_parameter, False, True, 0.0, True )
    
    
    
    # ====================================================================================================
    # Learning
    # ====================================================================================================
    #reg = LogisticRegression(random_state=0).fit( x_train, y_train )
    reg = LinearRegression().fit( x_train, y_train )
    w = Learn.ADABoost( x_train[0:60, :], y_train[0:60], 30, missing_train )
    #print(w)

    
    # ====================================================================================================
    # Predicting
    # ====================================================================================================
    y_predict = reg.predict( x_test )
    y_predict2 = Learn.sign(x_train[60:].dot(w))
    y_predict = Learn.sign(x_test.dot(w))
    #print(w)
    #print(y_predict2)

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
    # Load.WriteData( write_file, data_test, y_predict, y_test )
    for i in range(len(y_predict)):
        if y_predict[i] == -1: y_predict[i] = 0
    Load.WriteResult( write_file, data_test, y_predict )
    

    
    # ====================================================================================================
    # Error measurement
    # ====================================================================================================
    print('Error')
    err = Error.Error( x_train, y_train, reg.coef_.T, 1 )
    print(err)
    err = Error.Error_withTrue( y_predict, y_test, 1 )
    print(err)
    err = Error.Error_withTrue( y_predict2, y_train[60:], 1 )
    print(err)
    
