import art_pic

# know about caeser_cipher 'https://en.wikipedia.org/wiki/Caesar_cipher'

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b',
            'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art_pic.logo)


def caesar_cipher():
    word = ""
    for i in text:
        if i not in alphabet:
            word += i
        else:
            position = alphabet.index(i)
            if direction == "encode":
                position += shift
            else:
                position -= shift
            word += alphabet[position]

    return word


game_on = True
while game_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    print(caesar_cipher())

    if input("restart :type 'yes' to go again , otherwise 'no'  : ") == "yes":
        continue
    else:
        print("GOODBYE")
        game_on = False
