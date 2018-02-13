'''2. To find all prime numbers within a given range.'''

'''
    Prime number ->
    A number is greater than 1 is called a prime number,
    if it has only two factors, namely 1 and the number itself.
'''

lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

for num in range(lower_limit, upper_limit + 1):
    if num > 1:
        num_is_prime = True             # assuming the number is prime number
        for i in range(2, num):         # looping between 2 and num
            if (num % i) == 0:          # if number (i) completely divides num, then num is not a prime
                num_is_prime = False    # if any no (i) can divide num, it means it isn't prime
                break                   # break the inner loop

    if num_is_prime == True:
        print(num)
