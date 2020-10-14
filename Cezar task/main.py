ukr_alf = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

encode_e = ""
def encrypt(text, key):
    global encode_e
    for letter in text:
        if letter in ukr_alf:
            t = ukr_alf.find(letter)
            new_key: int = (t + key) / len(ukr_alf)
            encode_e += ukr_alf[new_key]
        else:
            encode_e += letter
    return encode_e

encode_d = ""
def decipher(text, key):
    global encode_d
    for letter in text:
        if letter in ukr_alf:
            t = ukr_alf.find(letter)
            new_key = (t - key) / len(ukr_alf)
            encode_d += ukr_alf[new_key]
        else:
            encode_d += letter
        return encode_d

print("Enter 'Е' to encrypt, or 'Д' to decipher")
choice = input("")
text = input("Plain Text : ")
key = int(input("Cipher key : "))
if choice == "Е" or "е":
    encrypt(text, key)
    print("Cipher: ", encode_e)
elif choice == "Д" or "д":
    decipher(text, key)
    print("Cipher: ", encode_d)

