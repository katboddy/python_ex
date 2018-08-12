from sympy import expand, sympify, solve, solve_poly_inequality, Poly, Symbol, pprint, init_printing, solve_rational_inequalities, sin, solve_univariate_inequality
from sympy.core.sympify import SympifyError
from sympy.plotting import plot

# series
def print_series(n, x_value):
    init_printing(order='rev-lex')
    x = Symbol('x')
    series = x
    for i in range(2, n + 1):
        series = series + (x ** i) / i
    pprint(series)

    series_value = series.subs({x:x_value})
    print("Value of the series at {0}: {1}".format(x_value, series_value))


# product of two expressions
def producd(expr1, expr2):
    prod = expand(expr1*expr2)
    print(prod)


# if __name__ == '__main__':
#     expr1 = input('Enter the first expression: ')
#     expr2 = input('Enter the second expression: ')
#     try:
#         expr1 = sympify(expr1)
#         expr2 = sympify(expr2)
#     except SympifyError:
#         print('invalid input')
#     else:
#         producd(expr1, expr2)


# plot
def plot_expression(expr):
    y = Symbol('y')
    solutions = solve(expr, y)
    expr_y = solutions[0]
    plot(expr_y)


if __name__ == '__main__':
    expr = input('Enter your expression in terms of x and y: ')
    try:
        expr = sympify(expr)
    except SympifyError:
        print('Invalid input')
    else:
        plot_expression(expr)

# solving examples
x = Symbol('x')
expr = x**2 + 5*x + 4
solve(expr, dict=True)

ineq_obj = - x**2 + 4 < 0
lhs = ineq_obj.lhs
p = Poly(lhs, x)
rel = ineq_obj.rel_op
solve_poly_inequality(p,rel)

ineq_obj = ((x -1)/(x+2)) > 0
lhs = ineq_obj.lhs
numer, denom = lhs.as_numer_denom()
p1 = Poly(numer)
p2 = Poly(denom)
rel = ineq_obj.rel_op
solve_rational_inequalities([[((p1,p2), rel)]])

ineq_obj = sin(x) - 0.6 > 0
solve_univariate_inequality(ineq_obj, x, relational=False)