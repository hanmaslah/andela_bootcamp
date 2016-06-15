import unittest
import fizzbuzz
#from fizzbuzz import fizz_buzz

class FizzBuzzTest (unittest.TestCase):
    """
Testing FizzBuzz

    """
    def test_returns_fizz_divisibility_by_three(self):
        """
Test returns fizz when input is divisible by 3
        """
        self.assertEqual(fizzbuzz.fizz_buzz(9),'fizz')

    def test_returns_buzz_divisibility_by_five(self):
         """
Test returns buzz when input is divisible by 5

         """
         self.assertEqual(fizzbuzz.fizz_buzz(25), 'buzz')
         
    def test_returns_fizzbuzz_divisibility_by_five_and_three(self):
          """
Test returns fizzbuzz when input is divisible by both 3 and 5
          """
          self.assertEqual(fizzbuzz.fizz_buzz(45), 'fizzbuzz')
    def test_returns_number_if_not_divisible_by_five_or_three(self):
          """
Test returns number when input is divisible by both 3 and 5
          """
          self.assertEqual(fizzbuzz.fizz_buzz(11), 11)      
    
    def test_returns_error(self):
          """
Test returns fizzbuzz when input is divisible by both 3 and 5
          """
          self.assertEqual(fizzbuzz.fizz_buzz('name'), 'Kindly enter a digit')   
