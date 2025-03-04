import unittest  # Import the unittest module for writing and running test cases
from src.main.assignment_3 import euler_method, runge_kutta_4, func  # Import the functions to be tested

# Define a test case class inheriting from unittest.TestCase
class TestNumericalMethods(unittest.TestCase):
    """
    This class contains unit tests for numerical methods used in assignment_3.py.
    It verifies the correctness of the Euler Method and the Runge-Kutta Method (RK4).
    """

    def test_euler_method(self):
        """
        Test the Euler method implementation by checking the computed value
        against the expected result with an error tolerance of 5 decimal places.
        """
        # Define initial conditions
        t0, y0, t_final, n = 0, 1, 2, 10  # Initial time, initial value, final time, and number of iterations
        h = (t_final - t0) / n  # Compute step size

        # Run Euler's method
        result = euler_method(func, t0, y0, h, n)

        # Expected result based on precomputed values
        expected_result = 1.2446380979332121

        # Check if the computed result is close to the expected result
        self.assertAlmostEqual(result, expected_result, places=5)

    def test_runge_kutta_4(self):
        """
        Test the Runge-Kutta (RK4) method implementation by checking the computed value
        against the expected result with an error tolerance of 5 decimal places.
        """
        # Define initial conditions
        t0, y0, t_final, n = 0, 1, 2, 10  # Initial time, initial value, final time, and number of iterations
        h = (t_final - t0) / n  # Compute step size

        # Run Runge-Kutta method (RK4)
        result = runge_kutta_4(func, t0, y0, h, n)

        # Expected result based on precomputed values
        expected_result = 1.251316587879806

        # Check if the computed result is close to the expected result
        self.assertAlmostEqual(result, expected_result, places=5)

# Run the test suite when this script is executed directly
if __name__ == "__main__":
    unittest.main()  # Run all test cases

