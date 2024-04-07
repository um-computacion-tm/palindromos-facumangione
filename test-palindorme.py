import unittest
from palindrome import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_with_a(self):
        input_str = "a"  # Renombra la variable de entrada para evitar conflicto con la función input
        result = is_palindrome(input_str)
        self.assertTrue(result)

    def test_with_ala(self):
        input_str = "ala"
        result = is_palindrome(input_str)
        self.assertTrue(result)

    def test_with_neuquen(self):
        input_str = "neuquen"
        result = is_palindrome(input_str)
        self.assertTrue(result)

    def test_with_hola(self):
        input_str = "hola"
        result = is_palindrome(input_str)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
