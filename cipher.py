def takeInput():
    sentence = input("Enter your sentence")

def splitSentence(sentance):
    initalSplit = sentance.split()
    oddWords = []
    evenWords = []

    for i in range(len(initalSplit)):
        if i % 2 == 0:
            oddWords.append(initalSplit[i])
        else:
            evenWords.append(initalSplit[i])

    ### note to self - u are stupid :) ###
    # for word in initalSplit:
    #     if len(word) % 2 == 0:
    #         evenWords.append(word)
    #     else:
    #         oddWords.append(word)
    return oddWords, evenWords

def reverseAndJoinWords(odd, even):
    # print(odd, even)
    newWord = ""

    # odd, even = "531", "nm642"
    shorterWord = {
        "word": odd if len(odd) < len(even) else even,
        "type": "#" if len(odd) < len(even) else "!",
        "longWord": even if len(odd) < len(even) else odd
    }

    for i in range(1, len(shorterWord["word"])+1):
        newWord += odd[-i]
        newWord += even[-i]

    newWord += shorterWord["type"] + shorterWord["longWord"][:-len(shorterWord["word"])][::-1]
    # newWord += shorterWord["type"] + even[:-len(shorterWord["word"])][::-1]
    # if shorterWord["type"] == "odd":
    # #     # x = ""
    # #     # print(even[::-1])
    # #     # print(even[:2][::-1])
    # #     # x = even[:-len(odd)][::-1]
    # #     # print(shorterWord["type"])
    #     newWord += '#' + even[:-len(odd)][::-1]
    # else:
    # #     # newWord += odd[-len(even):]
    # #     # x = even[:-len(odd)][::-1]
    # #     # print(even[:-len(odd)], "sd")
    # #     # print(shorterWord["type"])
    #     newWord += '!' + odd[:-len(even)][::-1]
    return newWord + " "


def combineLists(odd: list, even: list):
    cipher = ""
    shorterList = {
        "list": odd if len(odd) < len(even) else even,
        "type": "odd" if len(odd) < len(even) else "even"
    }
    extraWord = ""
    if len(odd) > len(even):
        extraWord = (odd.pop(-1))

    for i in range(1, len(even) + 1):
        currentWords = (odd[-i], even[-i])
        cipher += reverseAndJoinWords(*currentWords)

    cipher += extraWord[::-1]

    # print(odd[-1][-1], even[-1][-1])
    # currentWords = (odd[-1], even[-1])
    #
    # reverseAndJoinWords(*currentWords)
    return cipher

def encrypt(inputSentence):
    # inputSentence = input("Enter your sentence")
    # inputSentence = "Hello world i am pleased to meet you"
    # inputSentence = "Hello world i am bored"
    expected = "tueoey!m doet!saelp im#a odlllreohw"

    oddWords, evenWords = splitSentence(inputSentence)
    # oddWords = ["Hello", "I", "pleased", "meet"]
    # evenWords = ["world", "am", "to", "you"]

    output = combineLists(oddWords, evenWords)
    return output
    # print(output)
    # print(expected)
    # assert output == "tueoey!m doet!saelp im#a odlllreohw"
    # print(oddWords)
    # print(evenWords)

def decrypt(inputCipher):
    # inputCipher = "tueoey!m doet!saelp im#a odlllreohw"

    splitCipher = inputCipher.split()
    oddWords = []
    plainText = ""
    extraWord = ""
    if len(splitCipher) % 2 != 0:
        extraWord = splitCipher.pop(-1)
        print(extraWord)
    for word in reversed(splitCipher):
        # if
        newOddWord, newEvenWord = "", ""
        for i, char in enumerate(word):
            if char != "#" and char != "!":
                if i % 2 == 0:
                    newEvenWord += char
                else:
                    newOddWord += char
            elif char == "#":
                newOddWord += word[i + 1:]
                break
            elif char == "!":
                newEvenWord += word[i + 1:]
                break
        newEvenWord, newOddWord = newEvenWord[::-1], newOddWord[::-1]
        # print(newOddWord, newEvenWord)
        plainText = f"{plainText}{newEvenWord} {newOddWord} "
        # plainText += newOddWord

    plainText += extraWord[::-1]
    return plainText





if __name__ == '__main__':
    # if input("encrypt or decrypt?") == "decrypt":
    #     decrypt()
    # else:
    #     encrypt()
    # print("hello world i am pleased to meet you cool")
    # userInput = input("enter input")
    userInput = "max hitchings and callum is gay"
    en = encrypt(userInput)
    # BUG # Decrypt doesn't work for odd length sentences
    de = decrypt(en)

    print("cipher:", en)
    # print("tueoey!m doet!saelp im#a odlllreohw")
    print("plain text:", de)

