
# Check Palindrome
def palindrome_check(str):
    input_string = str
    reverse_string = reverseString(str)

    if(reverse_string == input_string):
        return True

    return False


def reverseString(str):

    str =list(str)

    start_index = 0
    end_index = len(str) -1

    while end_index > start_index:
        str[start_index], str[end_index] = str[end_index], str[start_index]
        start_index = start_index + 1
        end_index = end_index - 1

    return ''.join(str)


if __name__ =='__main__':
    print(palindrome_check('debasis'))
    print(palindrome_check('madam'))