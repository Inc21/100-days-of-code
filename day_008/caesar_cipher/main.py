from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")


print(logo)

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    #  TODO-1: Create a function called 'encrypt' that
    #  takes the 'text' and 'shift' as inputs.

    # def encrypt(text, shift):
    #     encrypted_text = ""
    #     for letter in text:
    #         position = alphabet.index(letter)
    #         new_position = position + shift
    #         encrypted_text += alphabet[new_position]
    #     print(f"The encoded text is {encrypted_text}")

    #  TODO-2: Inside the 'encrypt' function, shift each letter of the 'text'
    #  forwards in the alphabet by the shift amount and print the encrypted
    #  text.

    #  e.g.
    #  plain_text = "hello"
    #  shift = 5
    #  cipher_text = "mjqqt"
    #  print output: "The encoded text is mjqqt"

    #  HINT: How do you get the index of an item in a list:
    #  https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    #  🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

    #  TODO-3: Call the encrypt function and pass in the user inputs. You
    #  should be able to test the code and encrypt a message.

    #  TODO-1: Create a different function called 'decrypt' that takes the
    #  'text' and 'shift' as inputs.

    #  TODO-2: Inside the 'decrypt' function, shift each letter of the 'text'
    #  *backwards* in the alphabet by the shift amount and
    #  print the decrypted text.

    #  e.g.
    #  cipher_text = "mjqqt"
    #  shift = 5
    #  plain_text = "hello"
    #  print output: "The decoded text is hello"

    # def decrypt(text, shift):
    #     decrypted_text = ""
    #     for letter in text:
    #         position = alphabet.index(letter)
    #         new_position = position - shift
    #         decrypted_text += alphabet[new_position]
    #     print(f"The decoded text is {decrypted_text}")

    #  TODO-3: Check if the user wanted to encrypt or decrypt the message by
    #  checking the 'direction' variable. Then call the correct function based
    #  on that 'direction' variable. You should be able to test the code to
    #  encrypt *AND* decrypt a message.

    # if direction == "encode":
    #     encrypt(text, shift)
    # elif direction == "decode":
    #     decrypt(text, shift)

    #  TODO-1: Combine the encrypt() and decrypt() functions into a single
    #  function called caesar().

    #  TODO-2: Call the caesar() function, passing over the 'text', 'shift' and
    #  'direction' values.

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")
