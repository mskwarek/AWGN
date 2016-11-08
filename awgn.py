import numpy

def read_signal_data(filename):
    with open(filename, 'r') as fi:
        return list(fi.read())

def generate_noise(length):
    return numpy.random.normal(0,1,length)

def add_noise_to_signal(signal, noise):
    signal_with_noise = []
    for i in range(0, len(signal)):
        signal_with_noise.append( float(signal[i]) + noise[i]) 
    return signal_with_noise

if __name__=='__main__':
    signal = read_signal_data('dane')
    noise = generate_noise(len(signal))
    signal_with_noise = add_noise_to_signal(signal, noise)
    print "noise:", noise    
    print "signal:", signal
    print "signal with noise", signal_with_noise
