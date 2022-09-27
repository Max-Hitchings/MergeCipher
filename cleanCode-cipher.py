def takeInput():
    sentence = input("Enter your sentence")
    for char in ["!#$%&'()*+, -./:;<=>?@[\]^_`{|}~"]:
        sentence.replace(char, '')
    sentence.replace('"', '')

    return sentence

def splitSentence(sentance):
    initalSplit = sentance.split()
    oddWords = []
    evenWords = []

    for i in range(len(initalSplit)):
        if i % 2 == 0:
            oddWords.append(initalSplit[i])
        else:
            evenWords.append(initalSplit[i])

    return oddWords, evenWords

def reverseAndJoinWords(odd, even):
    newWord = ""
    oddL, evenL = len(odd), len(even)

    shorterWord = {
        "word": odd if oddL < evenL else even,
        "type": "#" if oddL < evenL else "!",
        "longWord": odd if oddL > evenL else even
    }

    for i in range(1, len(shorterWord["word"])+1):
        newWord += odd[-i]
        newWord += even[-i]

    newWord += shorterWord["type"] + shorterWord["longWord"][:-len(shorterWord["word"])][::-1]

    return newWord + " "


def combineLists(odd: list, even: list):
    cipher = ""
    # shorterList = {
    #     "list": odd if len(odd) < len(even) else even,
    #     "type": "odd" if len(odd) < len(even) else "even"
    # }
    extraWord = ""
    if len(odd) > len(even):
        extraWord = (odd.pop(-1))

    # loop through words to length of even because that will always be <= len of odd words
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
    # split the cipher up into its two word blocks
    splitCipher = inputCipher.split()
    plainText = ""
    extraWord = ""

    # checks for end of a word signaled by either ! or #
    if '!' not in splitCipher[-1] and '#' not in splitCipher[-1]:
        extraWord = splitCipher.pop(-1)

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
        plainText = f"{plainText}{newEvenWord} {newOddWord} "

    plainText += extraWord[::-1]
    return plainText


if __name__ == '__main__':
    while True:
        if input("encrypt or decrypt? (e/d) ") == "d":
            print(decrypt(takeInput()))
        else:
            print(encrypt(takeInput()))

        if input("again? (y/n) ") == "n":
            break
