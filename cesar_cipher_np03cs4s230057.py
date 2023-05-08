"""
This module provides a simple implementation of the Caesar Cipher encryption and decryption algorithm.
"""
import os



def welcome():
    '''
    This function writes a welcome text
    '''
    print('Welcome to the Caesar Cipher \nThis program encrypts and decrypts text with the caesar cipher')

def enter_message():
    a = input('Would you like to encrypt (e) or decrypt (d): ')
    a = a.lower()
    if a == 'e':
        text_to_encrypt = input('What message would you like to encrypt: ').upper()
        shift = int(input('What is the shift number: '))
        encrypted_text = encrypt(text_to_encrypt, shift)
        print(f'The encrypted text is: {encrypted_text}')

    elif a == 'd':
        text_to_decrypt = input('What message would you like to decrypt: ').upper()
        shift = int(input('what is the shift number:'))
        decrypted_text = decrypt(text_to_decrypt, shift)
        print(f'The decrypted text is: {decrypted_text}')

    else:
        print('Invalid mode')
        enter_message()

def encrypt(normal_text, key):
    """
    Encrypt the plaintext using the given shift key and return the resulting ciphertext
    """
    decrypted_text = ''
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num_alpha = len(alpha)
    for string in normal_text:
        string = string.upper()
        if not string == ' ':
            index = alpha.find(string)
            if index == -1:
                decrypted_text += string
            else:
                new_index = (index + key) % num_alpha
                decrypted_text += alpha[new_index]
        else:
            decrypted_text += ' '
    return decrypted_text


def decrypt(encrypted_text, key):
    """
    Decrypt the ciphertext using the given shift key and return the resulting plaintext
    """
    normal_text = ''
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


    num_alpha = len(alpha)
    for string in encrypted_text:
        string = string.upper()
        if not string == ' ':
            index = alpha.find(string)
            if index == -1:
                normal_text += string
            else:
                new_index = (index - key) % num_alpha
                normal_text += alpha[new_index]
        else:
            normal_text += ' '
    return normal_text

def process_file(filename, mode, shift):
    messages = []
    with open(filename, 'r') as f:
        for line in f:
            message = line.strip()
            if mode == 'e':
                encrypted = encrypt(message, shift)
                messages.append(encrypted)
            elif mode == 'd':
                decrypted = decrypt(message, shift)
                messages.append(decrypted)
    return messages
def is_file(filename):
    return os.path.exists(filename)
def write_messages(messages):
    with open('results.txt', 'w') as f:
        for message in messages:
            f.write(message + '\n')
def message_or_file():
    mode = ""
    while mode not in ["e", "d"]:
        mode = input("Would you like to encrypt (e) or decrypt (d):").lower()

        if mode not in ["e", "d"]:
            print("Invalid mode, please enter 'e' for encrypt or 'd' for decrypt.")
    source = ""
    while source not in ["c", "f"]:
        source = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if source not in ["c", "f"]:
            print("Invalid source, please enter 'c' for console or 'f' for file.")
    if source == "c":
        key = input('what is the shift number:')
        encrypt(source,key)
    else:
        filename = input("Enter filename: ")
        while not is_file(filename):
            print(f"File '{filename}' not found.")
            filename = input("Enter filename: ")
        with open(filename, "r") as f:
            message = f.read().strip()
    return mode, message, filename


def main():
    welcome()
    message_or_file()
    


main()