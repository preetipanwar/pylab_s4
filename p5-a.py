''' 5. a)
    To add 'ing' at the end of a given string (length should be at least 3). If the
    given string already ends with 'ing' then add 'ly' instead. If the string length of
    the given string is less than 3, leave it unchanged.
    Sample String : 'abc'
    Expected Result : 'abcing'
    Sample String : 'string'
    Expected Result : 'stringly'
'''

def stringing(word):
    ''' modifying strings '''
    if len(word) >= 3:
        #check if the last three letters are 'ing'
        if word[-3:] == 'ing':      # if last 3 characters are 'ing'
            return word + 'ly'
        else:
            return word + 'ing'
    return word                     # if word is less than 3, return word

if __name__ == '__main__':
    print(stringing('abc'))
    print(stringing('string'))
