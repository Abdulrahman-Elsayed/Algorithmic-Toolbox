# Uses python3
import sys

def fibonacci(n):
    if n <= 1:
        return n
    else:
        previous, current = 0, 1
        
        for _ in range(n - 1):
            previous, current = current, previous + current
            
        return current    


def pisano_period(m):
    previous, current = 0, 1
    
    for i in range(6 * m):
        previous, current = current, (previous + current) % m
        
        if previous == 0 and current == 1:
            return i + 1


def fibonacci_modulo(n, m):
    pisano_length = pisano_period(m)
    n = n % pisano_length
    
    return fibonacci(n) % m
    
    
if __name__ == '__main__':
    #input = sys.stdin.read();
    n, m = map(int, input().split())
    print(fibonacci_modulo(n, m))
