import io
import unittest.mock
import line as ex2


class TP4LineTest(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_slice_advanced(self, mock_stdout):
        inputs = iter(["2.3", "-4", "50", "-32.9"])
        with unittest.mock.patch('builtins.input', side_effect=lambda y: next(inputs)):
            ex2.line()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[0], "El coeficiente A de su ecuación de la recta es: 2.3")
            self.assertEqual(results[1], "El coeficiente B de su ecuación de la recta es: -4.0")
            self.assertEqual(results[2], "El coeficiente X1 de su ecuación de la recta es: 50.0")
            self.assertEqual(results[3], "El coeficiente X2 de su ecuación de la recta es: -32.9")
            self.assertEqual(results[4], "")
            self.assertEqual(results[5], "Para la siguiente ecuación:")
            self.assertEqual(results[6], "\tY = 2.3X + -4.0")
            self.assertEqual(results[7], "")
            self.assertEqual(results[8], "Dados los siguientes puntos:")
            self.assertEqual(results[9], "\tP1 (50.0, 110.99999999999999)")
            self.assertEqual(results[10], "\tP2 (-32.9, -79.66999999999999)")
            self.assertEqual(results[11], "")
            self.assertEqual(results[12], "La distancia entre ellos es: 207.9121422620622")
        inputs2 = iter(["1", "2", "50", "50"])
        with unittest.mock.patch('builtins.input', side_effect=lambda y: next(inputs2)):
            ex2.line()
            results = mock_stdout.getvalue().splitlines()
            self.assertEqual(results[13], "El coeficiente A de su ecuación de la recta es: 1.0")
            self.assertEqual(results[14], "El coeficiente B de su ecuación de la recta es: 2.0")
            self.assertEqual(results[15], "El coeficiente X1 de su ecuación de la recta es: 50.0")
            self.assertEqual(results[16], "El coeficiente X2 de su ecuación de la recta es: 50.0")
            self.assertEqual(results[17], "")
            self.assertEqual(results[18], "Para la siguiente ecuación:")
            self.assertEqual(results[19], "\tY = 1.0X + 2.0")
            self.assertEqual(results[20], "")
            self.assertEqual(results[21], "Dados los siguientes puntos:")
            self.assertEqual(results[22], "\tP1 (50.0, 52.0)")
            self.assertEqual(results[23], "\tP2 (50.0, 52.0)")
            self.assertEqual(results[24], "")
            self.assertEqual(results[25], "La distancia entre ellos es: 0.0")


if __name__ == '__main__':
    unittest.main()
