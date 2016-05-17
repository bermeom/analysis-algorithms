
import numpy as np
import matplotlib.pyplot as plt 
from scipy import integrate
import math
import random

# Define logarithmic likelihood function.
# params ... array of fit params, here just alpha
# D      ... sum over log(M_n)
# N      ... number of data points.
# M_min  ... lower limit of mass interval
# M_max  ... upper limit of mass interval
def evaluateLogLikelihood(params, D, N, M_min, M_max):
    alpha = params[0]  # extract alpha
    # Compute normalisation constant.
    c = (1.0 - alpha)/(math.pow(M_max, 1.0-alpha)
                        - math.pow(M_min, 1.0-alpha))
    # return log likelihood.
    return N*math.log(c) - alpha*D

# Generate toy data.
N      = 1000000  # Draw 1 Million stellar masses.
alpha  = 2.35
M_min  = 1.0
M_max  = 100.0
supernova= np.genfromtxt("SCPUnion2.1_mu_vs_z.txt");
Masses = supernova[:,2];#sampleFromSalpeter(N, alpha, M_min, M_max)
LogM   = np.log(np.array(Masses))
D      = np.mean(LogM)*N

# initial guess for alpha as array.
guess = [3.0]
# Prepare storing MCMC chain as array of arrays.
A = [guess]
# define stepsize of MCMC.
stepsizes = [0.005]  # array of stepsizes
accepted  = 0.0

# Metropolis-Hastings with 10,000 iterations.
for n in range(10000):
    old_alpha  = A[len(A)-1]  # old parameter value as array
    old_loglik = evaluateLogLikelihood(old_alpha, D, N, M_min,
                    M_max)
    # Suggest new candidate from Gaussian proposal distribution.
    new_alpha = np.zeros([len(old_alpha)])
    for i in range(len(old_alpha)):
        # Use stepsize provided for every dimension.
        new_alpha[i] = random.gauss(old_alpha[i], stepsizes[i])
    new_loglik = evaluateLogLikelihood(new_alpha, D, N, M_min,
                    M_max)
    # Accept new candidate in Monte-Carlo fashing.
    if (new_loglik > old_loglik):
        A.append(new_alpha)
        accepted = accepted + 1.0  # monitor acceptance
    else:
        u = random.uniform(0.0,1.0)
        if (u < math.exp(new_loglik - old_loglik)):
            A.append(new_alpha)
            accepted = accepted + 1.0  # monitor acceptance
        else:
            A.append(old_alpha)

print "Acceptance rate = "+str(accepted/10000.0)

# Discard first half of MCMC chain and thin out the rest.
Clean = []
for n in range(5000,10000):
    if (n % 10 == 0):
        Clean.append(A[n][0])

# Print Monte-Carlo estimate of alpha.
print "Mean:  "+str(np.mean(Clean))
print "Sigma: "+str(np.std(Clean))

plt.figure(1)
plt.hist(Clean, 20, histtype='step', lw=3)
plt.xticks([2.346,2.348,2.35,2.352,2.354],
           [2.346,2.348,2.35,2.352,2.354])
plt.xlim(2.345,2.355)
plt.xlabel(r'$\alpha$', fontsize=24)
plt.ylabel(r'$\cal L($Data$;\alpha)$', fontsize=24)
plt.savefig('example-MCMC-results.png')
plt.show()