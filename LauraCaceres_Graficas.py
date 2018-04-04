import numpy as np
import matplotlib.pyplot as plt
# Carga los datos 
datosP= np.loadtxt('times_python.csv')
datosCPP=np.loadtxt('times_cpp.csb')

dT=datosP[:,0]
dN=datosP[:,1]
ddT=datosCPP[:,0]
ddN=datosCPP[:,1]

#Grafica 
plt.figure()
plt.plot(dN,dT)
plt.plot(ddT,ddN)
plt.legend
plt.xlabel("Datos")
plt.ylabel ("Tiempo")
plt.tittle("Tiempo Vs N")
plt.savefig("cpp_vs_python.png")

