from unittest import TestCase

from snacks import array_snack


class Test(TestCase):
    def test_element_largest(self):
        my_array = [9, 5, 4, 3, 2]
        self.assertEquals(9, array_snack.element_largest(my_array))

    def test_element_largest(self2):
        my_array = [-4, -2, -9, -5, -3]
        import self
        self.assertEquals(-1, array_snack.element_largest(my_array))


class Test(TestCase):
    def test_element_check(self):
        my_array = [5, 8, 2, 6,2]
        self.assertTrue(array_snack.element_check(my_array, 3))

    def test_negative_element(self):
        my_array =[2, 9, -3]
        self.assertTrue(array_snack.element_check(my_array, -3))

    def test_absent_element(self):
        my_array = [2, 3, 6, 7, 8]
        self.assertFalse(array_snack.element_check(my_array, 10))
