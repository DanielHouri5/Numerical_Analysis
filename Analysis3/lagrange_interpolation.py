from colors import bcolors
from Romberg_method import romberg_integration, f, definition_domain
import math


def lagrange_interpolation(x_data, y_data, x):
    """
    Lagrange Interpolation

    Parameters:
    x_data (list): List of x-values for data points.
    y_data (list): List of y-values for data points.
    x (float): The x-value where you want to evaluate the interpolated polynomial.

    Returns:
    float: The interpolated y-value at the given x.
    """
    n = len(x_data)
    result = 0.0

    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term

    return result


if __name__ == '__main__':
    """
        print(" Date: 08/04/24\n"
              " Group: Daniel Houri , 209445071 \n"
              "        Yakov Shtefan , 208060111 \n"
              "        Vladislav Rabinovich , 323602383 \n"
              " Git: https://github.com/DanielHouri5/Examiner3/tree/main \n"
              " Name: Eve Hackmon , 209295914 \n"
              " Input: \n")
    """
    x_data = [1.2, 1.3, 1.4, 1.5, 1.6]
    y_data = [3.5095, 3.6984, 3.9043, 4.1293, 4.3756]

    x_interpolate1 = 1.35
    x_interpolate2 = 1.65
    y_interpolate1 = lagrange_interpolation(x_data, y_data, x_interpolate1)
    y_interpolate2 = lagrange_interpolation(x_data, y_data, x_interpolate2)
    print(bcolors.OKBLUE, "\nInterpolated value at x =", x_interpolate1, "is y =", round(y_interpolate1, 1), bcolors.ENDC)
    print(bcolors.OKBLUE, "\nInterpolated value at x =", x_interpolate2, "is y =", round(y_interpolate2, 1), bcolors.ENDC)
    print()

    a = round(y_interpolate1, 1)
    b = round(y_interpolate2, 1)

    if not definition_domain(a) or not definition_domain(b):
        print("Error - division by zero!")
    else:
        n = 1
        integral1 = romberg_integration(f, a, b, n)
        integral2 = romberg_integration(f, a, b, n+1)
        print("n:    integral:")
        print("------------------------")
        print(n, " - ", integral1)
        print(n+1, " - ", integral2)
        while round(integral1, 5) != round(integral2, 5):
            n += 1
            integral1 = romberg_integration(f, a, b, n)
            integral2 = romberg_integration(f, a, b, n + 1)
            print(n + 1, " - ", integral2)

        #print(f" Division into n={n} sections ")
        print(bcolors.OKBLUE, f"\nApproximate integral in range [{a},{b}] is {round(integral2, 5)}", bcolors.ENDC)

