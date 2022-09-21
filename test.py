import random
import unittest
import json
import requests
import time

from cipher import encrypt, decrypt

class TestSum(unittest.TestCase):

    def test_default(self):
        input = "hello world i am pleased to meet you"
        self.assertEqual(decrypt(encrypt(input)).strip(), input)

    def test_odd_sentence(self):
        input = "hello world i am pleased to meet you coolio"
        self.assertEqual(decrypt(encrypt(input)).strip(), input)

    def test_random(self):
        words = []
        for x in range(random.randint(5, 9)):
            wordRequest = requests.get("https://random-word-api.herokuapp.com/word")
            words.append(wordRequest.json()[0])

            # dont get rate limited :)
            time.sleep(.01)
        input = ' '.join(words)
        x = input
        self.assertEqual(decrypt(encrypt(input)).strip(), x, f"encrypted: {encrypt}")

    # def test_sum_tuple(self):
    #     self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    for x in range(10):
        words = []
        for x in range(random.randint(5, 9)):
            wordRequest = requests.get("https://random-word-api.herokuapp.com/word")
            words.append(wordRequest.json()[0])

            # dont get rate limited :)
            time.sleep(.001)
        input = ' '.join(words)
        x = input
        if decrypt(encrypt(input)).strip() !=  x:
            print(x + "\n" + encrypt(input) + "\n" + decrypt(encrypt(input)).strip())
        assert decrypt(encrypt(input)).strip() ==  x
    # unittest.main()
# topper quarts whipworms giftless fico mojo



# import json
#
# from .cipher import encrypt, decrypt
#
# def test(testCase, i):
#     output = decrypt(encrypt(testCase))
#     if output == testCase:
#         print(f"test {i} passed")
#     else:
#         print(f"test {i} failed\noutput: {output}\nshould have been: {testCase}")
#
