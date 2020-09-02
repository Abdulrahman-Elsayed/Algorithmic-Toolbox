def pisano_numbers(n, m):
    previous, current = 0, 1
    pisano_numbers = [previous, current]
    
    for i in range(6 * m):
        previous, current = current, (previous + current) % m
        pisano_numbers.append(current)
        if previous == 0 and current == 1:
            pisano_numbers = pisano_numbers[0:-2]
            return pisano_numbers
            break

            
n = int(input())

fibonacci_mod_10 = pisano_numbers(n, 10)
fibonacci_mod_10_sum = sum(fibonacci_mod_10)
fibonacci_mod_10_len = len(fibonacci_mod_10)

if n < fibonacci_mod_10_len:
    print(sum(fibonacci_mod_10[:n + 1]) % 10)
else:
    f = n // fibonacci_mod_10_len
    n = n % fibonacci_mod_10_len
    print((fibonacci_mod_10_sum + sum(fibonacci_mod_10[:n + 1])) % 10)
