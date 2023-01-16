import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt

def Qfunc(x):
    return 0.5*mp.erfc(x/mp.sqrt(2))

snrlength = 10
snr_dB = np.linspace(0, 9, 10)
simlen = int(1e5)

err = []
ber = []

mean=0
variance=1

#Noise = np.random.normal(mean, variance, simlen)

for i in range(0, snrlength):
    Noise=np.random.normal(mean,variance,simlen)
    snr = 10**(0.1*snr_dB[i])
    x1 = mp.sqrt(1*snr) + Noise

    err_noise = np.size(np.nonzero(x1 < 0))
    err.append(err_noise/simlen)
    ber.append(Qfunc(mp.sqrt(snr)))

plt.semilogy(snr_dB.T, ber, label = 'Analysis',color='black')
plt.semilogy(snr_dB.T, err, 'o',  label = 'Simulated')
plt.xlabel('SNR $\\left(\\frac{A}{\\sqrt{2}}\\right)$')
#plt.xlabel('SNR$\\left(\\frac{E_b}{N_0}\\right)$')
plt.ylabel('$P_e$')
plt.legend()
plt.grid()
plt.savefig('ber_snr.png')
plt.show()
