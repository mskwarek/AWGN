import argparse
import numpy


def read_signal_data(filename):
    with open(filename) as f:
        content = f.readlines()
    return [numpy.complex(x.strip()) for x in content]


def write_noised_signal_data(filename, noised):
    formatted = [str(noised[i]).replace(")", "").replace("(", "") for i in range(0, len(noised))]
    with open(filename, 'w+') as fi:
        fi.write("\n".join(formatted))


def measure_power(x):
    return float(sum([(float(1) / float(len(x))) * numpy.absolute(x[i]) ** 2 for i in range(0, len(x))]))


def generate_random_vector(signal):
    re = numpy.random.normal(0, 1, len(signal))
    im = numpy.random.normal(0, 1, len(signal))
    return [numpy.complex(re[x], im[x]) for x in range(0, len(re))]


def convert_snr_to_lin(snr):
    return float(10 ** (snr / 20))


def noise_signal(orig_signal, snr):
    variance = numpy.sqrt(measure_power(orig_signal) / (2 * convert_snr_to_lin(snr)))
    random_data = generate_random_vector(orig_signal)
    print len(random_data), variance
    noise = [random_data[i] * variance for i in range(0, len(random_data))]
    return [(orig_signal[i]) + noise[i] for i in range(0, len(orig_signal))]


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', type=str, required=True, dest='src')
    parser.add_argument('--dst', type=str, required=True, dest='dst')
    parser.add_argument('--snr', type=float, required=True, dest='snr')
    return parser.parse_args()


if __name__ == '__main__':
    signal = read_signal_data(parse_arguments().src)
    print signal
    signal_with_noise = noise_signal(signal, parse_arguments().snr)
    print signal_with_noise
    write_noised_signal_data(parse_arguments().dst, signal_with_noise)
