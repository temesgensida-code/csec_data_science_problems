def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return f"the number {n} is not a prime number"
    return f"the number {n} is a prime number"

print(is_prime(11))