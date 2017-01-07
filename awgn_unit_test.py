import unittest

import awgn


class IsOddTests(unittest.TestCase):
    
    def testOne(self):
        self.failUnless(len(awgn.read_signal_data('dane')) > 0)

    def testSum(self):
        self.failUnless(awgn.measure_power([2, 2, 2, 2]) is not 4)

    def testNoise(self):
        import matplotlib.pyplot as plot
        import numpy as np
        x = np.linspace(-2*np.pi, 2*np.pi, 500)
        y = 10*np.sin(x)
        z = awgn.noise_signal(y, 30)
        plot.plot(x, y)
        plot.plot(x, z)
        plot.show()

def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
