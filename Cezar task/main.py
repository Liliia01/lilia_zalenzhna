alphabetUpper = 'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
alphabetLower = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'

def encode(text: str, key: int) -> str:
    encodedAlphabetUpper = 'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    encodedAlphabetLower = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'


    encodedAlphabetUpper = encodedAlphabetUpper[key:] + encodedAlphabetUpper[:key]
    encodedAlphabetLower = encodedAlphabetLower[key:] + encodedAlphabetLower[:key]

    x = 0
    encodedText = ''

    while(x < len(text)):
        y = 0
        if text[x].isupper():
            while (y < len(alphabetUpper)):
                if text[x] == alphabetUpper[y]:
                    encodedText += encodedAlphabetUpper[y]
                y+=1
        elif text[x].islower():
            while (y < len(alphabetLower)):
                if text[x] == alphabetLower[y]:
                    encodedText += encodedAlphabetLower[y]
                y += 1
        else:
            if text[x] == ' ':
                encodedText += ' '
            elif text[x] == '!':
                encodedText += '!'
            elif text[x] == ',':
                encodedText += ','
            else:
                encodedText += '.'
        x+=1

    text = encodedText
    print(text)
    return text

def decode(text: str, key: int) -> str:
    encodedAlphabetUpper = 'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    encodedAlphabetLower = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'

    encodedAlphabetUpper = encodedAlphabetUpper[key:] + encodedAlphabetUpper[:key]
    encodedAlphabetLower = encodedAlphabetLower[key:] + encodedAlphabetLower[:key]

    x = 0
    decodedText = ''

    while (x < len(text)):
        y = 0
        if text[x].isupper():
            while (y < len(alphabetUpper)):
                if text[x] == encodedAlphabetUpper[y]:
                    decodedText += alphabetUpper[y]
                y += 1
        elif text[x].islower():
            while (y < len(encodedAlphabetLower)):
                if text[x] == encodedAlphabetLower[y]:
                    decodedText += alphabetLower[y]
                y += 1
        else:
            if text[x] == ' ':
                decodedText += ' '
            elif text[x] == '!':
                decodedText += '!'
            elif text[x] == ',':
                decodedText += ','
            else:
                decodedText += '.'
        x += 1
    text = decodedText
    print(text)
    return text
if __name__ == '__main__':

    text_to_encode = 'Привіт. Сьогодні чудовий день для нападу на галлів'
    key = 8
    encoded_text = encode(text_to_encode, key)
    decoded_text = decode(encoded_text, key)

    assert text_to_encode == decoded_text, "Oooops! Something go wrong"



