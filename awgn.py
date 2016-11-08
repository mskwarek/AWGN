import numpy


with open('dane', 'r') as file:
    signal = list(file.read())
    
noise = numpy.random.normal(0,1,len(signal))
signal_with_noise = []
for i in range(0, len(signal)):
    signal_with_noise.append( float(signal[i]) + noise[i]) 

print "noise:", noise    
print "signal:", signal
print "signal with noise", signal_with_noise
