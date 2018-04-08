from math import sqrt


def get_roots(a, b, c):
    """Solves quadratic equation a*x^2 + b*x + c = 0.
    Inputs are coeffitients a, b, c and non-null a is
    assumed. Depending on discriminant, returns two float,
    one float or None, or both of None type roots.
    """        
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
