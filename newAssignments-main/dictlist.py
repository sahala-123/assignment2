My_List = [1, 'hi', 5.29, False, 'fine', 88, True]
result_dict = {}
for item in My_List:
    data_type = type(item)
    if data_type in result_dict:
        result_dict[data_type].append(item)
    else:
        result_dict[data_type] = [item]
print(result_dict)
