def vigenere_cipher(message, key, direction=1):
    """Encrypt or decrypt the message using the Vigenère cipher."""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_index = 0
    final_message = ''
    
    for char in message.lower():
        if not char.isalpha():
            final_message += char  # Keep non-alphabetic characters unchanged
        else:
            key_char = key[key_index % len(key)]  # Get the key character for current index
            key_index += 1
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def get_input_choice():
    """Prompt the user for encryption or decryption choice."""
    print("What do you want to do? \n1. Encrypt\n2. Decrypt")
    choice = input("\nChoose one of the above: ").strip()
    
    if choice not in ['1', '2']:
        print("Mala electio!!!")
        exit()
    
    return choice

def main():
    # Get user choice (Encrypt or Decrypt)
    choice = get_input_choice()

    # Get the message and key
    text = input("Enter Message: ")
    key = input("Enter Custom Key: ")

    # Determine the operation (encrypt or decrypt)
    if choice == '1':
        result = vigenere_cipher(text, key, direction=1)
        print(f"Original message: {text}")
        print(f"Key: {key}")
        print(f"Encrypted Message: {result}")
    elif choice == '2':
        result = vigenere_cipher(text, key, direction=-1)
        print(f"Encrypted text: {text}")
        print(f"Key: {key}")
        print(f"Decrypted Message: {result}")

# Execute the program
if __name__ == "__main__":
    main()
