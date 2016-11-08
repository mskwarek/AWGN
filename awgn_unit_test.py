import unittest
import awgn

class IsOddTests(unittest.TestCase):
    
    def testOne(self):
        self.failUnless(len(awgn.read_signal_data('dane')) > 0)

def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
