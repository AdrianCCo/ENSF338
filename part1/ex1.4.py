def funci(n, my_dict = dict()):

    if n in my_dict:
        return my_dict.get(n)
    
    if n == 0 or n == 1:
        my_dict[n] = n
        return n

    else:
        result = funci(n - 1, my_dict) + funci(n - 2, my_dict)
    
    my_dict[n] = result

    return result

