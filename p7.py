''' 7. 
    Write a program that accepts a sequence of whitespace separated words as input and
    prints the words after removing all duplicate words and sorting them
    alphanumerically.
'''

# Suppose the following input is supplied to the program:
# sun 3.35m and 2m long string includes the sun mercury venus and which includes no sun sense?
# Then, the output should be:
# 2m 3.35m and includes long mercury no sense? string sun thevenus which

print('Enter a line: ')
line = input()

tokenize_line = line.split(' ')                    # split the line at ' ' a space
sort_tokenize_line = sorted(tokenize_line)         # sort tokenized list, note this is a list

clean_list = []                                    # create an empty list

for word in sort_tokenize_line:
    if word in clean_list:                         # if word already in list, do nothing
        pass
    else:                                          # if word not in clean_list, add it
        clean_list.append(word)

new_line = ' '.join(clean_list)                    # join list to form a string
print(new_line)
