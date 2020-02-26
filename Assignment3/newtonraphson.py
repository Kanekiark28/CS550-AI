def NewtonRaphson(fpoly, a, tolerance=.00001):
    """Given a set of polynomial coefficients fpoly
    for a univariate polynomial function,
    e.g. (3, 6, 0, -24) for 3x^3 + 6x^2 +0x^1 -24x^0,
    find the real roots of the polynomial (if any)
    using the Newton-Raphson method.
    a is the initial estimate of the root and
    starting state of the search
    This is an iterative method that stops when the
    change in estimators is less than tolerance.
   """
    fpoly = (self.fpoly)
    a = self.a 
    fpoly_over_deriv = fpoly/derivative(fpoly) #f(x)/f'(x) -> store as a variable

    while abs(fpoly_over_deriv) >= tolerance:
        fpoly_over_deriv = fpoly/derivative(fpoly)
        fpoly = fpoly - fpoly_over_deriv
    return fpoly
    




def polyval(fpoly, x):
    """polyval(fpoly, x)
    Given a set of polynomial coefficients from highest order to x^0,
    compute the value of the polynomial at x. We assume zero
    coefficients are present in the coefficient list/tuple.
    Example: f(x) = 4x^3 + 0x^2 + 9x^1 + 3 evaluated at x=5
    polyval([4, 0, 9, 3], 5))
    returns 548
    """
    fpoly = (self.fpoly) #instantiate fpoly as a tuple 
    degree = len(fpoly) #length of the polynomial to iterate through tuple and compute degrees
    answer = 0 
    counter = 0 
    while degree > 0 and c:
        answer = fpoly(counter)*x**degree + answer #4(x)^degree
        degree = degree - 1
        counter = counter + 1
    return answer
    




def derivative(fpoly):
    """derivative(fpoly)
    Given a set of polynomial coefficients from highest order to x^0,
    compute the derivative polynomial. We assume zero coefficients
    are present in the coefficient list/tuple.
    Returns polynomial coefficients for the derivative polynomial.
    Example:
    derivative((3,4,5)) # 3 * x**2 + 4 * x**1 + 5 * x**0
    returns: [6, 4] # 6 * x**1 + 4 * x**0"""
    fpoly = (self.fpoly)
    degree = len(fpoly)
    deriv = []
    answer = 0
    counter = 0
    while degree > 0:
        answer = fpol(counter) * degree
        degree = degree - 1
        deriv.append(answer)
    return deriv
