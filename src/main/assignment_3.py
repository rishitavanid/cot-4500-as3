import numpy as np


def euler_method(f, t0, y0, h, n):
    """
    Implements Euler's method to approximate the solution of y' = f(t, y).

    Parameters:
        f (function): The function f(t, y).
        t0 (float): Initial value of t.
        y0 (float): Initial value of y.
        h (float): Step size.
        n (int): Number of iterations.

    Returns:
        float: Approximated value of y at the final step.
    """
    t, y = t0, y0
    for _ in range(n):
        y += h * f(t, y)
        t += h
    return y


def runge_kutta_4(f, t0, y0, h, n):
    """
    Implements the classical Runge-Kutta (RK4) method.

    Parameters:
        f (function): The function f(t, y).
        t0 (float): Initial value of t.
        y0 (float): Initial value of y.
        h (float): Step size.
        n (int): Number of iterations.

    Returns:
        float: Approximated value of y at the final step.
    """
    t, y = t0, y0
    for _ in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + h / 2, y + k1 / 2)
        k3 = h * f(t + h / 2, y + k2 / 2)
        k4 = h * f(t + h, y + k3)
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += h
    return y


# Given function: f(t, y) = t - y^2
def func(t, y):
    return t - y ** 2


if __name__ == "__main__":
    # Given parameters
    t0 = 0
    y0 = 1
    t_final = 2
    n = 10  # Number of iterations
    h = (t_final - t0) / n  # Step size

    # Compute results
    euler_result = euler_method(func, t0, y0, h, n)
    runge_kutta_result = runge_kutta_4(func, t0, y0, h, n)

    # Print results
    print(f"Euler Method Result: {euler_result}")
    print(f"Runge-Kutta Method Result: {runge_kutta_result}")

