import io
import unittest.mock
import leap_year as ex1


class TP4LeapYearTest(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_slice_advanced(self, mock_stdout):
        with unittest.mock.patch('builtins.input', return_value="2000"):
            ex1.leap_year()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "El año 2000 es bisiesto")
        with unittest.mock.patch('builtins.input', return_value="2001"):
            ex1.leap_year()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[1], "El año 2001 no es bisiesto")
        with unittest.mock.patch('builtins.input', return_value="1700"):
            ex1.leap_year()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[2], "El año 1700 no es bisiesto")
        with unittest.mock.patch('builtins.input', return_value="100"):
            ex1.leap_year()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[3], "El año 100 no es bisiesto")


if __name__ == '__main__':
    unittest.main()
