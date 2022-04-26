# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and sea
import string

text = 'Мне нравится учить Python.'
for i in string.punctuation:
    if i in text:
        text = text.replace(i, '')
print(text)
text = text.split()
print(max(text, key=len))






