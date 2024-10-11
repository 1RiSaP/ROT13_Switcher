letters = 'abcdefghijklmnopqrstuvwxyz'

def rot13(message):
    result = ''

    flag = False
    for letter in message:
        if letter.lower() in letters:
            if letter == letter.upper():
                flag = True
            s = letters.index(letter.lower())
            if answer.lower() == 'encrypt':
                s += 13
                if s > 25:
                    s -= 26
            elif answer.lower() == 'decrypt':
                s -= 13
                if s < 0:
                    s += 26
            if flag:
                result += letters[s].upper()
                flag = False
            else:
                result += letters[s]
        else:
            result += letter

    return result

print('-'*20+"ROT13 encryptor/decryptor"+'-'*20)
answer = input("Encrypt or decrypt?\n")
message = input("Enter the text to be encrypted or decrypted\t 0 = stop\n")
while message != '0':

    if answer.lower() == 'encrypt':
        print('--->', rot13(message))
    elif answer.lower() == 'decrypt':
        print('--->', rot13(message))
    else:
        print("Invalid input")

    answer = input("Encrypt or decrypt?\n")
    message = input("Enter the text to be encrypted or decrypted\t 0 = stop\n")