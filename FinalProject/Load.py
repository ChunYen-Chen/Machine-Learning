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
    print( 'Loading: %s'%(file_name) )
    
    with open(file_name, 'r') as f:
        lines = f.readlines()
    
    lines[0] = lines[0].strip('\n')
    category = lines[0].split(',')
    #print(category)

    N = len(lines)-1
    
    for i in range(N):
        lines[i+1] = lines[i+1].strip('\n')
        temp       = lines[i+1].split(',')

        # check if the id exist in the current data
        idx = ID_idx.get(temp[0])
        if idx == None: continue

        for j in range(len(category)):
            #if temp[j] == '': temp[j] = 'Missing'
            data[idx][category[j]] = DataTransfer ( category[j], temp[j] )
    return data


"""
Customer ID                       : unique string
Count                             : 1.0 for all data
Gender                            : Male: 0.0, Female: 1.0

Age                               : float
Under 30                          : No: 0.0, Yes: 1.0
Senior Citizen                    : No: 0.0, Yes: 1.0

Married                           : No: 0.0, Yes: 1.0

Dependents                        : No: 0.0, Yes: 1.0
Number of Dependents              : float

Country                           : Class
State                             : Class
City                              : Class

Zip Code                          : float
Lat Long                          : float
Latitude                          : float
Longitude                         : float

Satisfaction Score                : float
Quarter                           : All Q3
Referred a Friend                 : No: 0.0, Yes: 1.0
Number of Referrals               : float
Tenure in Months                  : float
Offer                             : Offer A: 1.0, Offer B: 2.0, Offer C: 3.0, Offer D: 4.0, Offer E: 5.0
Phone Service                     : No: 0.0, Yes: 1.0
Avg Monthly Long Distance Charges : float
Multiple Lines                    : No: 0.0, Yes: 1.0

Internet Service                  : No: 0.0, Yes: 1.0
Internet Type                     : No: 0.0, DSL: 1.0, Fiber: 2.0, Optic: 3.0, Cable: 4.0

Avg Monthly GB Download           : float
Online Security                   : No: 0.0, Yes: 1.0
Online Backup                     : No: 0.0, Yes: 1.0
Device Protection Plan            : No: 0.0, Yes: 1.0
Premium Tech Support              : No: 0.0, Yes: 1.0
Streaming TV                      : No: 0.0, Yes: 1.0
Streaming Movies                  : No: 0.0, Yes: 1.0
Streaming Music                   : No: 0.0, Yes: 1.0
Unlimited Data                    : No: 0.0, Yes: 1.0
Contract                          : Month-to-Month: 1.0, One Year: 2.0, Two Year: 3.0
Paperless Billing                 : No: 0.0, Yes: 1.0
Payment Method                    : Bank Withdrawal: 1.0, Credit Card: 2.0, Mailed Chack: 3.0
Monthly Charge                    : float
Total Charges                     : float
Total Refunds                     : float
Total Extra Data Charges          : float
Total Long Distance Charges       : float
Total Revenue                     : float
Churn Category                    : No Churn: 0, Competitor: 1, Dissatisfaction: 2, Attitude: 3, Price: 4, Other: 5
"""
def DataTransfer( category, string ):
    if   category == 'Customer ID':                       return string
    elif category == 'Count':                             return numberTrans(string)
    elif category == 'Gender':                            return YesNoTrans(string)
    elif category == 'Age':                               return numberTrans(string)
    elif category == 'Under 30':                          return YesNoTrans(string)
    elif category == 'Senior Citizen':                    return YesNoTrans(string)
    elif category == 'Married':                           return YesNoTrans(string)
    elif category == 'Dependents':                        return YesNoTrans(string)
    elif category == 'Number of Dependents':              return numberTrans(string)
    elif category == 'Country':                           return string
    elif category == 'State':                             return string
    elif category == 'City':                              return string
    elif category == 'Zip Code':                          return numberTrans(string)
    elif category == 'Lat Long':                          return string #TODO
    elif category == 'Latitude':                          return string #TODO
    elif category == 'Longitude':                         return string #TODO
    elif category == 'Satisfaction Score':                return numberTrans(string)
    elif category == 'Quarter':                           return string
    elif category == 'Referred a Friend':                 return YesNoTrans(string)
    elif category == 'Number of Referrals':               return numberTrans(string)
    elif category == 'Tenure in Months':                  return numberTrans(string)
    elif category == 'Offer':                             return OtherTrans(string)
    elif category == 'Phone Service':                     return YesNoTrans(string)
    elif category == 'Avg Monthly Long Distance Charges': return numberTrans(string)
    elif category == 'Multiple Lines':                    return YesNoTrans(string)
    elif category == 'Internet Service':                  return YesNoTrans(string)
    elif category == 'Internet Type':                     return OtherTrans(string)
    elif category == 'Avg Monthly GB Download':           return numberTrans(string)
    elif category == 'Online Security':                   return YesNoTrans(string)
    elif category == 'Online Backup':                     return YesNoTrans(string)
    elif category == 'Device Protection Plan':            return YesNoTrans(string)
    elif category == 'Premium Tech Support':              return YesNoTrans(string)
    elif category == 'Streaming TV':                      return YesNoTrans(string)
    elif category == 'Streaming Movies':                  return YesNoTrans(string)
    elif category == 'Streaming Music':                   return YesNoTrans(string)
    elif category == 'Unlimited Data':                    return YesNoTrans(string)
    elif category == 'Contract':                          return OtherTrans(string)
    elif category == 'Paperless Billing':                 return YesNoTrans(string)
    elif category == 'Payment Method':                    return OtherTrans(string)
    elif category == 'Monthly Charge':                    return numberTrans(string)
    elif category == 'Total Charges':                     return numberTrans(string)
    elif category == 'Total Refunds':                     return numberTrans(string)
    elif category == 'Total Extra Data Charges':          return numberTrans(string)
    elif category == 'Total Long Distance Charges':       return numberTrans(string)
    elif category == 'Total Revenue':                     return numberTrans(string)
    elif category == 'Churn Category':                    return OtherTrans(string)
    else:
        print("Can't find the category: %s"%(string))
        exit()
    return 


def YesNoTrans( string ):
    if   string == 'Yes':    return 1.0
    elif string == 'No':     return 0.0
    elif string == 'Male':   return 0.0
    elif string == 'Female': return 1.0
    elif string == '':       return None
    else:
        print("Input string is not 'Yes' or 'No': %s"%(string))
        exit()
    return

def numberTrans( string ):
    if string == '': return None
    return float(string)


def OtherTrans( string ):
    if   string == 'None':    return 0.0
    elif string == 'Offer A': return 1.0
    elif string == 'Offer B': return 2.0
    elif string == 'Offer C': return 3.0
    elif string == 'Offer D': return 4.0
    elif string == 'Offer E': return 5.0

    elif string == 'No':          return 0.0
    elif string == 'DSL':         return 1.0
    elif string == 'Fiber Optic': return 2.0
    elif string == 'Cable':       return 3.0

    elif string == 'Month-to-Month': return 1.0
    elif string == 'One Year':       return 2.0
    elif string == 'Two Year':       return 3.0

    elif string == 'Bank Withdrawal': return 1.0
    elif string == 'Credit Card':     return 2.0
    elif string == 'Mailed Check':    return 3.0
    
    elif string == 'No Churn':        return 0.0
    elif string == 'Competitor':      return 1.0
    elif string == 'Dissatisfaction': return 2.0
    elif string == 'Attitude':        return 3.0
    elif string == 'Price':           return 4.0
    elif string == 'Other':           return 5.0

    elif string == '': return None
    else:
        print("Input string is not the given string: %s"%(string))
        exit()
    return


def DataFillEmpty( data, category ):
    print('Filling the empty data with None.')
    for i in range(len(data)):
        for key in category:
            if key not in data[i]:
                data[i][key] = None
    return data


'''
Input       : throw    : Don't pick the data with empty value.
              fill_num : fill the None with number
              parameters: The last parameter should always be the y of the data
Output      : 
Description : 
Note        :
'''
def DataSelect( data, parameters, throw=True, fill=False, fill_num=0.0 ):
    print('Selecting the data with given category.')
    # Check if None
    idxs = []
    if throw:
        for i in range( len(data) ):
            temp = False
            for j in data[i]:
                if data[i][j] == None: temp = True
            if not temp: idxs.append(i)
    elif fill:
        idxs = [i for i in range(len(data))]
        for i in range( len(data) ):
            for j in data[i]:
                if data[i][j] == None: temp = fill_num
    else:
        idxs = [i for i in range(len(data))]

    # Select data
    x = np.ones( (len(idxs), len(parameters)) )
    y = np.zeros( len(idxs) )
    for i in range(len(idxs)):
        for j in range(len(parameters)-1):
            x[i, j+1] = data[idxs[i]][parameters[j]]
        y[i] = data[idxs[i]][parameters[-1]]

    return x, y


def FixAge( data ):
    print('Fixing the Age category.')
    for i in range(len(data)):
        if data[i]['Age'] == None: continue

        if data[i]['Age'] < 30:  data[i]['Under 30'] = 1.0
        else:                    data[i]['Under 30'] = 0.0
        
        if data[i]['Age'] >= 65: data[i]['Senior Citizen'] = 1.0
        else:                    data[i]['Senior Citizen'] = 0.0
    return data


def FixDependent( data ):
    print('Fixing the Dependent category.')
    for i in range(len(data)):
        if data[i]['Dependents'] == 0.0:  data[i]['Number of Dependents'] = 0.0
        
        if   data[i]['Number of Dependents'] == None: continue
        elif data[i]['Number of Dependents'] == 0.0:  data[i]['Dependents'] = 0.0
        elif data[i]['Number of Dependents'] != 0.0:  data[i]['Dependents'] = 1.0
        
    return data


def FixReferred( data ):
    print('Fixing the Referred category.')
    for i in range(len(data)):
        if data[i]['Referred a Friend'] == 0.0:  data[i]['Number of Referrals'] = 0.0
        
        if   data[i]['Number of Referrals'] == None: continue
        elif data[i]['Number of Referrals'] == 0.0:  data[i]['Referred a Friend'] = 0.0
        elif data[i]['Number of Referrals'] != 0.0:  data[i]['Referred a Friend'] = 1.0
    return data


def FixInetrnet( data ):
    print('Fixing the Internet category.')
    for i in range(len(data)):
        if   data[i]['Internet Type'] == None: continue
        elif data[i]['Internet Type'] == 0.0:  data[i]['Internet Service'] = 0.0
        elif data[i]['Internet Type'] != 0.0:  data[i]['Internet Service'] = 1.0
    return data


def FixChurn( data, learn_type ):
    print('Fixing the Internet category.')
    for i in range(len(data)):
        if learn_type == 0:
            break
        elif learn_type == 1:
            if   data[i]['Churn Category'] == None: continue
            elif data[i]['Churn Category'] == 0.0:  data[i]['Churn Category'] = 0.0
            elif data[i]['Churn Category'] != 0.0:  data[i]['Churn Category'] = 1.0
    return data
