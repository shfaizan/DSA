# In the following exercise you will finish writing smallest_positive which is a function that finds the smallest
# positive number in a list.

def smallest_positive(in_list):
    current_smallest = None
    for i in in_list:
        if i > 0 and (current_smallest is None or i < current_smallest):
            current_smallest = i
    return current_smallest

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

if __name__ == '__main__':
    pass
