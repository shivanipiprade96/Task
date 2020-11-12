#subtask_b

m_list = range(1,10001)  # m belongs to list of natural numbers from 1 to 10000
for m in m_list:
    no_of_steps = 0
    while not m==1:
        if m % 2 == 0:
            m /= 2
        else:
            m = 3*m + 1
        no_of_steps += 1
    print('Number of steps are : ',no_of_steps)

