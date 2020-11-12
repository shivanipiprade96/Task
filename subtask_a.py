#subtask_a
no_of_steps = 0
m = int(input('Enter the starting value : '))
if m>1:
    while not m==1:
        if m % 2 == 0:
            m /= 2
        else:
            m = 3*m + 1
        no_of_steps += 1
else:
    print('Only natural numbers are accepted!')
print('Number of steps : ',no_of_steps)
