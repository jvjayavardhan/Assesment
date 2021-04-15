# Author : Jayavardhan Bairabathina
# 2. PROBLEM DEFINITION
# ----------------------------------------------
# Sentence:You really cannot repeat three times the word 'because' because 'because' is a conjunction that should not be used in such a way.
# Question: Write a program logic to reverse the word "because" and print a sentence without using built-in functions/methods.

def reverse_the_word_and_print_sentence(test_str, given_word):
    '''
    A method to reverse the given word and return the string!
    '''
    reversed_word = given_word[::-1]
    return ((reversed_word).join(test_str.split(given_word)))


if __name__ == '__main__':
    test_str = "You really cannot repeat three times the word 'because' because 'because' is a conjunction that should not be used in such a way."
    given_word = 'because'
    print(reverse_the_word_and_print_sentence(test_str, given_word))
