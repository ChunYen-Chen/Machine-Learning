import Load
import numpy as np
import matplotlib.pylab as plt

LINE_COLOR = ['black', 'lime', 'red', 'aqua']

def count( data, category, category_type, refer, refer_types, norm=False ):
    counter = np.zeros(len(refer_types))
    
    number = 0
    for i in range(len(data)):
        if type(data[i][refer]) == type(None): continue
        for j in range(len(refer_types)):
            if category_type == 'all':
                number += 1
                if data[i][refer] == refer_types[j]: counter[j] += 1
            elif data[i][category] == category_type:
                number += 1
                if data[i][refer] == refer_types[j]: counter[j] += 1

    if not norm: number = 1
    return counter / number


def anaOffer( data ):
    print('Analysising Offer')
    category = [ 'Gender', 'Under 30', 'Senior Citizen', 'Married', 'Dependents',\
                 'Referred a Friend', 'Phone Service', 'Multiple Lines',\
                 'Internet None', 'Internet DSL', 'Internet Fiber Optic', 'Internet Cable',\
                 'Online Security', 'Online Backup', 'Device Protection Plan',\
                 'Premium Tech Support', 'Streaming TV', 'Streaming Movies', \
                 'Streaming Music', 'Unlimited Data', 'Paperless Billing', 'Payment Bank',\
                 'Contract M2M', 'Contract 1Y', 'Contract 2Y',\
                 'Payment Credit', 'Payment Mailed']
    
    types = ['None', 'A', 'B', 'C', 'D', 'E']
    
    N = len(category)
    Nx = 7 
    Ny = int(N/Nx) + 1
    fig, ax = plt.subplots(Ny, Nx, figsize=(13, 7))
    
    for i in range(len(category)):
        k = int(i/Nx)
        l = i % Nx

        number = count( data, 'Offer', 'all', category[i], [0.0, 1.0], norm=True )
        for j in range(len(number)):
            ax[k, l].axhline( number[j], color=LINE_COLOR[j], alpha=0.5)
        
        for j in range(len(types)):
            number = count( data, 'Offer', j, category[i], [0.0, 1.0], norm=True )
            ax[k, l].scatter( [0, 1], number, s=int(2**(6-j)), label = 'Offer %s'%types[j] )
        
        number = count( data, 'Offer', None, category[i], [0.0, 1.0], norm=True )
        ax[k, l].scatter( [0, 1], number, marker = "X", s=10, color='black', alpha=0.5)
        
        ax[k, l].set(title = category[i])
        ax[k, l].title.set_size(10)
        ax[k, l].set(ylim=[0.0, 1.0])
        ax[k, l].set_xticks([])
        ax[k, l].set_yticks([])
        if i == 1: ax[k, l].legend(loc=0, fontsize=7)
    
    plt.savefig('./figure/offer.png', dpi=200)
    plt.close()
    return

def anaInternet( data ):
    print('Analysising Internet')
    category = [ 'Gender', 'Under 30', 'Senior Citizen', 'Married', 'Dependents',\
                 'Referred a Friend', 'Phone Service', 'Multiple Lines',\
                 'Contract M2M', 'Contract 1Y', 'Contract 2Y',\
                 'Online Security', 'Online Backup', 'Device Protection Plan',\
                 'Premium Tech Support', 'Streaming TV', 'Streaming Movies', \
                 'Streaming Music', 'Unlimited Data', 'Paperless Billing', 'Payment Bank',\
                 'Offer None', 'Offer A', 'Offer B', 'Offer C', 'Offer D', 'Offer E',\
                 'Payment Credit', 'Payment Mailed']
    
    types = ['None', 'DSL', 'Fiber', 'Cable']
    
    N = len(category)
    Nx = 7 
    Ny = int(N/Nx) + 1
    fig, ax = plt.subplots(Ny, Nx, figsize=(13, 7))
    
    for i in range(len(category)):
        k = int(i/Nx)
        l = i % Nx

        number = count( data, 'Internet Type', 'all', category[i], [0.0, 1.0], norm=True )
        for j in range(len(number)):
            ax[k, l].axhline( number[j], color=LINE_COLOR[j], alpha=0.5)
        
        for j in range(len(types)):
            number = count( data, 'Internet Type', j, category[i], [0.0, 1.0], norm=True )
            ax[k, l].scatter( [0, 1], number, s=int(2**(6-j)), label = 'Internet %s'%types[j] )

        number = count( data, 'Internet Type', None, category[i], [0.0, 1.0], norm=True )
        ax[k, l].scatter( [0, 1], number, marker = "X", s=10, color='black', alpha=0.5)
        
        ax[k, l].set(title = category[i])
        ax[k, l].title.set_size(10)
        ax[k, l].set(ylim=[0.0, 1.0])
        ax[k, l].set_xticks([])
        ax[k, l].set_yticks([])
        if i == 1: ax[k, l].legend(loc=0, fontsize=7)
    
    plt.savefig('./figure/internet.png', dpi=200)
    plt.close()
    return

def anaPayment( data ):
    print('Analysising Payment')
    category = [ 'Gender', 'Under 30', 'Senior Citizen', 'Married', 'Dependents',\
                 'Referred a Friend', 'Phone Service', 'Multiple Lines',\
                 'Contract M2M', 'Contract 1Y', 'Contract 2Y',\
                 'Internet None', 'Internet DSL', 'Internet Fiber Optic', 'Internet Cable',\
                 'Online Security', 'Online Backup', 'Device Protection Plan',\
                 'Premium Tech Support', 'Streaming TV', 'Streaming Movies', \
                 'Streaming Music', 'Unlimited Data', 'Paperless Billing',\
                 'Offer None', 'Offer A', 'Offer B', 'Offer C', 'Offer D', 'Offer E',\
                 ]
    
    types = ['Bank', 'Credit', 'Mailed']
    
    N = len(category)
    Nx = 7 
    Ny = int(N/Nx) + 1
    fig, ax = plt.subplots(Ny, Nx, figsize=(13, 7))
    
    for i in range(len(category)):
        k = int(i/Nx)
        l = i % Nx

        number = count( data, 'Payment Method', 'all', category[i], [0.0, 1.0], norm=True )
        for j in range(len(number)):
            ax[k, l].axhline( number[j], color=LINE_COLOR[j], alpha=0.5)
        
        for j in range(len(types)):
            number = count( data, 'Payment Method', j+1, category[i], [0.0, 1.0], norm=True )
            ax[k, l].scatter( [0, 1], number, s=int(2**(6-j)), label = 'Payment %s'%types[j] )

        number = count( data, 'Payment Method', None, category[i], [0.0, 1.0], norm=True )
        ax[k, l].scatter( [0, 1], number, marker = "X", s=10, color='black', alpha=0.5)
        
        ax[k, l].set(title = category[i])
        ax[k, l].title.set_size(10)
        ax[k, l].set(ylim=[0.0, 1.0])
        ax[k, l].set_xticks([])
        ax[k, l].set_yticks([])
        if i == 1: ax[k, l].legend(loc=0, fontsize=7)
    
    plt.savefig('./figure/payment.png', dpi=200)
    plt.close()
    return


def anaContract( data ):
    print('Analysising Contract')
    category = [ 'Gender', 'Under 30', 'Senior Citizen', 'Married', 'Dependents',\
                 'Referred a Friend', 'Phone Service', 'Multiple Lines',\
                 'Internet None', 'Internet DSL', 'Internet Fiber Optic', 'Internet Cable',\
                 'Online Security', 'Online Backup', 'Device Protection Plan',\
                 'Premium Tech Support', 'Streaming TV', 'Streaming Movies', \
                 'Streaming Music', 'Unlimited Data', 'Paperless Billing', 'Payment Bank',\
                 'Offer None', 'Offer A', 'Offer B', 'Offer C', 'Offer D', 'Offer E',\
                 'Payment Credit', 'Payment Mailed']
    
    types = ['M2M', '1Y', '2Y']
    
    N = len(category)
    Nx = 7 
    Ny = int(N/Nx) + 1
    fig, ax = plt.subplots(Ny, Nx, figsize=(13, 7))
    
    for i in range(len(category)):
        k = int(i/Nx)
        l = i % Nx

        number = count( data, 'Contract', 'all', category[i], [0.0, 1.0], norm=True )
        for j in range(len(number)):
            ax[k, l].axhline( number[j], color=LINE_COLOR[j], alpha=0.5)
        
        for j in range(len(types)):
            number = count( data, 'Contract', j+1, category[i], [0.0, 1.0], norm=True )
            ax[k, l].scatter( [0, 1], number, s=int(2**(6-j)), label = 'Contract %s'%types[j] )

        number = count( data, 'Contract', None, category[i], [0.0, 1.0], norm=True )
        ax[k, l].scatter( [0, 1], number, marker = "X", s=10, color='black', alpha=0.5)
        
        ax[k, l].set(title = category[i])
        ax[k, l].title.set_size(10)
        ax[k, l].set(ylim=[0.0, 1.0])
        ax[k, l].set_xticks([])
        ax[k, l].set_yticks([])
        if i == 1: ax[k, l].legend(loc=0, fontsize=7)
    
    plt.savefig('./figure/contract.png', dpi=200)
    plt.close()
    return

def anaTerune( data ):
    print('Analysising Tenure')
    category = [ 'Gender', 'Under 30', 'Senior Citizen', 'Married', 'Dependents',\
                 'Referred a Friend', 'Phone Service', 'Multiple Lines',\
                 'Internet None', 'Internet DSL', 'Internet Fiber Optic', 'Internet Cable',\
                 'Online Security', 'Online Backup', 'Device Protection Plan',\
                 'Premium Tech Support', 'Streaming TV', 'Streaming Movies', \
                 'Streaming Music', 'Unlimited Data', 'Paperless Billing', 'Payment Bank',\
                 'Contract M2M', 'Contract 1Y', 'Contract 2Y',\
                 'Offer None', 'Offer A', 'Offer B', 'Offer C', 'Offer D', 'Offer E',\
                 'Payment Credit', 'Payment Mailed']
    
    types = ['1', '2', '3', '4', '5']
    
    N = len(category)
    Nx = 7 
    Ny = int(N/Nx) + 1
    fig, ax = plt.subplots(Ny, Nx, figsize=(13, 7))
    
    for i in range(len(category)):
        k = int(i/Nx)
        l = i % Nx

        number = count( data, 'Tenure', 'all', category[i], [0.0, 1.0], norm=True )
        for j in range(len(number)):
            ax[k, l].axhline( number[j], color=LINE_COLOR[j], alpha=0.5)
        
        for j in range(len(types)):
            number = count( data, 'Tenure', j+1, category[i], [0.0, 1.0], norm=True )
            ax[k, l].scatter( [0, 1], number, s=int(2**(6-j)), label = 'Tenure %s'%types[j] )

        number = count( data, 'Tenure', None, category[i], [0.0, 1.0], norm=True )
        ax[k, l].scatter( [0, 1], number, marker = "X", s=10, color='black', alpha=0.5)
        
        ax[k, l].set(title = category[i])
        ax[k, l].title.set_size(10)
        ax[k, l].set(ylim=[0.0, 1.0])
        ax[k, l].set_xticks([])
        ax[k, l].set_yticks([])
        if i == 1: ax[k, l].legend(loc=0, fontsize=7)
    
    plt.savefig('./figure/tenure.png', dpi=200)
    plt.close()
    return


def anaTerune1( data ):
    print('Analysising Tenure 1')
    category = [ 'Gender', 'Under 30', 'Senior Citizen', 'Married', 'Dependents',\
                 'Referred a Friend', 'Phone Service', 'Multiple Lines',\
                 'Internet None', 'Internet DSL', 'Internet Fiber Optic', 'Internet Cable',\
                 'Online Security', 'Online Backup', 'Device Protection Plan',\
                 'Premium Tech Support', 'Streaming TV', 'Streaming Movies', \
                 'Streaming Music', 'Unlimited Data', 'Paperless Billing', 'Payment Bank',\
                 'Contract M2M', 'Contract 1Y', 'Contract 2Y',\
                 'Payment Credit', 'Payment Mailed']
    
    data_new = Load.DataFilter( data, 'Tenure 1', [1] )
    offer = [0., 1.]
    types = ['None', 'A']
    
    N = len(category)
    Nx = 7 
    Ny = int(N/Nx) + 1
    fig, ax = plt.subplots(Ny, Nx, figsize=(13, 7))
    
    for i in range(len(category)):
        k = int(i/Nx)
        l = i % Nx

        number = count( data_new, 'Offer', 'all', category[i], [0.0, 1.0], norm=True )
        for j in range(len(number)):
            ax[k, l].axhline( number[j], color=LINE_COLOR[j], alpha=0.5)
        
        for j in range(len(types)):
            number = count( data_new, 'Offer', offer[j], category[i], [0.0, 1.0], norm=True )
            ax[k, l].scatter( [0, 1], number, s=int(2**(6-j)), label = 'Offer %s'%types[j] )

        number = count( data_new, 'Offer', None, category[i], [0.0, 1.0], norm=True )
        ax[k, l].scatter( [0, 1], number, marker = "X", s=10, color='black', alpha=0.5)
        
        ax[k, l].set(title = category[i])
        ax[k, l].title.set_size(10)
        ax[k, l].set(ylim=[0.0, 1.0])
        ax[k, l].set_xticks([])
        ax[k, l].set_yticks([])
        if i == 1: ax[k, l].legend(loc=0, fontsize=7)
    
    plt.savefig('./figure/tenure_1.png', dpi=200)
    plt.close()
    return

def anaTerune2( data ):
    print('Analysising Tenure 2')
    category = [ 'Gender', 'Under 30', 'Senior Citizen', 'Married', 'Dependents',\
                 'Referred a Friend', 'Phone Service', 'Multiple Lines',\
                 'Internet None', 'Internet DSL', 'Internet Fiber Optic', 'Internet Cable',\
                 'Online Security', 'Online Backup', 'Device Protection Plan',\
                 'Premium Tech Support', 'Streaming TV', 'Streaming Movies', \
                 'Streaming Music', 'Unlimited Data', 'Paperless Billing', 'Payment Bank',\
                 'Contract M2M', 'Contract 1Y', 'Contract 2Y',\
                 'Payment Credit', 'Payment Mailed']
    
    data_new = Load.DataFilter( data, 'Tenure 2', [1] )
    offer = [0., 2.]
    types = ['None', 'B']
    
    N = len(category)
    Nx = 7 
    Ny = int(N/Nx) + 1
    fig, ax = plt.subplots(Ny, Nx, figsize=(13, 7))
    
    for i in range(len(category)):
        k = int(i/Nx)
        l = i % Nx

        number = count( data_new, 'Offer', 'all', category[i], [0.0, 1.0], norm=True )
        for j in range(len(number)):
            ax[k, l].axhline( number[j], color=LINE_COLOR[j], alpha=0.5)
        
        for j in range(len(types)):
            number = count( data_new, 'Offer', offer[j], category[i], [0.0, 1.0], norm=True )
            ax[k, l].scatter( [0, 1], number, s=int(2**(6-j)), label = 'Offer %s'%types[j] )

        number = count( data_new, 'Offer', None, category[i], [0.0, 1.0], norm=True )
        ax[k, l].scatter( [0, 1], number, marker = "X", s=10, color='black', alpha=0.5)
        
        ax[k, l].set(title = category[i])
        ax[k, l].title.set_size(10)
        ax[k, l].set(ylim=[0.0, 1.0])
        ax[k, l].set_xticks([])
        ax[k, l].set_yticks([])
        if i == 1: ax[k, l].legend(loc=0, fontsize=7)
    
    plt.savefig('./figure/tenure_2.png', dpi=200)
    plt.close()
    return


def anaTerune3( data ):
    print('Analysising Tenure 3')
    category = [ 'Gender', 'Under 30', 'Senior Citizen', 'Married', 'Dependents',\
                 'Referred a Friend', 'Phone Service', 'Multiple Lines',\
                 'Internet None', 'Internet DSL', 'Internet Fiber Optic', 'Internet Cable',\
                 'Online Security', 'Online Backup', 'Device Protection Plan',\
                 'Premium Tech Support', 'Streaming TV', 'Streaming Movies', \
                 'Streaming Music', 'Unlimited Data', 'Paperless Billing', 'Payment Bank',\
                 'Contract M2M', 'Contract 1Y', 'Contract 2Y',\
                 'Payment Credit', 'Payment Mailed']
    
    data_new = Load.DataFilter( data, 'Tenure 3', [1] )
    offer = [0., 3.]
    types = ['None', 'C']
    
    N = len(category)
    Nx = 7 
    Ny = int(N/Nx) + 1
    fig, ax = plt.subplots(Ny, Nx, figsize=(13, 7))
    
    for i in range(len(category)):
        k = int(i/Nx)
        l = i % Nx

        number = count( data_new, 'Offer', 'all', category[i], [0.0, 1.0], norm=True )
        for j in range(len(number)):
            ax[k, l].axhline( number[j], color=LINE_COLOR[j], alpha=0.5)
        
        for j in range(len(types)):
            number = count( data_new, 'Offer', offer[j], category[i], [0.0, 1.0], norm=True )
            ax[k, l].scatter( [0, 1], number, s=int(2**(6-j)), label = 'Offer %s'%types[j] )

        number = count( data_new, 'Offer', None, category[i], [0.0, 1.0], norm=True )
        ax[k, l].scatter( [0, 1], number, marker = "X", s=10, color='black', alpha=0.5)
        
        ax[k, l].set(title = category[i])
        ax[k, l].title.set_size(10)
        ax[k, l].set(ylim=[0.0, 1.0])
        ax[k, l].set_xticks([])
        ax[k, l].set_yticks([])
        if i == 1: ax[k, l].legend(loc=0, fontsize=7)
    
    plt.savefig('./figure/tenure_3.png', dpi=200)
    plt.close()
    return

def anaTerune4( data ):
    print('Analysising Tenure 4')
    category = [ 'Gender', 'Under 30', 'Senior Citizen', 'Married', 'Dependents',\
                 'Referred a Friend', 'Phone Service', 'Multiple Lines',\
                 'Internet None', 'Internet DSL', 'Internet Fiber Optic', 'Internet Cable',\
                 'Online Security', 'Online Backup', 'Device Protection Plan',\
                 'Premium Tech Support', 'Streaming TV', 'Streaming Movies', \
                 'Streaming Music', 'Unlimited Data', 'Paperless Billing', 'Payment Bank',\
                 'Contract M2M', 'Contract 1Y', 'Contract 2Y',\
                 'Payment Credit', 'Payment Mailed']
    
    data_new = Load.DataFilter( data, 'Tenure 4', [1] )
    offer = [0., 4.]
    types = ['None', 'C']
    
    N = len(category)
    Nx = 7 
    Ny = int(N/Nx) + 1
    fig, ax = plt.subplots(Ny, Nx, figsize=(13, 7))
    
    for i in range(len(category)):
        k = int(i/Nx)
        l = i % Nx

        number = count( data_new, 'Offer', 'all', category[i], [0.0, 1.0], norm=True )
        for j in range(len(number)):
            ax[k, l].axhline( number[j], color=LINE_COLOR[j], alpha=0.5)
        
        for j in range(len(types)):
            number = count( data_new, 'Offer', offer[j], category[i], [0.0, 1.0], norm=True )
            ax[k, l].scatter( [0, 1], number, s=int(2**(6-j)), label = 'Offer %s'%types[j] )

        number = count( data_new, 'Offer', None, category[i], [0.0, 1.0], norm=True )
        ax[k, l].scatter( [0, 1], number, marker = "X", s=10, color='black', alpha=0.5)
        
        ax[k, l].set(title = category[i])
        ax[k, l].title.set_size(10)
        ax[k, l].set(ylim=[0.0, 1.0])
        ax[k, l].set_xticks([])
        ax[k, l].set_yticks([])
        if i == 1: ax[k, l].legend(loc=0, fontsize=7)
    
    plt.savefig('./figure/tenure_4.png', dpi=200)
    plt.close()
    return

def anaTerune5( data ):
    print('Analysising Tenure 5')
    category = [ 'Gender', 'Under 30', 'Senior Citizen', 'Married', 'Dependents',\
                 'Referred a Friend', 'Phone Service', 'Multiple Lines',\
                 'Internet None', 'Internet DSL', 'Internet Fiber Optic', 'Internet Cable',\
                 'Online Security', 'Online Backup', 'Device Protection Plan',\
                 'Premium Tech Support', 'Streaming TV', 'Streaming Movies', \
                 'Streaming Music', 'Unlimited Data', 'Paperless Billing', 'Payment Bank',\
                 'Contract M2M', 'Contract 1Y', 'Contract 2Y',\
                 'Payment Credit', 'Payment Mailed']
    
    data_new = Load.DataFilter( data, 'Tenure 5', [1] )
    offer = [0., 5.]
    types = ['None', 'E']
    
    N = len(category)
    Nx = 7 
    Ny = int(N/Nx) + 1
    fig, ax = plt.subplots(Ny, Nx, figsize=(13, 7))
    
    for i in range(len(category)):
        k = int(i/Nx)
        l = i % Nx

        number = count( data_new, 'Offer', 'all', category[i], [0.0, 1.0], norm=True )
        for j in range(len(number)):
            ax[k, l].axhline( number[j], color=LINE_COLOR[j], alpha=0.5)
        
        for j in range(len(types)):
            number = count( data_new, 'Offer', offer[j], category[i], [0.0, 1.0], norm=True )
            ax[k, l].scatter( [0, 1], number, s=int(2**(6-j)), label = 'Offer %s'%types[j] )

        number = count( data_new, 'Offer', None, category[i], [0.0, 1.0], norm=True )
        ax[k, l].scatter( [0, 1], number, marker = "X", s=10, color='black', alpha=0.5)
        
        ax[k, l].set(title = category[i])
        ax[k, l].title.set_size(10)
        ax[k, l].set(ylim=[0.0, 1.0])
        ax[k, l].set_xticks([])
        ax[k, l].set_yticks([])
        if i == 1: ax[k, l].legend(loc=0, fontsize=7)
    
    plt.savefig('./figure/tenure_5.png', dpi=200)
    plt.close()
    return


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

    # all total charge fixed
    data_train = Load.FixTotal( data_train )
    data_test  = Load.FixTotal( data_test  )

    # since the total value has been updated we can filled some blank back
    data_train = Load.FixLongDistanceCharge( data_train )
    data_test  = Load.FixLongDistanceCharge( data_test  )
    
    data_train = Load.FixDataUsage( data_train )
    data_test  = Load.FixDataUsage( data_test  )

    data_train, extra_category1 = Load.Numeric2Category( data_train )
    data_test,  extra_category1 = Load.Numeric2Category( data_test  )

    # separate the category label to binary label
    data_train, extra_category = Load.Category2Binary( data_train )
    data_test,  extra_category = Load.Category2Binary( data_test  )

    # Churn or not
    data_train = Load.FixChurn( data_train, learn_type, DoCopy=True )
    data_test  = Load.FixChurn( data_test,  learn_type, DoCopy=True )

    data_train = data_train + data_test 

    # Analysis offer
    anaOffer( data_train )
    anaContract( data_train )
    anaInternet( data_train )
    anaPayment( data_train )
    anaTerune( data_train )
    anaTerune1( data_train )
    anaTerune2( data_train )
    anaTerune3( data_train )
    anaTerune4( data_train )
    anaTerune5( data_train )
