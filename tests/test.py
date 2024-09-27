import unittest
from src.main import CHARS, length_input, quantity_input, generate_password

class TestInput(unittest.TestCase):
    def test_length_input_is_valid(self):
        self.assertEqual(length_input(length=6), 6)
        self.assertEqual(length_input(length=15), 15)
    
    
    def test_length_input_lower_than_minimum(self):
        with self.assertRaises(ValueError):
            length_input(length=4)

    
    def test_length_input_is_negative(self):
        with self.assertRaises(ValueError):
            length_input(length=-2)

    
    def test_quantity_input_is_valid(self):
        self.assertEqual(quantity_input(quantity=5), 5)
        self.assertEqual(quantity_input(quantity=3), 3)


    def test_quantity_input_is_zero(self):
        with self.assertRaises(ValueError):
            quantity_input(quantity=0)


    def test_quantity_input_is_negative(self):
        with self.assertRaises(ValueError):
            quantity_input(quantity=-2)


    def test_quantity_input_is_lower_than_maximum(self):
        with self.assertRaises(ValueError):
            quantity_input(quantity=7)


    def test_generate_password_is_random(self):
        password = generate_password(length=10, quantity=1)
        self.assertEqual(len(set(password)), len(password))

    
    def test_generate_password_with_valid_characters_only(self):
        passwords = generate_password(length=10, quantity=1)

        for i in range(len(passwords)):
            for char in passwords[i]:
                self.assertIn(char, CHARS)
        
    
    def test_generate_password_length_is_correct(self):
        password_length = 3
        passwords = generate_password(length=password_length, quantity=3)

        for i in range(len(passwords)):
            self.assertEqual(len(passwords[i]), password_length)


    def test_generate_password_quantity_is_valid(self):
        quantity_input = 2
        passwords = generate_password(length=10, quantity=quantity_input)        

        self.assertEqual(len(passwords), quantity_input)


if __name__ == '__main__':
    unittest.main()
