import unittest

class test_dummy(unittest.TestCase):

    def test_dummy_1(self):
        b = 16
        self.assertEqual(b, 16)

    def test_dummy_2(self):

        b = True
        self.assertTrue(b)

    def test_dummy_3(self):

        b = True
        self.assertFalse(b, 'Error in test dummy 3')

    def test_dummy_4(self):

        b = 'stop'
        a = ['start', 'continue', 'stop']

        self.assertIn(b, a)

    def test_dummy_5(self):

        b = 'restart'
        a = ['start', 'continue', 'stop']

        self.assertNotIn(b, a)

    def test_dummy_6(self):
        b = None

        self.assertIsNone(b)