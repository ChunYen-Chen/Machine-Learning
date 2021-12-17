import numpy as np
import copy


"""
General Parameter: 
    DoCpoy: If True, copy the input list, but it is time consuming.
"""



def WriteData( file_name, data, y ):
    print( 'Writing the file to %s'%file_name )
    with open( file_name, 'w' ) as f:
        for i in range(len(y)):
            f.write( '%s,%s\n'%(data[i]['Customer ID'], str(int(y[i]))) )
    return


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
def LoadData( ID_idx, data_in, file_name, DoCopy=False ):
    print( 'Loading: %s'%(file_name) )

    data = copy.deepcopy(data_in) if DoCopy else data_in
    
    with open(file_name, 'r') as f:
        lines = f.readlines()
    
    lines[0] = lines[0].strip('\n')
    category = lines[0].split(',')
    #print(category)

    N = len(lines)-1
    
    for i in range(N):
        lines[i+1] = lines[i+1].strip('\n')
        temp       = lines[i+1].split(',')
        N_data = len(temp)
        N_category = len(category)

        # check if the id exist in the current data
        idx = ID_idx.get(temp[0])
        if idx == None: continue

        for j in range(N_category):
            if N_data != N_category: 
                if category[j] == 'Lat Long': cell_data = temp[j][1:]+','+temp[j+1][:-1]
                elif category[j] == 'Latitude': cell_data = temp[j+1]
                elif category[j] == 'Longitude': cell_data = temp[j+1]
                else: cell_data = temp[j]
            else:
                cell_data = temp[j]
            data[idx][category[j]] = DataTransfer ( category[j], cell_data )
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

Country                           : All United State
State                             : All California
City                              : Class

Zip Code                          : float
Lat Long                          : (float, float)
Latitude                          : float
Longitude                         : float

Satisfaction Score                : float
Quarter                           : All Q3
Referred a Friend                 : No: 0.0, Yes: 1.0
Number of Referrals               : float
Tenure in Months                  : float
Offer                             : None: 0.0, Offer A: 1.0, Offer B: 2.0, Offer C: 3.0, Offer D: 4.0, Offer E: 5.0
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
    elif category == 'Latitude':                          return numberTrans(string)
    elif category == 'Longitude':                         return numberTrans(string)
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
        exit("Can't find the category: %s"%(string))
    return 


def YesNoTrans( string ):
    if   string == 'Yes':    return 1.0
    elif string == 'No':     return 0.0
    elif string == 'Male':   return 0.0
    elif string == 'Female': return 1.0
    elif string == '':       return None
    else:
        exit("Input string is not 'Yes' or 'No': %s"%(string))
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
        exit("Input string is not the given string: %s"%(string))
    return


def DataFillEmpty( data_in, category, DoCopy=False ):
    print('Filling the empty data with None.')
    
    data = copy.deepcopy(data_in) if DoCopy else data_in

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
    else:
        idxs = [i for i in range(len(data))]

    # Select data
    x = np.ones( (len(idxs), len(parameters)) )
    y = np.zeros( len(idxs) )
    for i in range(len(idxs)):
        for j in range(len(parameters)-1):
            temp = data[idxs[i]][parameters[j]]
            if fill and temp == None: temp = fill_num
            x[i, j+1] = temp
        y[i] = data[idxs[i]][parameters[-1]]

    return x, y


def FixAge( data_in, DoCopy=False ):
    print('Fixing the Age category.')
    
    data = copy.deepcopy(data_in) if DoCopy else data_in
    
    for i in range(len(data)):
        if data[i]['Age'] == None: continue

        if data[i]['Age'] < 30:  data[i]['Under 30'] = 1.0
        else:                    data[i]['Under 30'] = 0.0
        
        if data[i]['Age'] >= 65: data[i]['Senior Citizen'] = 1.0
        else:                    data[i]['Senior Citizen'] = 0.0
    return data


def FixDependent( data_in, DoCopy=False ):
    print('Fixing the Dependent category.')
    
    data = copy.deepcopy(data_in) if DoCopy else data_in
    
    for i in range(len(data)):
        if data[i]['Dependents'] == 0.0:  data[i]['Number of Dependents'] = 0.0
        
        if   data[i]['Number of Dependents'] == None: continue
        elif data[i]['Number of Dependents'] == 0.0:  data[i]['Dependents'] = 0.0
        elif data[i]['Number of Dependents'] != 0.0:  data[i]['Dependents'] = 1.0
        
    return data


def FixReferred( data_in, DoCopy=False ):
    print('Fixing the Referred category.')
    
    data = copy.deepcopy(data_in) if DoCopy else data_in
    
    for i in range(len(data)):
        if data[i]['Referred a Friend'] == 0.0:  data[i]['Number of Referrals'] = 0.0
        
        if   data[i]['Number of Referrals'] == None: continue
        elif data[i]['Number of Referrals'] == 0.0:  data[i]['Referred a Friend'] = 0.0
        elif data[i]['Number of Referrals'] != 0.0:  data[i]['Referred a Friend'] = 1.0
    return data
    


def FixLoction( data_in, DoCopy=False ):
    print('Fixing the Location category.')
    
    data = copy.deepcopy(data_in) if DoCopy else data_in
    
    for i in range(len(data)):
        if data[i]['Lat Long'] != None and data[i]['Lat Long'] != '':
            Lat_Long = data[i]['Lat Long'].split(', ')
            data[i]['Latitude']  = float(Lat_Long[0])
            data[i]['Longitude'] = float(Lat_Long[1])
        else:
            if data[i]['Latitude']  == None: continue
            if data[i]['Longitude'] == None: continue
            data[i]['Lat Long'] = str(data[i]['Latitude']) + ', ' + str(data[i]['Longitude'])
    return data


def FixInetrnet( data_in, DoCopy=False ):
    print('Fixing the Internet category.')
    
    data = copy.deepcopy(data_in) if DoCopy else data_in
    
    for i in range(len(data)):
        if   data[i]['Internet Type'] == None: continue
        elif data[i]['Internet Type'] == 0.0:  data[i]['Internet Service'] = 0.0
        elif data[i]['Internet Type'] != 0.0:  data[i]['Internet Service'] = 1.0
    return data


def FixChurn( data_in, learn_type, DoCopy=False ):
    print('Fixing the Internet category.')
    
    data = copy.deepcopy(data_in) if DoCopy else data_in
    
    for i in range(len(data)):
        if learn_type == 0:
            break
        elif learn_type == 1:
            if   data[i]['Churn Category'] == None: continue
            elif data[i]['Churn Category'] == 0.0:  data[i]['Churn Category'] = 0.0
            elif data[i]['Churn Category'] != 0.0:  data[i]['Churn Category'] = 1.0
    return data
