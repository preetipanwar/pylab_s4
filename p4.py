'''4. To demonstrate use of slicing in string'''

# slicing in python is very interesting, easy and has a modern approach
# string[begin : end]    // simply tell where to begin and end to slice a string.
# string[begin : ]       // this means we want to slice from a point to the end of the string
# string[ : end]         // this means we want to slice from a point to the begining of the string

# ------    ---------   -----------    ------- #
# slicing strings
steve_jobs = "Stay hungry, Stay foolish"

# lets slice the string steve_jobs from 0 to 11th position
print(steve_jobs[0:11])     # output: Stay hungry

# lets slice the string steve_jobs from sixth position till end
print(steve_jobs[5:])       # output: hungry, Stay foolish

# lets slice the last three words in the string
print(steve_jobs[-3:])      # see how can we use -ve num as well to slice from the right end instead

# ------    ---------   -----------    ------- #
# slicing works similarly on lists, just like strings
fruits = ['apple', 'mango', 'grapes', 'guava', 'banana']

print(fruits[0])            # output: apple
print(fruits[0 : 3])        # output: apple, mango, grapes
print(fruits[2 : ])         # output: grapes, guava, banana
print(fruits[ : 2])         # output: apple, mango

# so it can easily be observed as the list can be sliced in a similar fashion as strings

# lets make it a bit more advance, what if we wish to slice 'ppl' from apple?
print(fruits[0][1:4])       # output: ppl


# ------    ---------   -----------    ------- #
# real life example
# what if you have a string of url which you want to clean (i.e. you want url just to be till .html

url = "https://www.lynda.com/Bootstrap-tutorials/Bootstrap-4-Essential-Training/372545-2.html?srchtrk=index%3a1%0alinktypeid%3a2%0aq%3abootstrap%0apage%3a1%0as%3arelevance%0asa%3atrue"

# url has a lot of data after .html which normally is meta data is of no use to user,
# we can slice things after .html lets first find .html and then slice every thing after it.

position_of_html = url.find('.html')        # use find() method to find .html
clean_url = url[:position_of_html + 5]      # add 5 position to include .html
print(clean_url)  # output: https://www.lynda.com/Bootstrap-tutorials/Bootstrap-4-Essential-Training/372545-2.html
