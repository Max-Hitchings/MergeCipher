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
    print(odd, even)
    newWord = ""

    # odd, even = "531", "nm642"
    shorterWord = {
        "word": odd if len(odd) < len(even) else even,
        "type": "odd" if len(odd) < len(even) else "even"
    }

    for i in range(1, len(shorterWord["word"])+1):
        newWord += odd[-i]
        newWord += even[-i]
    if shorterWord["type"] == "odd":
        # x = ""
        # print(even[::-1])
        # print(even[:2][::-1])
        # x = even[:-len(odd)][::-1]
        print(shorterWord["type"])
        newWord += '#' + even[:-len(odd)][::-1]
    else:
        # newWord += odd[-len(even):]
        # x = even[:-len(odd)][::-1]
        # print(even[:-len(odd)], "sd")
        print(shorterWord["type"])
        newWord += '!' + odd[:-len(even)][::-1]
    return newWord + " "


def combineLists(odd: list, even: list):
    cipher = ""
    shorterList = {
        "list": odd if len(odd) < len(even) else even,
        "type": "odd" if len(odd) < len(even) else "even"
    }

    for i in range(1, len(shorterList["list"]) + 1):
        currentWords = (odd[-i], even[-i])
        cipher += reverseAndJoinWords(*currentWords)

    if len(odd) > len(even):
        cipher += odd[-1][::-1]

    # print(odd[-1][-1], even[-1][-1])
    # currentWords = (odd[-1], even[-1])
    #
    # reverseAndJoinWords(*currentWords)
    return cipher

def encrypt():
    inputSentence = input("Enter your sentence")
    # inputSentence = "Hello world i am pleased to meet you"
    # inputSentence = "Hello world i am bored"
    expected = "tueoey!m doet!saelp im#a odlllreohw"

    oddWords, evenWords = splitSentence(inputSentence)
    # oddWords = ["Hello", "I", "pleased", "meet"]
    # evenWords = ["world", "am", "to", "you"]

    output = combineLists(oddWords, evenWords)
    print(output)
    # print(expected)
    # assert output == "tueoey!m doet!saelp im#a odlllreohw"
    # print(oddWords)
    # print(evenWords)

def decrypt():
    pass


if __name__ == '__main__':
    if input("encrypt or decrypt?") == "decrypt":
        decrypt()
    else:
        encrypt()

