import numpy as np
import matplotlib.pyplot as plt

def function_to_integrate(x):
    """Function to be tested"""
    return x**2

def analytic_integral_of_f(a=None, b=None):
    """
    Analytical integral of function we are tesing
    Input: a starting value (lower limit) and an ending value (upper limit)
    Output: in this case, the integral of x^2
    """
    return 1/3. * (b**3 - a**3)

def trapezoidal_rule(f, a=None, b=None, n=None):
    """
    Given a function to integrate, a starting point, ending point, and number of points between
    this function will calculate the integral using the trapezoidal rule (trapezoid fitted segments to curve)
    Input: function, a(start), b(end), n(number of points)
    Output: Integral of given function (quite accurate)
    """
    h = (b - a)/n
    value = 0.
    for x in np.linspace(a, b - h, n - 1): #a, b-h to avoid going too far (minus 1 step.) n - 1 to avoid extra count
        value += 0.5 * (f(x + h)+f(x))  
    return value*h

def lefthand_riemann(f, a=None, b=None, n=None):
    """
    Given a function to integrate, a starting point, ending point, and number of points between
    this function will calculate the integral using the Lefthand Riemann sums method (left step rectangles along curve)
    Input: function, a(start), b(end), n(number of points)
    Output: Integral of given function (less accurate than other methods)
    """
    h = (b - a)/n
    value = 0.
    for x in np.linspace(a, b - h, n - 1):
        value += f(x) + h
        value += h 
    return value * h
    
 
def simpson_rule(f, a=None, b=None, n=None):
    """
    Given a function to integrate, a starting point, ending point, and number of points between
    this function will calculate the integral using simpson rule method.(3 point parabola estimates)    
    Input: function, a(start), b(end), n(number of points)
    Output: Integral of given function (very accurate)
    """
    h = (b - a)/n
    value = 0.
    for x in np.linspace(a, b-h, n-1):
            value += (h/3.) * (f(x) + (4.*(f(x + h))) + (f(x + h + h)))
    return value / 2

#Writer's notes:
#1 - requires me to divide by 2 to find relatively accurate value
#2 - does not take into account extra ending steps to impliment trapezoidal rule / proper spare end point integration

def relative_error(true=None, estimate=None):
    value = np.abs(true - estimate) / np.abs(true)
    return value

if __name__ == "__main__":
    a = 0 #starting point
    b = 1 #ending point
    n = 10 # initial number of points value
    answer = analytic_integral_of_f(a, b) #true answer to test accuracy
    
    simpson_int_10 = simpson_rule(function_to_integrate, a, b, n)
    lefthand_int_10 = lefthand_riemann(function_to_integrate, a, b, n)
    trape_int_10 = trapezoidal_rule(function_to_integrate, a, b, n)
        
    simpson10 = relative_error(answer, simpson_int_10)   
    lefthand10 = relative_error(answer, lefthand_int_10)
    trapezoid10 = relative_error(answer, trape_int_10)
    print('For number of steps equals:', n)
    print('Simpson error:', simpson10)
    print('Lefthand error:', lefthand10)
    print('Trapezoidal error:', trapezoid10)
    print('\n')
    
    #same sequence for n = 10**2
    n = 100
    
    simpson_int_100 = simpson_rule(function_to_integrate, a, b, n)
    lefthand_int_100 = lefthand_riemann(function_to_integrate, a, b, n)
    trape_int_100 = trapezoidal_rule(function_to_integrate, a, b, n)
    
    simpson100 = relative_error(answer, simpson_int_100)
    lefthand100 = relative_error(answer, lefthand_int_100)
    trapezoid100 = relative_error(answer, trape_int_100)
    print('For number of steps equals:', n)
    print('Simpson error:', simpson100)
    print('Lefthand error:', lefthand100)
    print('Trapezoidal error:', trapezoid100)   
    print('\n')
    
    #same sequence for n = 10**3
    n = 1000
    
    simpson_int_1000 = simpson_rule(function_to_integrate, a, b, n)
    lefthand_int_1000 = lefthand_riemann(function_to_integrate, a, b, n)
    trape_int_1000 = trapezoidal_rule(function_to_integrate, a, b, n)
    
    simpson1000 = relative_error(answer, simpson_int_1000)
    lefthand1000 = relative_error(answer, lefthand_int_1000)
    trapezoid1000 = relative_error(answer, trape_int_1000)
    print('For number of steps equals:', n)
    print('Simpson error:', simpson1000)
    print('Lefthand error:', lefthand1000)
    print('Trapezoidal error:', trapezoid1000)
    print('\n')
    
    #same sequence for n = 10**4 
    n = 10000
    simpson_int_10000 = simpson_rule(function_to_integrate, a, b, n)
    lefthand_int_10000 = lefthand_riemann(function_to_integrate, a, b, n)
    trape_int_10000 = trapezoidal_rule(function_to_integrate, a, b, n)
    
    simpson10000 = relative_error(answer, simpson_int_10000)
    lefthand10000 = relative_error(answer, lefthand_int_10000)
    trapezoid10000 = relative_error(answer, trape_int_10000)
    print('For number of steps equals:', n)
    print('Simpson error:', simpson10000)
    print('Lefthand error:', lefthand10000)
    print('Trapezoidal error:', trapezoid10000)
    
    #Increasing number of steps decreases our error percent. Makes sense as the more precise the data is, and the more points we have to evaluate, the more accurate integral techniques are.
    #By doubling the number of steps we cut our error in half. In the code above, the error margin decreases by a magnitude of 10 each time.
    
    #condensing error values at different step sizes
    lefthandarray = [lefthand10, lefthand100, lefthand1000, lefthand10000]
    trapezoidarray = [trapezoid10, trapezoid100, trapezoid1000, trapezoid10000]
    simpsonarray = [simpson10, simpson100, simpson1000, simpson10000]
    
    #Plotting bit of code:
    plt.plot(lefthandarray, label = 'Lefthand Riemann Error', color = 'blue')
    plt.plot(trapezoidarray, label = 'Trapezoidal Error', color = 'purple')
    plt.plot(simpsonarray, label = 'Simpson Error', color = 'orange')
    plt.title('Integration Methods and Relative Error')
    plt.yscale('log')
    plt.ylabel('Error values')
    plt.xlabel('Powers of 10 for number of points between 0 and 1')
    plt.legend()
    plt.show()
