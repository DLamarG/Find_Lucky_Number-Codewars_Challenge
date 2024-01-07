def filter_lucky(lst):
    import re
    lucky_list = []
    list_of_str_nums = [str(j) for j in lst]
    for num in list_of_str_nums:
        if re.search(r'[7]', num):
            lucky_list.append(num)
    return [int(a) for a in lucky_list]

print(filter_lucky([1,2,3,4,5,6,7,68,69,70,15,17])) # --> [7,70,17]
print(filter_lucky([71,9907,69])) # --> [71,9907] 