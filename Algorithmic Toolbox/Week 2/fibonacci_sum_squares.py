def last_digit(n):
    previous = 0
    current = 1
    n = n % 60
    if n <= 1:
        return n
    else:
        for _ in range(n - 1):
            previous, current = current, (previous + current) % 10
        return current    
    
if __name__ == '__main__':
    n = int(input())
    last_digit1 = last_digit(n)
    last_digit2 = last_digit(n + 1)
    print((last_digit1 * last_digit2) % 10)
    