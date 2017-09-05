# binary search
# 1.2

# guess a number between 1 and 100
# high/low problem

# simple search - start at index 1 and work up
# binary search - start at middle and determine if in upper or lower range

# simple search - takes n steps
# binary search - log base 2 of n

# binary search only works if list is in order.

# log base 2 - log(2)8 = 3
# 2^5 = 32 <-> log(2)32 = 5

# https://www.khanacademy.org/computing/computer-science/algorithms

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else: low = mid + 1

    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 1))
print(binary_search(my_list, 3))
print(binary_search(my_list, 9))
print(binary_search(my_list, 1))
