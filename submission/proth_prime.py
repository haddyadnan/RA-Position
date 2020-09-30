from decimal import Decimal
import decimal
decimal.getcontext().prec = 1000000
#Import decimal to handle large output and avoid overflow error

def ProthPrime():
    
    '''
    This function prompts user to provide a proth number as input then check if said input is a proth prime
    
    
    Input
    -----
    proth number: int
    Input must be a proth number
    
    Return
    ------
    status: string
    The status of the number if sanity check is passed or not and if it's a proth prime or not. The integer that satisfies the condition is also printed
    
    Reference
    ---------
    https://en.wikipedia.org/wiki/Proth%27s_theorem
    
    Examples
    -------
    from proth_prime import ProthPrime
    >>> ProthPrime()
    ... Enter a proth number: 1153
    >>> sanity check 'Passed': 1153 is a proth number
    >>> 928 satisfies the condition. 1153 is a proth prime
    >>> proth_prime()
    ... Enter a proth number: 9
    >>> sanity check 'Passed': 9 is a proth number
    >>> 9 is not a proth prime
    >>> proth_prime()
    ... Enter a proth number: 7
    >>> sanity check 'Failed': 7 is not a proth number. Input must be a proth number. See docstring
    
    ''' 
    
    #SImple try and except to handle error
    try:
        #prompt user for input (input must be a proth number)
        n = int(input('Enter a proth number: '))
        
        #sanity check to confirm input is a proth number
        if (lambda N:N-1&1-N>N**.5)(n):
            print(f'sanity check \'Passed\': {n} is a proth number')
            
            #run a loop from 2 to n to try all integer within the range and check if the proth theorem's condition is satisfied
            for a in range(2,n+1):
                #if a==n then no integer within the range satisfies the condition
                if a == n:
                    print(f'{n} is not a proth prime')
                #Terminate the loop once the condition is satisfied    
                if int((Decimal(a)**(Decimal(n-1)/Decimal(2)) + 1)) % n == 0:
                    print(f'{a} satisfies the condition. {n} is a proth prime')
                    break
                #continue looping if the condition is satisfied till a == n (if a >= n the condition cannot be satisfied neither)
                elif int((Decimal(a)**(Decimal(n-1)/Decimal(2)) + 1)) % n != 0:
                    continue

        else:
            print(f'sanity check \'Failed\': {n} is not a proth number, Input must be a proth number. See docstring')
    except:
        print('please check input for possible error. \nOnly Integers accepted, alphabets and special characters will return error')

#For command line use        
if __name__ == '__main__':
    ProthPrime()
