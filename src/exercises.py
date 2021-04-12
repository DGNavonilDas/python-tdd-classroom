def reverse_list(input_list):
    """
    Reverses order of elements in list input_list.
    """
    i = 0
    n = len(input_list)
    while 2*i < n:
        # Swap i and n-i-1
        input_list[i],input_list[n-i-1] = input_list[n - i - 1],input_list[i]
        i += 1
    
    return input_list

def count_digits(number):
    """
    Return count of digits
    """
    ans = 0
    while number > 0:
        ans += 1
        number = number // 10
    return ans