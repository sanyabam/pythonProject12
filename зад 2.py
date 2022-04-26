# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and sea

my_list = [25, 56, 78, 5, 88, 5, 99, 5, 88, 78, 5]
my_list1 = []
for i in my_list:
    if my_list.count(i) > 1 and i not in my_list1:
        my_list1.append(i)
        print((i, my_list.count(i) // 2))


