# Secret Code Generator: Secret Cipher
def encode_message(message, shift):
    #Encodes a message by shifting letters by 'shift' positions.
    coded = ""
    for char in message:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - start + shift) % 26 + start
            coded += chr(shifted)
        else:
            coded += char  # No-letters are unchanged
    return coded

def decode_message(message, shift):
    #Decodes a message by reversing the shift.
    return encode_message(message, -shift)  # Decoding is negative shift

def get_shift():
    #Prompt user for a valid integer shift value.
    while True:
        shift_input = input("Enter the shift value (integer): ")
        if shift_input.strip().startswith('-'):
            is_negative = True
            number = shift_input.strip()[1:]
        else:
            is_negative = False
            number = shift_input.strip()
        if number.isdigit():
            return int(shift_input)
        else:
            print("Invalid shift. Please enter a whole number.")

def main_menu():
    #Display menu and handle user choice.
    print("=== Secret Code Generator ===")
    while True:
        print("\nMenu:\n1. Encode a message\n2. Decode a message\n3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            message = input("Enter the message to encode: ")
            shift = get_shift()
            encoded = encode_message(message, shift)
            print("Encoded message:", encoded)
        elif choice == '2':
            message = input("Enter the coded message to decode: ")
            shift = get_shift()
            decoded = decode_message(message, shift)
            print("Decoded message:", decoded)
        elif choice == '3':
            print("Thank you for using the Secret Cipher Agent!\nSeeing you soon Agent!\nGoodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main_menu()
