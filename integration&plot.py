# nouveau commentaire
#3.2
def diffList(V):
    n=len(V)
    d=[0]*(n-1)
    for i in range(n-1):
        d[i]=V[i+1]-V[i]
    return d
import numpy as np
def diffNp(V):
    n=len(V)
    d=V[1:n]-V[:n-1]
    return d
#V=[3.5,9.5,2.3,6,4.1]
'''import timeit
VL=[np.random.random() for i in range(1000)]
VN=np.random.random(1000)
print(timeit.timeit("diffList(VL)",setup="from__main__import diffList",number=100000))
print(timeit.timeit("diffNp(VN)",setup="from__main__ import diffNp",number=100000))'''
#print(diffList(V))
#print(diffNp(np.array(VN)))
#3.3 representation graphique
import matplotlib.pyplot as plt
plt.title("Fonctions Trigonometriques")
plt.xlabel("X")
plt.xticks([k*np.pi/2 for k in range(5)],['$0$','$\pi/2$','$\pi$','$3\pi/2$','$2\pi$'])
plt.ylabel("Y")
X=np.linspace(0,2*np.pi,100)
#X=np.array([k*np.pi/2 for k in range(5)])
for k in range(1,4):
    plt.plot(X,np.sin(k*X),label="sin(%d x)" %k)
    plt.plot(X,np.cos(k*X),label="cos(%d y)" %k)
plt.legend()
plt.show()
#3.4 indexage de tableaux
M=np.array([0.9602,-0.99,0.2837,0.9602,0.7539,-0.1455,-0.99,-0.9111,0.9602,0.9602,-0.1455,-0.99,0.5403,-0.99,0.9602,0.2837,-0.99,0.2837,0.9602])
cond1=(M<0)
M[cond1]=0
print(M)
m=max(M)
print("max=",m)
cond2=(M==m)
M[cond2==False]=0
M[cond2]=1
print("M=",M)
L=np.array([i+1 for i in range(len(M))])
print("L=",L)
T=(M*L)*0.1
print("T=",T)
cond3=(T!=0)
temps=T[cond3]-0.1
print("temps=",temps)

