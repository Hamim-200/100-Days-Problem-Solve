
# Generator function to produce first n prime numbers.

def prime_generator(n):
    
    count = 0      # Number of primes generated so far
    num = 2        # Start checking from 2, the first prime

    while count < n:           # Keep going until n primes are generated
        is_prime = True        # Assume current number is prime
        i = 2                  # Start checking for factors from 2

        while i * i <= num:   # Only check up to square root of num
            if num % i == 0:  # If divisible, it's not prime
                is_prime = False
                break
            i += 1            # Check next number

        if is_prime:           # If num is prime
            yield num          # Yield one prime number
            count += 1         # Increase prime count

        num += 1               # Check next number


n = int(input("Enter number of primes: "))

for prime in prime_generator(n):
    print(prime, end=" ")



# Checking the prime number
def prime_no(n):
    if n < 2:
        return False  # numbers < 2 are not prime

    for i in range(2, n):   # check divisibility from 2 to n-1
        if n % i == 0:
            return False    # divisible → not prime

    return True  # no divisor found → prime


num = int(input("Enter a Number: "))

if prime_no(num):
    print("Prime")
else:
    print("Not Prime")
