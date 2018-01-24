''' 5. b.
    To get a string from a given string where
    all occurrences of its first char have been
    changed to '$', except the first char itself.
'''

def modify_string(word):
    first_char = word[0]        # set first character of our string to first_char variable
    new_string = first_char     # add first_char to our new empty string, we will add more later

    for pointer in word[1:]:
        if pointer == first_char:
            new_string += '$'
        else:
            new_string += pointer

    return new_string

if __name__ == '__main__':
    print(modify_string('elephant'))
    print(modify_string('arastratiosphecomyia'))
