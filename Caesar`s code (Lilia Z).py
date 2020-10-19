def encode(text: str, key: int) -> str:
    alphabet_lower = 'йцукенгшщзхъфывапролджэячсмитьбю'
    alphabet_upper = alphabet_lower.upper()
    alphabet_len = len(alphabet_lower)

    ord_first_letter_lower = ord('а')
    ord_first_letter_upper = ord('А')

    new_text = ''

    for й in text:
        if й in alphabet_lower:
            new_text += chr(((ord(й) - ord_first_letter_lower + key) % alphabet_len) + ord_first_letter_lower)
        elif й in alphabet_upper:
            new_text += chr(((ord(й) - ord_first_letter_upper + key) % alphabet_len) + ord_first_letter_upper)
        else:
            new_text += й

    return new_text


def decode(text: str, key: int) -> str:
    return encode (text, -key)


if __name__ == "__main__":
    text = 'Привыт. Сьогодны чудовий день для нападу на галлыв'
    key = 8
    encoded_text = encode(text=text, key=key)
    decoded_text = decode(text=encoded_text, key=key)

    assert text == decoded_text, "Oooops! Something go wrong"



