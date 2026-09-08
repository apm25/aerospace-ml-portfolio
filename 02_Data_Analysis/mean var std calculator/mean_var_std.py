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

    return {
        'mean': [
            new_array.mean(axis=0).tolist(),
            new_array.mean(axis=1).tolist(),
            new_array.mean().tolist()
        ],
        'variance': [
            new_array.var(axis=0).tolist(),
            new_array.var(axis=1).tolist(),
            new_array.var().tolist()
        ],
        'standard deviation': [
            new_array.std(axis=0).tolist(),
            new_array.std(axis=1).tolist(),
            new_array.std().tolist()
        ],
        'max': [
            new_array.max(axis=0).tolist(),
            new_array.max(axis=1).tolist(),
            new_array.max().tolist()
        ],
        'min': [
            new_array.min(axis=0).tolist(),
            new_array.min(axis=1).tolist(),
            new_array.min().tolist()
        ],
        'sum': [
            new_array.sum(axis=0).tolist(),
            new_array.sum(axis=1).tolist(),
            new_array.sum().item()
        ]
    }
print(calculate([9,1,5,3,3,3,2,9,0]))

