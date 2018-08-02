import math
 
def genPrimes(context):
    primes = []
    count = 3
    while True:
        isprime = True
        for x in range(2, int(math.sqrt(count) + 1)):
            if context.get_remaining_time_in_millis() < 1000:
                return primes
            if count % x == 0:
                isprime = False
                break
        if isprime:
            primes.append(count)
        count += 1
 
def lambda_handler(event, context):
    primes = genPrimes(context)
    return primes