# Example code to be discussed in the following videos

import time

def parity (n,verbose=False):
    '''Returns 1 if passed integer number is odd
    '''
    if not isinstance(n, int): raise TypeError('Only integers in parity()')
    if verbose: print('n = ', format(n, "b"))  # print binary form of the number
    return n & 1  # bitwise and operation returns the value of last bit

def maximum_from_list (vars):
    '''Returns the maximum from a list of values
    '''
    m=float('-inf')  # init with the worst value
    for v in vars:
        if v > m: m = v
    return m

def binary_search(grid=[0,1],val=0,delay=0):
    '''Returns the index of val on the sorted grid
    Optional delay introduces a delay (in microsecond)
    '''
    i1,i2 = 0,len(grid)-1
    if val==grid[i1]: return i1
    if val==grid[i2]: return i2
    j=(i1+i2)//2
    while grid[j]!=val:
        if val>grid[j]:
            i1=j
        else:
            i2=j
        j=(i1+i2)//2  # divide in half
        time.sleep(delay*1e-6)  # micro-sec to seconds
    return j

def compositions(N,m):
    '''Iterable on compositions of N with m parts
    Returns the generator (to be used in for loops)
    '''
    cmp=[0,]*m
    cmp[m-1]=N  # initial composition is all to the last
    yield cmp
    while cmp[0]!=N:
        i=m-1
        while cmp[i]==0: i-=1  # find lowest non-zero digit
        cmp[i-1] = cmp[i-1]+1  # increment next digit
        cmp[m-1] = cmp[i]-1    # the rest to the lowest
        if i!=m-1: cmp[i] = 0  # maintain cost sum
        yield cmp
