from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if a == 0:
        print("Function solves STRICTLY quadratic equation.")
        return
    if discriminant < 0:
        root1 = None
        root2 = None
    else:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = None if discriminant == 0 else (-b + sqrt(discriminant)) / (2 * a)
    return root1, root2
