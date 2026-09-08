import numpy as np

def calculate(inputlist):
    if len(inputlist) != 9:
        raise ValueError("List must contain nine numbers.")
    new_array = np.array([inputlist[0:3], inputlist[3:6], inputlist[6:9]], dtype=np.float64)
    output_dict = {'mean': [],'variance': [], 'standard deviation': [], 'max': [], 'min': [], 'sum': []}
    output_dict['mean'] = [[float(np.mean())]]
  # return calculations