def reverse_items_in_tuple(tup):
    tup_list = list(tup)
    for i in range(len(tup_list)):
        tup_list[i] = tup_list[i][::-1]
    reversed_tup = tuple(tup_list)
    return reversed_tup
my_tuple = ("hello", "world", "python")
reversed_tuple = reverse_items_in_tuple(my_tuple)
print("Original Tuple:", my_tuple)
print("Reversed Tuple:", reversed_tuple)
