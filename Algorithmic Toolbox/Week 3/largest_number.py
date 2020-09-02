#Uses python3

import sys

def is_greater_or_equal(a, b):
    if a[0] > b[0]:
        return True
    elif a[0] == b[0]:
        if len(a) == 1 and len(b) == 1:
            return True
        elif len(a) > len(b):
            d = len(a) - len(b)
            b += b[0] * d
        else:
            d = len(b) - len(a)
            a += a[0] * d     
        return is_greater_or_equal(a[1:], b[1:])    
    else:
        return False
    
    
def largest_number(a):
    res = ''
    while a:
        max_order = ' '
        for num in a:
            if is_greater_or_equal(num, max_order):
                max_order = num
        
        res += max_order
        a.remove(max_order)        
        
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
