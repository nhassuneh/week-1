# add code below ...
import string


# exercise 1
def palindrome(word):
    # lowercase and remove spaces
    clean_word = word.lower().replace(" ", "")
    # remove punctuation
    for p in string.punctuation:
        clean_word = clean_word.replace(p, "")
    # flip the word to check if it is a palindrome
    return_value = clean_word[::-1]

    print("Cleaned string:", clean_word)
    print("Is palindrome?:", return_value == clean_word)

    return return_value == clean_word


# exercise 2
def parentheses(sequence):
    # parentheses counter
    counter = 0
    # take input
    input = sequence
    # convert input to list
    my_list = list(input)
    # Loop through list
    # parentheses add or subtract from counter
    for i in my_list:
        if i == "(":
            counter += 1
        elif i == ")":
            counter -= 1
        if counter < 0:
            return False
    # return true if counter is 0, else false
    if counter == 0:
        return True
    else:
        return False