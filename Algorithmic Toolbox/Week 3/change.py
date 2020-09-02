# Uses python3

def get_change(m):
    n = 0

    while m >= 10:
        m -= 10
        n += 1

    while m >= 5:
        m -= 5
        n += 1

    while m >= 1:
        m -= 1
        n += 1   

    return n

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
