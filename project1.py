def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n*0.5)+1):
        if n % i == 0:
            return False
    return True


def are_relatively_prime(x, y):
    if is_prime(x) and is_prime(y):
        return True
    else:
        return False


def primes_up_to(n):
    prime_list = []
    for i in range(n):
        if is_prime(i):
            prime_list.append(i)
    return prime_list


def prime_decomposition(n):

    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1

    if n > 1:
        factors.append(n)
    return factors


def decomp_check(n):
    duplicate = set()

    for num in prime_decomposition(n):
        if num in duplicate:
            return False
        duplicate.add(num)
        if len(duplicate) > 2:
            return False
    return True
