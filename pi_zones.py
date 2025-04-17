pi_lookup = [0]
for i in range(1, 10001):
    is_prime = True
    if i == 1:
        is_prime = False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    pi_lookup.append(pi_lookup[-1] + (1 if is_prime else 0))

def get_pi(x):
    if 1 <= x <= 10000:
        return pi_lookup[x]
    raise ValueError("x خارج النطاق المسموح به (1–10000)")
