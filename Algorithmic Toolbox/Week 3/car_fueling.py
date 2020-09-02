# python3
import sys


def compute_min_refills(distance, tank, stops):
    x = stops
    x.insert(0, 0)
    x.append(distance)
    n = len(x)
    count = 0
    current = 0
    
    while current < n - 1:
        last = current
        
        while (current < n - 1) and (x[current + 1] - x[last] <= tank):
            current += 1
            
        if last == current:
            return - 1
        
        if current < n - 1:
            count += 1
    
    return count

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
