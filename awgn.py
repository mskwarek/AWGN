import argparse
import numpy


def read_signal_data(filename):
    with open(filename, 'r') as fi:
        return list(fi.read())


def write_noised_signal_data(filename, noised):
    formatted = [str(noised[i]) for i in range(0, len(noised))]
    with open(filename, 'w+') as fi:
        fi.write("\n".join(formatted))


def measure_power(x):
    return float(sum([(float(1) / float(len(x))) * float(x[i]) ** 2 for i in range(0, len(x))]))


def generate_random_vector(signal):
    return numpy.random.normal(0, 1, len(signal))


def convert_snr_to_lin(snr):
    return float(10 ** (snr / 20))


def noise_signal(orig_signal, snr):
    variance = float(numpy.sqrt(measure_power(orig_signal) / convert_snr_to_lin(snr)))
    noise = variance * generate_random_vector(orig_signal)
    return [float(orig_signal[i]) + noise[i] for i in range(0, len(orig_signal))]


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', type=str, required=True, dest='src')
    parser.add_argument('--dst', type=str, required=True, dest='dst')
    parser.add_argument('--snr', type=float, required=True, dest='snr')
    return parser.parse_args()


if __name__ == '__main__':
    signal = read_signal_data(parse_arguments().src)
    signal_with_noise = noise_signal(signal, parse_arguments().snr)
    write_noised_signal_data(parse_arguments().dst, signal_with_noise)

