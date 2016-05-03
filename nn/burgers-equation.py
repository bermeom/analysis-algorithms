from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import pyplot
import numpy

def print_matrix( matrix ):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print '\n'.join(table)

nx = 8
ny = 8
nt = 120
c = 1
dx = 2/float(nx-1)
dy = 2/float(ny-1)
sigma = .0009
nu = 0.01
dt = sigma*dx*dy/float(nu)


x = numpy.linspace(0,2,nx)
y = numpy.linspace(0,2,ny)


u = numpy.ones((ny,nx)) ##create a 1xn vector of 1's
v = numpy.ones((ny,nx))
un = numpy.ones((ny,nx)) ##
vn = numpy.ones((ny,nx))
comb = numpy.ones((ny,nx))

u[.5/dy:1/dy+1,.5/dx:1/dx+1]=2 ##set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2
v[.5/dy:1/dy+1,.5/dx:1/dx+1]=2 ##set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2

#print_matrix(v)
for n in range(nt+1): ##loop across number of time steps
    un = u.copy()
    vn = v.copy()
    
    u[1:-1,1:-1] = un[1:-1,1:-1] - dt/dx*un[1:-1,1:-1]*(un[1:-1,1:-1]-un[1:-1,0:-2])-dt/dy*vn[1:-1,1:-1]* \
                   (un[1:-1,1:-1]-un[0:-2,1:-1])+nu*dt/dx*2*(un[1:-1,2:]-2*un[1:-1,1:-1]+un[1:-1,0:-2])+ \
                   nu*dt/dy*2*(un[2:,1:-1]-2*un[1:-1,1:-1]+un[0:-2,1:-1])
    
    v[1:-1,1:-1] = vn[1:-1,1:-1] - dt/dx*un[1:-1,1:-1]*(vn[1:-1,1:-1]-vn[1:-1,0:-2])-dt/dy*vn[1:-1,1:-1]* \
                   (vn[1:-1,1:-1]-vn[0:-2,1:-1])+nu*dt/dx*2*(vn[1:-1,2:]-2*vn[1:-1,1:-1]+vn[1:-1,0:-2])+ \
                   nu*dt/dy*2*(vn[2:,1:-1]-2*vn[1:-1,1:-1]+vn[0:-2,1:-1])
     
    u[0,:] = 1
    u[-1,:] = 1
    u[:,0] = 1
    u[:,-1] = 1
    
    v[0,:] = 1
    v[-1,:] = 1
    v[:,0] = 1
    v[:,-1] = 1
 
print_matrix(u)