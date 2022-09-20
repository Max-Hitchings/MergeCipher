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
    newWord = ""
    shorterWord = {
        "word": odd if len(odd) < len(even) else even,
        "type": "#" if len(odd) < len(even) else "!",
        "longWord": even if len(odd) < len(even) else odd
    }

    for i in range(1, len(shorterWord["word"])+1):
        newWord += odd[-i]
        newWord += even[-i]

    newWord += shorterWord["type"] + shorterWord["longWord"][:-len(shorterWord["word"])][::-1]
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
    return cipher

def encrypt(inputSentence):
    oddWords, evenWords = splitSentence(inputSentence)
    output = combineLists(oddWords, evenWords)
    return output

def decrypt(inputCipher):
    splitCipher = inputCipher.split()
    plainText = ""
    extraWord = ""
    if len(splitCipher) % 2 != 0:
        extraWord = splitCipher.pop(-1)
        print(extraWord)
    for word in reversed(splitCipher):
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
        plainText = f"{plainText}{newEvenWord} {newOddWord} "

    plainText += extraWord[::-1]
    return plainText


if __name__ == '__main__':
    userInput = "hello world i am pleased to meet you cooloooooooooo"
    # userInput = "hello my name is max"
    en = encrypt(userInput)
    # BUG # Decrypt doesn't work for odd length sentences
    de = decrypt(en)

    print("cipher:", en)
    print("plain text:", de)
