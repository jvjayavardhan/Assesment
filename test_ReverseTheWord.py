#Author : Jayavardhan Bairabathina
# 2. PROBLEM DEFINITION - TEST
# ----------------------------------------------
# Sentence:You really cannot repeat three times the word 'because' because 'because' is a conjunction that should not be used in such a way.
# Question: Write a program logic to reverse the word "because" and print a sentence without using built-in functions/methods.

import unittest

from main import reverse_the_word_and_print_sentence


class TestReverseTheWord(unittest.TestCase):
    '''
    A class to test the method test_reverse_the_word_and_print_sentence!
    '''

    def test_reverse_the_word_and_print_sentence(self):
        test_str = "You really cannot repeat three times the word 'because' because 'because' is a conjunction that should not be used in such a way."
        out_put_test_str = "You really cannot repeat three times the word 'esuaceb' esuaceb 'esuaceb' is a conjunction that should not be used in such a way."
        self.assertEqual(reverse_the_word_and_print_sentence(test_str, 'because'), out_put_test_str)
        self.assertEqual(reverse_the_word_and_print_sentence(test_str, ' because '), out_put_test_str)


if __name__ == '__main__':
    unittest.main()
