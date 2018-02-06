''' 6.a.
    To compute the frequency of the words from the input.
    The output should output after sorting the key alphanumerically.
'''

# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

# in the input below write something like:
# sun 3.35m and 2m long string includes the sun Mercury Venus and which includes no sun sense?

print("Enter a line: ")
line = input().lower()                          # accept lower case input
freq = {}                                       # create a dictionary to store the frequency

tokenized_line = line.split(' ')                # split the words apart and add them to a list

for word in tokenized_line:
    if word in freq.keys():                     # if a word exists inside freq
        freq[word] = freq[word] + 1             # increase the value of its key by one
    else:
        freq[word] = 1                          # else, add the word to freq with value 1

for i in sorted(freq):                          # sort freq by key
    print(i + ': ' + str(freq[i]))              # print sorted value

print('\nx --------------- x ------------- x\n')

# Alternative solution: using list.count() method to count the frequency of the words in a list

freq2 = {}

tokenized_line2 = line.split(' ')

for word in tokenized_line2:
    if word not in freq2.keys():                    # if word not in freq2{}
        freq2[word] = tokenized_line2.count(word)   # count every word in list and add to freq2 dictionary

for key, value in sorted(freq2.items()):            # iterate over sorted dictionary
    print(key + ': ' + str(value))          # note the way we used key, value pair (looks much cleaner)
