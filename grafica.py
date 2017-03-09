import numpy as np
import matplotlib.pyplot as plt

infile = np.genfromtxt("datos.txt")

T = 10000001
x = infile[:,0]
v = infile[:,1]


def trans(x,t):
    a = np.zeros(64)
    a = x[t*64:(t+1)*64]
    return a;

def energia(k,x_n,v_n,t):
    w = 4*(np.sin(k*np.pi/(2*64+2)))**2
    n = (np.pi*k/64)*np.arange(64)
    y = np.sin(n)
    Q =  np.sqrt(2.0/64)*np.dot(trans(x_n,t),y)
    dQ = np.sqrt(2.0/64)*np.dot(trans(v_n,t),y)
    return (1/2.0)*(dQ**2+(w**2)*(Q**2));

z = 100*np.arange(1000) 

fig = plt.figure()
ax = plt.axes()
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("E")

E = np.zeros(1000);
for i in range(0,1000):
    E[i] = energia(1,x,v,i*100)

plt.scatter(z,E,s=2,color= "red",label="k=1")


E = np.zeros(1000);
for i in range(0,1000):
    E[i] = energia(2,x,v,i*100)

plt.scatter(z,E,s=2, color = "blue",label="k=2")

E = np.zeros(1000);
for i in range(0,1000):
    E[i] = energia(3,x,v,i*100)

plt.scatter(z,E,s=2, color = "green",label="k=3")


ax.legend()

filename = 'energia' 
plt.savefig(filename + '.pdf',format = 'pdf')
plt.close()
