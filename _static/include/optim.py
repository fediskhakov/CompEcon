# Collection of simple optimization algorithms from the Computational Economics course
#
# by Fedor Iskhakov, 2020

import numpy as np

def bisection(f,a=0,b=1,tol=1e-6,maxiter=100,callback=None):
    '''Bisection method for solving equation f(x)=0
    on the interval [a,b], with given tolerance and number of iterations.
    Callback function is invoked at each iteration if given.
    '''
    if f(a)*f(b)>0:
        raise ValueError('Function has the same sign at the bounds')
    for i in range(maxiter):
        err = abs(b-a)
        if err<tol: break
        x = (a+b)/2
        a,b = (x,b) if f(a)*f(x)>0 else (a,x)
        if callback != None: callback(err=err,x=x,iter=i)
    else:
        raise RuntimeError('Failed to converge in %d iterations'%maxiter)
    return x


def newton(fun,grad,x0,tol=1e-6,maxiter=100,callback=None):
    '''Newton method for solving equation f(x)=0
    with given tolerance and number of iterations.
    Callback function is invoked at each iteration if given.
    '''
    for i in range(maxiter):
        x1 = x0 - fun(x0)/grad(x0)
        err = abs(x1-x0)
        if callback != None: callback(err=err,x0=x0,x1=x1,iter=i)
        if err<tol: break
        x0 = x1
    else:
        raise RuntimeError('Failed to converge in %d iterations'%maxiter)
    return (x0+x1)/2


def solve_sa(F,x0,tol=1e-6,maxiter=100,callback=None):
    '''Computes the solution of fixed point equation x = F(x)
    with given initial value x0 and algorithm parameters
    Method: successive approximations
    '''
    for i in range(maxiter):  # main loop
        x1 = F(x0)  # update approximation
        err = np.amax(abs(x0-x1))  # allow for x to be array
        if callback != None: callback(iter=i,err=err,x=x1,x0=x0)
        if err<tol:  
            break  # break out if converged
        x0 = x1  # get ready to the next iteration
    else:
        raise RuntimeError('Failed to converge in %d iterations'%maxiter)
    return x1


def newton2(fun,grad,x0,tol=1e-6,maxiter=100,callback=None):
    '''Newton method for solving equation f(x)=0, x is vector of 2 elements,
    with given tolerance and number of iterations.
    Callback function is invoked at each iteration if given.
    '''
    # conversion to array function of array argument
    npfun = lambda x: np.asarray(fun(x[0],x[1]))
    npgrad = lambda x: np.asarray(grad(x[0],x[1]))
    for i in range(maxiter):
        x1 = x0 - np.linalg.inv(npgrad(x0)) @ npfun(x0)  # matrix version
        err = np.amax(np.abs(x1-x0))  # vector version
        if callback != None: callback(iter=i,err=err,x0=x0,x1=x1,fun=fun)
        if err<tol: break
        x0 = x1
    else:
        raise RuntimeError('Failed to converge in %d iterations'%maxiter)
    return (x0+x1)/2
    

# def grid_search(fun,bounds=(0,1),ngrid=10):
#     '''Grid search between given bounds over given number of points'''
#     grid = np.linspace(*bounds,ngrid)
#     func = fun(grid)
#     i = np.argmax(func)  # index of the element attaining maximum
#     return grid[i]

