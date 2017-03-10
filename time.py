import numpy as np
import matplotlib.pyplot as plt

t1 =np.genfromtxt('datos1.txt',skip_header=1001, usecols=(0))
t2 =np.genfromtxt('datos2.txt',skip_header=1001, usecols=(0))
t4 =np.genfromtxt('datos4.txt',skip_header=1001, usecols=(0))

t=np.zeros(4)

t[0]=t1[0]
t[1]=t2[0]
t[2]=0
t[3]=t4[0]

x=np.linspace(1,4,4)
plt.scatter(x,t, color = "blue")
plt.ylabel('tiempo')
plt.xlabel('procesadores')
filename = 'Tiempo' 
plt.savefig(filename + '.pdf',format = 'pdf')
plt.close()
