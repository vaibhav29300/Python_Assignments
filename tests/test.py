import unittest
import sys
from unittest import result
sys.path.append('C:\\Users\\USER\\Desktop\\assignments.gitlab.com\\assignment_1\\assignment_1')
import app


class TestCalc(unittest.TestCase):
    def test_print_hello_world(self):
        result=app.print_hello_world()
        self.assertEqual(result,"Hello World")
    def test_sum_correct(self):
        result=app.sum(10,5)
        self.assertEqual(result,15)
    def test_get_largest_number_correct(self):
        result=app.get_largest_number(10,5)
        self.assertEqual(result,10)
    def test_get_largest_of_three_correct(self):
        result=app.get_largest_of_three(10,5,2)
        self.assertEqual(result,10)
    def test_print_array(self):
        result=app.print_array(5)
        self.assertEqual(result,[0,1,2,3,4])
    def test_get_sum_of_array(self):
        result=app.get_sum_of_array([1,2,3,4,5])
        self.assertEqual(result,15)
    def test_isPrime(self):
        result=app.isPrime(17)
        self.assertEqual(result,"prime")
    def test_get_array_of_range_of_numbers(self):
        result=app.get_array_of_range_of_numbers(5,10)
        self.assertEqual(result,[5,6,7,8,9,10])
    def test_get_factorial(self):
        result=app.get_factorial(5)
        self.assertEqual(result,120)
    def test_get_factorial_without_loop(self):
        result=app.get_factorial_without_loop(5)
        self.assertEqual(result,120)
    def test_reverse_digits(self):
        result=app.reverse_digits(123)
        self.assertEqual(result,321)
    def test_prime_numbers_in_range(self):
        result=app.prime_numbers_in_range(5,10)
        self.assertEqual(result,[5,7])
    def test_find_number_of_occurences(self):
        result=app.find_number_of_occurences([2,69,7,8,9,2,2],2)
        self.assertEqual(result,3)
    def test_find_first_occurences(self):
        result=app.find_first_occurences([2,69,7,8,9,2,2],69)
        self.assertEqual(result,1)
    def test_print_rhombus(self):
        result=app.print_rhombus(5)
        self.assertEqual(result,"""*****
 *****
  *****
   *****
    *****""")
    def test_number_to_word(self):
        result=app.number_to_word(123).strip()
        self.assertEqual(result,"one two three")
    def test_print_triangle_pointing_right(self):
        result=app.print_triangle_pointing_right(5)
        self.assertEqual(result,"""#
##
###
####
#####""")



if __name__ == '__main__' :
    unittest.main()