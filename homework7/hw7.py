
import numpy as np
import matplotlib.pyplot as plt 
from scipy import integrate
import math

def print_matrix( matrix ):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print '\n'.join(table)

def DL(z,H0,dm,c):
    def func(z,dm):
        return 1/math.sqrt(dm*(1+z)**3+(1-dm))
    z1,erro=integrate.quad(func,0,z,args=float(dm))
    dis=float((1+float(z))*(float(c)/float(H0))*(float(z1)));
    return float(dis)

def modist(z,H0,dm,c):
    return float(float(5.0*math.log10(DL(z,H0,dm,c)))-float(5));

def chi_squared(H0,dm):
    suma =0
    for i in range (len(redshift)):
        suma+=float((modist(float(redshift[i]),float(H0),float(dm),float(3*(10**8)))-float(modisi[i])**2))/float(error_magaparente[i]**2);
    
    return suma;
    
def metropolis_hastings(H0,dm):
    return (np.exp((-(chi_squared(H0,dm)))/(2.0)));
    
    
supernova= np.genfromtxt("SCPUnion2.1_mu_vs_z.txt");
id_supernova=supernova[:,0];
redshift=supernova[:,1]#z
magaparente=supernova[:,2]#
error_magaparente=supernova[:,3]

M=-19.3;
H0=67.8*(10**3);#Hubble constant, H0= (67.8 +/- 0.9) km/s/Mpc
Omega_m=0.308;#Omega_m = 0.308 +/- 0.012 
modisi=[];
for i in range (len(magaparente)):
    modisi.append(magaparente[i]-M);
    #print magaparente[i]-M;
    
print metropolis_hastings(H0,Omega_m);