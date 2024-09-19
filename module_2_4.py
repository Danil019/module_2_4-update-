numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

primes = []
not_primes = []
is_prime = None

for i in range(len(numbers)):
    for j in range(2, 6, 2):
        if i >= 3 and numbers[i] % 2 == 0 and i >= 2:
            is_prime = False
            break
        elif numbers[i] != 3 and numbers[i] % 3 == 0:
            is_prime = False
            break
        elif numbers[i] < 2:
            break
        else:
            is_prime = True
            break

    if is_prime:
        primes.append(numbers[i])
    elif is_prime is None:
        pass
    else:
        not_primes.append(numbers[i])

print('Простые числа:\n', primes, '\nНе простые числа:\n', not_primes)