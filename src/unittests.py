import unittest
import data2midi as d

class TestSomeMethods(unittest.TestCase):

    def test_valid(self):
        self.assertTrue(d.data2midi.isValidFormat('csv'))
        self.assertTrue(d.data2midi.isValidFormat('tsv'))
        self.assertTrue(d.data2midi.isValidFormat('CSV'))
        self.assertFalse(d.data2midi.isValidFormat('ust'))

if __name__ == '__main__':
     unittest.main()