import unittest
import os
import sys
file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir + "/src")

from climb import (
    count_ways_to_climb_basic,
    count_ways_to_climb_memo,
    count_ways_to_climb_table,
)


class TestClimbBasic(unittest.TestCase):
    """
    Test class for the Climbing Stairs challenge functions.

    Each test case verifies the correctness of the implemented functions.
    """
    """
        Test case for count_ways_to_climb_basic function.

        - Behavior: Verifies that the function returns the correct count of ways to climb stairs.
        - Parameters: num_steps (int) - The number of steps to climb.
        - Return Value: int - The count of ways to climb the stairs.
        """
    def test_with_0(self):
        num = 0
        result = 1
        self.assertEqual(count_ways_to_climb_basic(num), result)

    def test_with_1(self):
        num = 1
        result = 1
        self.assertEqual(count_ways_to_climb_basic(num), result)

    def test_with_2(self):
        num = 2
        result = 2
        self.assertEqual(count_ways_to_climb_basic(num), result)

    def test_with_10(self):
        num = 10
        result = 274
        self.assertEqual(count_ways_to_climb_basic(num), result)

    def test_with_20(self):
        num = 20
        result = 121415
        self.assertEqual(count_ways_to_climb_basic(num), result)


class TestClimbMemo(unittest.TestCase):
    """
        Test case for count_ways_to_climb_memo function.

        - Behavior: Verifies that the function returns the correct count of ways to climb stairs with memoization.
        - Parameters: num_steps (int) - The number of steps to climb.
                      memo (dict) - Memoization dictionary.
        - Return Value: int - The count of ways to climb the stairs.
        """
    
    def test_with_0(self):
        num = 0
        result = 1
        self.assertEqual(count_ways_to_climb_memo(num), result)

    def test_with_1(self):
        num = 1
        result = 1
        self.assertEqual(count_ways_to_climb_memo(num), result)

    def test_with_2(self):
        num = 2
        result = 2
        self.assertEqual(count_ways_to_climb_memo(num), result)

    def test_with_10(self):
        num = 10
        result = 274
        self.assertEqual(count_ways_to_climb_memo(num), result)

    def test_with_20(self):
        num = 20
        result = 121415
        self.assertEqual(count_ways_to_climb_memo(num), result)


class TestClimbTable(unittest.TestCase):
    """
        Test case for count_ways_to_climb_table function.

        - Behavior: Verifies that the function returns the correct count of ways to climb stairs with dynamic programming.
        - Parameters: num_steps (int) - The number of steps to climb.
        - Return Value: int - The count of ways to climb the stairs.
        """
    def test_with_0(self):
        num = 0
        result = 1
        self.assertEqual(count_ways_to_climb_table(num), result)

    def test_with_1(self):
        num = 1
        result = 1
        self.assertEqual(count_ways_to_climb_table(num), result)

    def test_with_2(self):
        num = 2
        result = 2
        self.assertEqual(count_ways_to_climb_table(num), result)

    def test_with_10(self):
        num = 10
        result = 274
        self.assertEqual(count_ways_to_climb_table(num), result)

    def test_with_20(self):
        num = 20
        result = 121415
        self.assertEqual(count_ways_to_climb_table(num), result)


if __name__ == "__main__":
    unittest.main()
