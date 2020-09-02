# python3


def max_pairwise_product(numbers):
    
    max_index1 = numbers.index(max(numbers))
    numbers2 = numbers.copy()
    numbers2[max_index1] = 0
    max_index2 = numbers2.index(max(numbers2))
    return (numbers[max_index1] * numbers[max_index2])


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
