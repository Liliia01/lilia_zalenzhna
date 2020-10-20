alf = "абвгдеєжзиіїйклмнопрстуфхцчшщьюя"
alf_upper = "АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"

def encrypt(text: str, key: int):
    encoded_text = ""
    leng = len(alf)
    for letter in text:
        if letter in alf:
            a = alf.find(letter)
            first_key: int = (a + key) % leng
            encoded_text += alf[first_key]
        elif letter in alf_upper:
            a = alf_upper.find(letter)
            first_key: int = (a + key) % leng
            encoded_text += alf_upper[first_key]
        else:
            encoded_text += letter
    return encoded_text

def decipher(text: str , key: int):
    decoded_text = ""
    leng = len(alf)
    for letter in text:
        if letter in alf:
            a = alf.find(letter)
            first_key: int = (a - key) % leng
            decoded_text += alf[first_key]
        elif letter in alf_upper:
            a = alf_upper.find(letter)
            first_key: int = (a - key) % leng
            decoded_text += alf_upper[first_key]
        else:
            decoded_text += letter
    return decoded_text

if __name__ == "__main__":
    text = 'Привіт. Сьогодні чудовий день для нарпаду на галлів'
    key=8
    encoded_text =encrypt (text=text, key=key)
    decoded_text =decipher (text=encoded_text, key=key)

    assert text == decoded_text, "Ooops!Something go wrong"


