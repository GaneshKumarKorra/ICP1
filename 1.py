char_list = list(input("Enter a string: "))
del char_list[1:3]
char_list.reverse()
print("Reversed string:", "".join(char_list))
