from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    root1 = (-b - sqrt(discriminant)) / (2 * a)
    root2 = None if discriminant == 0 else (-b + sqrt(discriminant)) / (2 * a)
    return root1, root2
