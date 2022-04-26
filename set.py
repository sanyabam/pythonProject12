# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and sea


my_list = [1, 'privet', (25, 'slovo'), [25, 56]]
my_list1 = []
for i in my_list:
    if type(i) == int or type(i) == float or type(i) == bool or type(i) == str\
         or type(i) == tuple:
        my_list1.append(i)
print(my_list1)
my_set = set(my_list1)
print(my_set)




