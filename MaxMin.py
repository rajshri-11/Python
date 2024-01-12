def max_num_in_list( list ):
    max = list[ 0 ]
    for x in list:
        if x > max:
            max = x
    return max
print(max_num_in_list([1, 2, -8, 0]))

def min_num_in_list( list ):
    min = list[ 0 ]
    for x in list:
        if x < min:
            min = x
    return min
print(min_num_in_list([1, 2, -8, 0]))
