from stack import Stack


def reverse_string(my_string):
    
    rev_stack = Stack()
    reversed = my_string[::-1]
    return reversed

    

if __name__ == "__main__":
    
    print(reverse_string("hello"))  # olleh
