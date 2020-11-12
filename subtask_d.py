#subtask_d
import numpy as np
import matplotlib.pyplot as plt
m_array = np.arange(1, 10001)
steps = np.array([])
for m in m_array:
    no_of_steps = 0
    while not m==1:
        if m % 2 == 0:
            m /= 2
        else:
            m = 3*m + 1
        no_of_steps += 1
    steps=np.append(steps,no_of_steps)
plt.xlabel("Starting Value (m)",fontsize=11)
plt.ylabel("No. of Steps until first occurence of 1")
plt.title("Interview Task Diagram")
plt.plot(m_array,steps,'o',color="blue", ms=.5, mec="red",mew=0.0)
plt.xlim(xmax=10000)
plt.ylim(ymin=0)
plt.show()
