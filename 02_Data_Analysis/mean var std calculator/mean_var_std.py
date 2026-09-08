import numpy as np

def calculate(inputlist):

    #Raise ValueError if input list length is < 9
    if len(inputlist) != 9:
        raise ValueError("List must contain nine numbers.")
    
    #Organise input list into NumPy array
    new_array = np.array([inputlist[0:3], inputlist[3:6], inputlist[6:9]], dtype=np.float64)

    #Initialise output dictionary
    output_dict = {'mean': [],'variance': [], 'standard deviation': [], 'max': [], 'min': [], 'sum': []}

    #Initialise for loop for 3 cases
    for i in range(3):

        #Initialise lists of each operation
        meanlist = []
        varlist = []
        sdlist = []
        maxlist = []
        minlist = []
        sumlist = []

        #Rows logic
        if i == 0:
            meanlist.append([float(np.mean(new_array[0])),float(np.mean(new_array[1])),float(np.mean(new_array[2]))])
            varlist.append([float(np.var(new_array[0])),float(np.var(new_array[1])),float(np.var(new_array[2]))])
            sdlist.append([float(np.std(new_array[0])),float(np.std(new_array[1])),float(np.std(new_array[2]))])
            maxlist.append([int(np.max(new_array[0])),int(np.max(new_array[1])),int(np.max(new_array[2]))])
            minlist.append([int(np.min(new_array[0])),int(np.min(new_array[1])),int(np.min(new_array[2]))])
            sumlist.append([int(np.sum(new_array[0])),int(np.sum(new_array[1])),int(np.sum(new_array[2]))])

        #Columns logic
        if i== 1:
            meanlist.append([float(np.mean(new_array[:,0])),float(np.mean(new_array[:,1])),float(np.mean(new_array[:,2]))])
            varlist.append([float(np.var(new_array[:,0])),float(np.var(new_array[:,1])),float(np.var(new_array[:,2]))])
            sdlist.append([float(np.std(new_array[:,0])),float(np.std(new_array[:,1])),float(np.std(new_array[:,2]))])
            maxlist.append([int(np.max(new_array[:,0])),int(np.max(new_array[:,1])),int(np.max(new_array[:,2]))])
            minlist.append([int(np.min(new_array[:,0])),int(np.min(new_array[:,1])),int(np.min(new_array[:,2]))])
            sumlist.append([int(np.sum(new_array[:,0])),int(np.sum(new_array[:,1])),int(np.sum(new_array[:,2]))])

        #Flattened array logic
        if i==2:
            meanlist = float(np.mean(new_array.flatten()))
            varlist = float(np.var(new_array.flatten()))
            sdlist = float(np.std(new_array.flatten()))
            maxlist = int(np.max(new_array.flatten()))
            minlist = int(np.min(new_array.flatten()))
            sumlist = int(np.sum(new_array.flatten()))

        #Append complete item lists to output dictionary
        output_dict['mean'].append(meanlist)
        output_dict['variance'].append(varlist)
        output_dict['standard deviation'].append(sdlist)
        output_dict['max'].append(maxlist)
        output_dict['min'].append(minlist)
        output_dict['sum'].append(sumlist)

                
  # return calculations
    return output_dict
