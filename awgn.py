import numpy

def read_signal_data(filename):
    with open(filename, 'r') as fi:
        return list(fi.read())

def generate_noise(length):
    return numpy.random.normal(0,1,length)

if __name__=='__main__':
    signal = read_signal_data('dane')
    noise = generate_noise(len(signal))
    signal_with_noise = [float(signal[i])+noise[i] for i in range(0, len(signal))]
    print "noise:", noise    
    print "signal:", signal
    print "signal with noise", signal_with_noise
    print "len: ", len(signal_with_noise), len(signal), len(noise)
