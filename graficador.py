import numpy as np
import matplotlib.pyplot as plt

X1 =np.genfromtxt('datos1.txt', usecols=(0))
V1 =np.genfromtxt('datos1.txt', usecols=(1))

X2 =np.genfromtxt('datos2.txt', usecols=(0))
V2 =np.genfromtxt('datos2.txt', usecols=(1))

X4 =np.genfromtxt('datos4.txt', usecols=(0))
V4 =np.genfromtxt('datos4.txt', usecols=(1))


X1 = X1.reshape((1001,64))
V1 = V1.reshape((1001,64))
X2 = X2.reshape((1001,64))
V2 = V2.reshape((1001,64))
X4 = X4.reshape((1001,64))
V4 = V4.reshape((1001,64))

E11 = np.zeros(1001)
E21 = np.zeros(1001)
E31 = np.zeros(1001)
E12 = np.zeros(1001)
E22 = np.zeros(1001)
E32 = np.zeros(1001)
E14 = np.zeros(1001)
E24 = np.zeros(1001)
E34 = np.zeros(1001)
Times = np.linspace(1,50001,1001)


def energia(k,X,V,t):
    w = 4*(np.sin(k*np.pi/(2*64+2)))**2
    n = (np.pi*k/64)*np.arange(64)
    y = np.sin(n)
    Q =  np.sqrt(2.0/64)*np.dot(X[t],y)
    dQ = np.sqrt(2.0/64)*np.dot(V[t],y)
    return (1.0/2.0)*(dQ**2+(w)*(Q**2));

for i in range(0,999):
	E11[i]=energia(1,X1,V1,i)
	E21[i]=energia(2,X1,V1,i)
	E31[i]=energia(3,X1,V1,i)
	E12[i]=energia(1,X2,V2,i)
	E22[i]=energia(2,X2,V2,i)
	E32[i]=energia(3,X2,V2,i)
	E14[i]=energia(1,X4,V4,i)
	E24[i]=energia(2,X4,V4,i)
	E34[i]=energia(3,X4,V4,i)
plt.subplot(3,1,1)

plt.scatter(Times,E11, color = "blue",label="k=1")
plt.scatter(Times,E21, color = "red",label="k=2")
plt.scatter(Times,E31, color = "black",label="k=3")
plt.title('Numero de procesadores = 1')
plt.ylabel('E_k')
plt.xlabel('tiempo')

plt.subplot(3,1,2)
plt.scatter(Times,E12, color = "blue",label="k=1")
plt.scatter(Times,E22, color = "red",label="k=2")
plt.scatter(Times,E32, color = "black",label="k=3")
plt.title('Numero de procesadores = 2')
plt.ylabel('E_k')
plt.xlabel('tiempo')

plt.subplot(3,1,3)
plt.scatter(Times,E14, color = "blue",label="k=1")
plt.scatter(Times,E24, color = "red",label="k=2")
plt.scatter(Times,E34, color = "black",label="k=3")
plt.title('Numero de procesadores = 4')
plt.ylabel('E_k')
plt.xlabel('tiempo')
plt.show()

filename = 'energia' 
plt.savefig(filename + '.pdf',format = 'pdf')
plt.close()

