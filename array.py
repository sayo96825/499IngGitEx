sortable_array = [4,"s",3,"a",7, 9,"y","o"]
print(sortable_array)
int_list = [x for x in sortable_array if isinstance(x,  int)]
int_list.sort()
print(int_list)