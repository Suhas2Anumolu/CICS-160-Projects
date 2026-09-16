def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n*0.5)+1):
        if n % i == 0:
            return False
    return True

def are_relatively_prime(x, y):
    for i in range(2, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            return False

    return True


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

    decomp = prime_decomposition(n)
    return len(decomp) == 2 and decomp[0] != decomp[1]
