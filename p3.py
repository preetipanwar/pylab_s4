''' 3. To print ‘n terms of Fibonacci series using iteration '''

fibonacci_list = [1, 1]                                         # placing seed values in a list

def fib(num):
    ''' fibonacci series'''
    while len(fibonacci_list) < num:
        # find the len of list in every loop
        length_of_list = len(fibonacci_list)

        last_item = fibonacci_list[length_of_list - 1]          # last item in list
        second_last_item = fibonacci_list[length_of_list - 2]   # second last item in list

        new_number = last_item + second_last_item               # next number in fibonacci
        fibonacci_list.append(new_number)                       # add new item to the list

    print(fibonacci_list)                                       # print output

if __name__ == '__main__':
    fib(10)
