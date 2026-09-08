import numpy as np

def calculate(inputlist):
    if len(inputlist) != 9:
        raise ValueError("List must contain nine numbers.")
    new_array = np.array([inputlist[0:3], inputlist[3:6], inputlist[6:9]], dtype=np.float64)
    output_dict = {'mean': [],'variance': [], 'standard deviation': [], 'max': [], 'min': [], 'sum': []}
    for i in range(3):
        meanlist = []
        varlist = []
        sdlist = []
        maxlist = []
        minlist = []
        sumlist = []
        if i == 0:
            meanlist.append([float(np.mean(new_array[0])),float(np.mean(new_array[1])),float(np.mean(new_array[2]))])
            varlist.append([float(np.var(new_array[0])),float(np.var(new_array[1])),float(np.var(new_array[2]))])
            sdlist.append([float(np.std(new_array[0])),float(np.std(new_array[1])),float(np.std(new_array[2]))])
            maxlist.append([int(np.max(new_array[0])),int(np.max(new_array[1])),int(np.max(new_array[2]))])
            minlist.append([int(np.min(new_array[0])),int(np.min(new_array[1])),int(np.min(new_array[2]))])
            sumlist.append([int(np.sum(new_array[0])),int(np.sum(new_array[1])),int(np.sum(new_array[2]))])
        if i== 1:
            meanlist.append([float(np.mean(new_array[:,0])),float(np.mean(new_array[:,1])),float(np.mean(new_array[:,2]))])
            varlist.append([float(np.var(new_array[:,0])),float(np.var(new_array[:,1])),float(np.var(new_array[:,2]))])
            sdlist.append([float(np.std(new_array[:,0])),float(np.std(new_array[:,1])),float(np.std(new_array[:,2]))])
            maxlist.append([int(np.max(new_array[:,0])),int(np.max(new_array[:,1])),int(np.max(new_array[:,2]))])
            minlist.append([int(np.min(new_array[:,0])),int(np.min(new_array[:,1])),int(np.min(new_array[:,2]))])
            sumlist.append([int(np.sum(new_array[:,0])),int(np.sum(new_array[:,1])),int(np.sum(new_array[:,2]))])
        if i==2:
            meanlist = float(np.mean(new_array.flatten()))
            varlist = float(np.var(new_array.flatten()))
            sdlist = float(np.std(new_array.flatten()))
            maxlist = int(np.max(new_array.flatten()))
            minlist = int(np.min(new_array.flatten()))
            sumlist = int(np.sum(new_array.flatten()))
        output_dict['mean'].append(meanlist)
        output_dict['variance'].append(varlist)
        output_dict['standard deviation'].append(sdlist)
        output_dict['max'].append(maxlist)
        output_dict['min'].append(minlist)
        output_dict['sum'].append(sumlist)

                
  # return calculations
    return output_dict
print(calculate([0,1,2,3,4,5,6,7,8]))
