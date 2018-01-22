# 2. To find all prime numbers within a given range.
'''
    Prime number ->
    A number is greater than 1 is called a prime number,
    if it has only two factors, namely 1 and the number itself.
'''

def check_prime(num):
    ''' check if num is Prime or not '''
    
    if num > 1:
        is_prime = True             # assuming the number is prime number
        for i in range(2, num):     # looping between 2 and num
            if (num % i) == 0:      # if number (i) completely divides num, then num is not a prime no.
                is_prime = False    # if any no (i) can divide num, it means it isn't prime
        return is_prime             # else it is prime
    return False                    # if number is less than 1 return False.


if __name__ == '__main__':

    for x in range(1, 37):
        if check_prime(x) == True:
            print(x)
