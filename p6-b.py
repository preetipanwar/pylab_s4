''' 6.b. 
    Write a program that accepts a comma separated sequence of words as input
    and prints the words in a comma-separated sequence after sorting them
    alphabetically.
'''
# Suppose the following input is supplied to the program:
# banana,raspberry,apricot,mango,apple,pomegranate"
# Then, the output should be:
# apple,apricot,banana,mango,pomegranate,raspberry

print("Enter a comma separated line, don't add any spaces: ")
line = input()                                      # enter input through keyboard

tokenized_line = line.split(',')                    # split words where there is a comma
sorted_tokenized_line = sorted(tokenized_line)      # sord words alphabetically
sorted_line = ','.join(sorted_tokenized_line)       # join words with comma

print(sorted_line)                                  # print onto console