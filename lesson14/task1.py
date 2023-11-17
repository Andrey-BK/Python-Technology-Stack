def print_list_recursive(list, index=0):
    if index < len(list):
        print(list[index])
        print_list_recursive(list, index + 1)
    else:
        print("Конец списка")

my_list = [1, 2, 3, 4, 5]
print_list_recursive(my_list)
