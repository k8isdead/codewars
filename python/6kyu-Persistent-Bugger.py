def persistence(n):
    '''
    Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
    which is the number of times you must multiply the digits in num until you reach a single digit.
    
    >>> persistence(39)
    3
    >>> persistence(999)
    4
    >>> persistence(4)
    0
    '''
    if n < 10:
        return 0
    mult = 1
    while n > 0:
        mult = n % 10 * mult
        n = n // 10
    return persistence(mult) + 1
    
