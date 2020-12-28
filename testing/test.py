import unittest
import script

class TestMain(unittest.TestCase):
    #where to write test
    def test_do_stuff(self):
        ''' Comment '''
        test_param = 10
        result = script.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'piecesOfString'
        result = script.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff3(self):
        test_param = None
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')
    
    def test_do_stuff4(self):
        test_param = ''
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

unittest.main()