import numpy as np
import copy


"""
General Parameter: 
    DoCpoy: If True, copy the input list, but it is time consuming.
"""



def WriteData( file_name, data, y, y_true=None ):
    print( 'Writing the file to %s'%file_name )
    with open( file_name, 'w' ) as f:
        for i in range(len(y)):
            if (y_true != None).all:
                f.write( '%s,%s,%s\n'%(data[i]['Customer ID'], str(int(y[i])), str(int(y_true[i]))) )
            else:
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

Satisfaction Score                : float 1, 2, 3, 4, 5
Quarter                           : All Q3
Referred a Friend                 : No: 0.0, Yes: 1.0
Number of Referrals               : float
Tenure in Months                  : float
Offer                             : None: 0.0, Offer A: 1.0, Offer B: 2.0, Offer C: 3.0, Offer D: 4.0, Offer E: 5.0
Phone Service                     : No: 0.0, Yes: 1.0
Avg Monthly Long Distance Charges : float
Multiple Lines                    : No: 0.0, Yes: 1.0

Internet Service                  : No: 0.0, Yes: 1.0
Internet Type                     : No: 0.0, DSL: 1.0, Fiber Optic: 3.0, Cable: 3.0

Avg Monthly GB Download           : float
Online Security                   : No: 0.0, Yes: 1.0
Online Backup                     : No: 0.0, Yes: 1.0
Device Protection Plan            : No: 0.0, Yes: 1.0
Premium Tech Support              : No: 0.0, Yes: 1.0
Streaming TV                      : No: 0.0, Yes: 1.0
Streaming Movies                  : No: 0.0, Yes: 1.0
Streaming Music                   : No: 0.0, Yes: 1.0

Unlimited Data                    : No: 0.0, Yes: 1.0
Total Extra Data Charges          : float *with the max=150

Contract                          : Month-to-Month: 1.0, One Year: 2.0, Two Year: 3.0
Paperless Billing                 : No: 0.0, Yes: 1.0
Payment Method                    : Bank Withdrawal: 1.0, Credit Card: 2.0, Mailed Chack: 3.0
Monthly Charge                    : float
Total Charges                     : float
Total Refunds                     : float
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
              missing_array : return the same size array as x but with 0 and 1. 1: missing
Output      : 
Description : 
Note        :
'''
def DataSelect( data, parameters, throw=True, fill=False, fill_num=0.0, missing_array=False ):
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
    x    = np.ones( (len(idxs), len(parameters)) )
    miss = np.zeros( (len(idxs), len(parameters)) )
    y    = np.zeros( len(idxs) )
    for i in range(len(idxs)):
        for j in range(len(parameters)-1):
            temp = data[idxs[i]][parameters[j]]
            if fill and temp == None: temp = fill_num
            if missing_array and temp == None: miss[i, j+1] = 1
            x[i, j+1] = temp
        temp = data[idxs[i]][parameters[-1]]
        y[i] = temp if temp != None else 0.0

    if missing_array:  return x, y, miss
    
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


def FixDataUsage( data_in, DoCopy=False ):
    print('Fixing the Data Usage category.')
    
    data = copy.deepcopy(data_in) if DoCopy else data_in
    
    for i in range(len(data)):
        if data[i]['Unlimited Data'] == 1.0:  data[i]['Total Extra Data Charges'] = 0.0
        
        if   data[i]['Total Extra Data Charges'] == None: continue
        elif data[i]['Total Extra Data Charges'] != 0.0:  data[i]['Unlimited Data'] = 0.0
    return data


def FixLongDistanceCharge( data_in, DoCopy=False ):
    print('Fixing the Long Distance Charge and Tenure in Months category.')
    
    data = copy.deepcopy(data_in) if DoCopy else data_in
    
    for i in range(len(data)):
        tot = data[i]['Total Long Distance Charges']
        num = data[i]['Tenure in Months']
        avg = data[i]['Avg Monthly Long Distance Charges']

        if tot == None and num != None and avg != None:
            data[i]['Total Long Distance Charges'] = num * avg
        if tot != None and num != None and avg == None:
            data[i]['Avg Monthly Long Distance Charges'] = tot / num
        if tot != None and num == None and avg != None:
            if avg == 0: continue
            data[i]['Tenure in Months'] = tot / avg
        
    return data


def FixChurn( data_in, learn_type, DoCopy=False ):
    print('Fixing the Churn category.')
    
    data = copy.deepcopy(data_in) if DoCopy else data_in
    
    for i in range(len(data)):
        if learn_type == 0:
            break
        elif learn_type == 1:
            if   data[i]['Churn Category'] == None: continue
            elif data[i]['Churn Category'] == 0.0:  data[i]['Churn Category'] = 0.0
            elif data[i]['Churn Category'] != 0.0:  data[i]['Churn Category'] = 1.0
    return data


"""
Suggest to be the binary or the numerical
"""
def AppdendCategories( data_in, new_categories, values, DoCopy=False ):
    print('Adding new categories: ', new_categories)

    # TODO Check the dimension of values
    
    data = copy.deepcopy(data_in) if DoCopy else data_in

    for i in range(len(data)):
        for j in range(len(new_categories)):
            data[i][new_categories[j]] = values[i][j]
    return data


def DataFilter( data, parameters, DoCopy=False ):
    print('')

    data = copy.deepcopy(data_in) if DoCopy else data_in
    
    return


"""
Use this function after DataFillEmpty
"""
def Category2Binary( data_in, DoCopy=False ):
    print('Transfer category label to multiple binary labels.')

    data = copy.deepcopy(data_in) if DoCopy else data_in

    target = ['Offer', 'Internet Type', 'Contract', 'Payment Method', 'Satisfaction Score'] # 'City' should be one of them.
    target_status = [False for i in range(len(target))] # 'City' should be one of them.
    
    # 1. Check if the label exist.
    for i in range(len(target)):
        if target[i] in data[0]: target_status[i] = True

    # 2. Brake into differnt labels
    for i in range(len(data)):
        if target_status[0]:
            initializer = None if data[i]['Offer'] == None else 0.0
            
            data[i]['Offer None'] = initializer
            data[i]['Offer A']    = initializer
            data[i]['Offer B']    = initializer
            data[i]['Offer C']    = initializer
            data[i]['Offer D']    = initializer
            data[i]['Offer E']    = initializer

            if data[i]['Offer'] == 0.0:  data[i]['Offer None'] = 1.0
            if data[i]['Offer'] == 1.0:  data[i]['Offer A']    = 1.0
            if data[i]['Offer'] == 2.0:  data[i]['Offer B']    = 1.0
            if data[i]['Offer'] == 3.0:  data[i]['Offer C']    = 1.0
            if data[i]['Offer'] == 4.0:  data[i]['Offer D']    = 1.0
            if data[i]['Offer'] == 5.0:  data[i]['Offer E']    = 1.0

        if target_status[1]:
            initializer = None if data[i]['Internet Type'] == None else 0.0
            
            data[i]['Internet None']        = initializer
            data[i]['Internet DSL']         = initializer
            data[i]['Internet Fiber Optic'] = initializer
            data[i]['Internet Cable']       = initializer

            if data[i]['Internet Type'] == 0.0:  data[i]['Internet None']        = 1.0
            if data[i]['Internet Type'] == 1.0:  data[i]['Internet DSL']         = 1.0
            if data[i]['Internet Type'] == 2.0:  data[i]['Internet Fiber Optic'] = 1.0
            if data[i]['Internet Type'] == 3.0:  data[i]['Internet Cable']       = 1.0

        if target_status[2]:
            initializer = None if data[i]['Contract'] == None else 0.0
            
            data[i]['Contract M2M'] = initializer
            data[i]['Contract 1Y']  = initializer
            data[i]['Contract 2Y']  = initializer

            if data[i]['Contract'] == 1.0:  data[i]['Contract M2M'] = 1.0
            if data[i]['Contract'] == 2.0:  data[i]['Contract 1Y']  = 1.0
            if data[i]['Contract'] == 3.0:  data[i]['Contract 2Y']  = 1.0

        if target_status[3]:
            initializer = None if data[i]['Payment Method'] == None else 0.0
            
            data[i]['Payment Bank']   = initializer
            data[i]['Payment Credit'] = initializer
            data[i]['Payment Mailed'] = initializer

            if data[i]['Payment Method'] == 1.0:  data[i]['Payment Bank']   = 1.0
            if data[i]['Payment Method'] == 2.0:  data[i]['Payment Credit'] = 1.0
            if data[i]['Payment Method'] == 3.0:  data[i]['Payment Mailed'] = 1.0
        
        if target_status[4]:
            initializer = None if data[i]['Satisfaction Score'] == None else 0.0
            
            data[i]['Satifaction 1'] = initializer
            data[i]['Satifaction 2'] = initializer
            data[i]['Satifaction 3'] = initializer
            data[i]['Satifaction 4'] = initializer
            data[i]['Satifaction 5'] = initializer

            if data[i]['Satisfaction Score'] == 1.0:  data[i]['Satisfaction 1'] = 1.0
            if data[i]['Satisfaction Score'] == 2.0:  data[i]['Satisfaction 2'] = 1.0
            if data[i]['Satisfaction Score'] == 3.0:  data[i]['Satisfaction 3'] = 1.0
            if data[i]['Satisfaction Score'] == 4.0:  data[i]['Satisfaction 4'] = 1.0
            if data[i]['Satisfaction Score'] == 5.0:  data[i]['Satisfaction 5'] = 1.0

    extra_category = []
    if target_status[0]:
        extra_category.append('Offer None')
        extra_category.append('Offer A')
        extra_category.append('Offer B')
        extra_category.append('Offer C')
        extra_category.append('Offer D')
        extra_category.append('Offer E')
    if target_status[1]:
        extra_category.append('Internet None')
        extra_category.append('Internet DSL')
        extra_category.append('Internet Fiber Optic')
        extra_category.append('Internet Cable')
    if target_status[2]:
        extra_category.append('Contract M2M')
        extra_category.append('Contract 1Y')
        extra_category.append('Contract 2Y')
    if target_status[3]:
        extra_category.append('Payment Bank')
        extra_category.append('Payment Credit')
        extra_category.append('Payment Mailed')
    if target_status[4]:
        extra_category.append('Satisfaction 1')
        extra_category.append('Satisfaction 2')
        extra_category.append('Satisfaction 3')
        extra_category.append('Satisfaction 4')
        extra_category.append('Satisfaction 5')


    return data, extra_category
