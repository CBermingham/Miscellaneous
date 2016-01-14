import matplotlib.pyplot as plt

time = []
psd = []
fit = []

f = open('psddata', 'rU')
lines=f.readlines()
f.close()
for l in lines:
	b = l.split()
	time.append(float(b[0]))
	psd.append(float(b[1]))
	fit.append(float(b[2]))
#	phase.append(float(b[9]))
#	amplitude.append(float(b[2]))

#phase = [i * 1E9 for i in phase]
#time = [i - time[0] for i in time]

#time2 = []
#phase2 = []
#amp2 = []

#f = open('touch_amp_phase', 'rU')
#lines=f.readlines()
#f.close()
#for l in lines:
#	b = l.split()
#	time2.append(float(b[0]))
#	phase2.append(float(b[1]))
#	amp2.append(float(b[3]))

#amp2 = [5E-4 * i *378 for i in amp2]

#time2 = [i - time2[0] for i in time2]

#f1=plt.figure("Graph")
#plt.plot(time, amplitude, label='Amplitude')
#plt.plot(time, phase, label='Phase')
#plt.xlabel("Time / s", fontsize=18)
#plt.ylabel("Displacement from initial position / nm", fontsize=18)
#plt.legend()
#plt.show()

#fig, ax1 = plt.subplots()
#ax1.plot(time, phase, 'b')
#ax1.set_xlabel('Time / s')
#ax1.set_ylabel('Position / nm (blue)')
#plt.xlim(xmin = 4, xmax = 4.3)

#ax2 = ax1.twinx()
#ax2.plot(time2, phase2, 'r')
#ax2.set_ylabel('sine of oscillation phase (red)')
#plt.xlim(xmin = 4, xmax = 4.3)

#ax3 = ax1.twinx()
#ax2.plot(time2, amp2, 'g', label = 'Amplitude')
#ax2.set_ylabel('Amplitude')
#plt.ylim(ymin = -1, ymax = 1)

plt.scatter(time, psd, color='r', s=1)
plt.plot(time, fit, color='b')
#plt.plot(time, fit)
#plt.plot(time2, amp2)
#plt.plot(time2, phase2)
plt.xlabel("Frequency $\mathit{f}$ (Hz)")
plt.ylabel("PSD of the cantilever (m$^2$/Hz)")
#plt.yscale('log')
plt.xscale('log')
plt.yscale('log')
plt.ylim(ymax=1E-18)
#plt.xlim(xmin = 4.135, xmax = 4.155)
plt.savefig('psd_figure.eps', format='eps')
plt.show()