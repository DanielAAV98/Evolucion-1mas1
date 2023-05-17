import numpy as np
import math
from random import random
from random import gauss
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def f(x,y,z):
    f=x+2*y+y*z-x**2-y**2-z**2
    #f = (4-2.1*(x**2)+((x**4)/3))*(x**2)+(x*y)+(-4+4*(y**2))*(y**2)
    #f = x**2+y**2
    return f

# def surface():
#     x = np.arange(-2, 2, 0.01) #variable x
#     y = np.arange(-2, 2, 0.01) #variable y
#     z = np.arange(-2, 2, 0.01) #variable z 
#     #Complete for a matrix named "surf"
#     s = len(x),len(y),len(z)  #tamaño de la matriz
#     surf = np.zeros(s)  #crear superficie (surface) vacía (inicia en ceros) de tamaño s (x,y)
#     for k in range (len(z)):
#         for j in range(len(y)):
#             for i in range(len(x)):
#                 surf[i,j,k] = f(x[i],y[j],z[k])
#     X, Y, K = np.meshgrid(x, y, k) #mesh grid x,y,k
#     #Z = np.array(surf) #matrix (list of lists) to array
# 
#     plt.figure(1)
#     ax = plt.axes(projection = '3d')  #ax definition
#     #Select one of three plot options:
#     ax.contour3D(x,y,surf,50,cmap="plasma")
#     #ax.plot_wireframe(X, Y, Z, color='black')
#     #ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='inferno', edgecolor='none')
#      
#     #labeling
#     ax.set_xlabel("x")
#     ax.set_ylabel("y")
#     ax.set_zlabel('z')
#     #plt.plot(-0.089, 0.71, 'gx')
#     #plt.plot(0.089, -0.71, 'gx')
#     plt.title('Función Objetivo');
 
# def path(u,v):
#     plt.figure(2)
# 
#     plt.plot(u[0], v[0], 'b^')
#     plt.text(u[0], v[0], '(x0,y0)')
#     for i in range(0,len(u)-1):
#         plt.plot([u[i], u[i+1]],[v[i], v[i+1]], 'r+-')
#     plt.plot(u[-1], v[-1], 'bs')
#     plt.text(u[-1], v[-1], '(xf,yf)')
#     plt.plot(-0.089, 0.71, 'gx')
#     plt.plot(0.089, -0.71, 'gx')
#     
#     plt.xlim([-2, 2])
#     plt.ylim([-2, 2])
#     plt.grid()
#     plt.title('Estrategia Evolutiva EE 1+1');
#     
def evol(u,v,w):
    plt.figure(1)
    plt.plot(u)
    plt.plot(v)
    plt.plot(w)
    plt.legend(('x1', 'X2', 'X3'))
    plt.ylim([-2,2])
    plt.show()
    
def mutation(x,s):
    xn = x + s*gauss(0,1)
    while xn < -2 or xn > 2:
        xn = x + s*gauss(0,1)
    return xn

def sigma(s, g, m):
    ps = m/g
    c = 0.817
    if g%20 == 0:
        if ps > 0.2:
            s = s/c	
        elif ps  < 0.2:
            s = s*c
        else:
            s = s
    else:
        s = s
    return s
    
def main():
    #parámetros de simulación
    xmin, xmax, ymin, ymax, zmin, zmax = [-2, 2, -2, 2, -2, 2]
    gmax = 1000
    m = 0
    #individuo inicial
    x = 4*random()+xmin
    y = 4*random()+ymin	
    z = 4*random()+zmin
    x0y0z0 = [round(x,6),round(y,6),round(z,6)]
    print("x0,y0,z0:",x0y0z0)
    #primer padre
    padre = f(x,y,z)
    s = 1
    #registro de individuos
    u = [x]
    v = [y]
    w = [z]
    #ciclo principal
    for g in range(1, gmax):
        s=sigma(s,g,m)
        xn = mutation(x,s)
        yn = mutation(y,s)
        zn = mutation(z,s)
        hijo = f(xn,yn,zn)
        if hijo > padre:
            x = xn
            y = yn
            z = zn
            m += 1
            padre = f(x,y,z)
        else:
            x = x
            y = y
            z = z
            m = m
        u.append(x)
        v.append(y)
        w.append(z)
        
    xfyfzf = [round(x,6),round(y,6), round(z,6)]
    print("xf,yf,zf:",xfyfzf)

#     surface()
#     path(u,v,w)
    evol(u,v,w)

    
main()