# current_name = ["yusuff","Habbeb","halimoh","rasheed"]
# new_name = ["kola","wale","tolu","kumi","yusuff"]

# for curren,new zip(current_name, new_name):
#     if new == current:
#         print("your are tied already!,the name has been taken")

# # if new_name in current_name:
# #     print("Name is not available")

import functools

list1 = ['A', 'B', 'C']
list2 = ['A', 'D', 'E']


if functools.reduce(lambda x, y: x and y, map(lambda a, b: a == b, list1, list2), True):
    print("Both List are same")
else:
    print("Not same")

list1 = ['A', 'B', 'C']
list2 = ['A', 'C', 'B']

res = [x for x in list1 + list2 if x not in list1 or x not in list2]

print(res)