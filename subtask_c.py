# subtask_c
# Used numpy array to optimise the code
# Overall a task executed in Numpy is around 5 to 100 times faster than
# the standard python list, which is a significant leap in terms of speed

import numpy as np

m_array = np.arange(1, 11)  
for m in m_array:
    no_of_steps = 0
    while not m==1:
        if m % 2 == 0:
            m /= 2
        else:
            m = 3*m + 1
        no_of_steps += 1
    print('Number of steps are : ',no_of_steps)



