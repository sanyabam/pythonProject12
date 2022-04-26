# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and sea



list = [15, 48, 'hello', 6,  19, 'world']
s = 0
for i in list:
    if type(i) == int and i % 2 == 0:
        s += i
    else:
        ind = list.index(i)
        list[ind] = 1
print('Сумма', s)
print(list)

glas = 0
soglas = 0

for i in list:

    if type(i) == str and i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'y' or i == 'u':
        glas += 1
    else:
        soglas += 1
print('Гласных', glas)
print('Согласных', soglas)






















