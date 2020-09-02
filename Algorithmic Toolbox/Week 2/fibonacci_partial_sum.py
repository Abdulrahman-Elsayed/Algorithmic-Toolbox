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


def fibonacci_last_digit_sum(k):
    fibonacci_mod_10 = pisano_numbers(k, 10)
    fibonacci_mod_10_sum = sum(fibonacci_mod_10)
    fibonacci_mod_10_len = len(fibonacci_mod_10)
    if k < fibonacci_mod_10_len:
        return sum(fibonacci_mod_10[:k + 1])
    else:
        f = k // fibonacci_mod_10_len
        k = k % fibonacci_mod_10_len
        return f * fibonacci_mod_10_sum + sum(fibonacci_mod_10[:k + 1])
            
m, n = map(int, input().split())           

from_sum = fibonacci_last_digit_sum(m - 1)
to_sum = fibonacci_last_digit_sum(n)
result = (to_sum - from_sum) % 10 
print(result)