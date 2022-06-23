
'''
new_lst = [1, 2, 3, 4]
def sum_list(lst):
	if len(lst) == 1:
		return lst[0]
	else:
		return lst[0] + sum_list(lst[1:])
print(sum_list(new_lst))            '''


import functools
new_lst = [1, 2, 3, 4]
print(functools.reduce(lambda x, y: x + y, new_lst))
