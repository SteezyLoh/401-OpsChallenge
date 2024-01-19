# RESOURCE: https://github.com/SteezyLoh/401-OpsChallenge/blob/main/Ops-401Challenge-class06.py 


#!/usr/bin/env python3

from cryptography.fernet import Fernet
import os

# Write the key to a file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key from a file
def load_key():
    return open("key.key", "rb").read()

# ENCRYPT a file
def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        data = file.read()
    
    f = Fernet(key)
    encrypted_data = f.encrypt(data)
    
    with open(file_path + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

# DECRYPT a file
def decrypt_file(file_path, key):
    with open(file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    
    with open(file_path.replace(".enc", ""), "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

# Encrypt all files in a folder and its subfolders
def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

# Decrypt all files in a folder and subfolders
def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

# Main function
def main():
    # Check if key file exists, if not, generate a new key
    if not os.path.exists("key.key"):
        write_key()

    # Load the key
    key = load_key()

    # Prompt the user to select a mode
    mode = int(input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n5. Encrypt a folder\n6. Decrypt a folder\n"))

    if mode in [1, 2]:
        # File encryption or decryption
        file_path = input("Enter the file path: ")
        if mode == 1:
            encrypt_file(file_path, key)
            print("File encrypted successfully.")
            os.remove(file_path)  # Delete the original file
        elif mode == 2:
            decrypt_file(file_path, key)
            print("File decrypted successfully.")
            os.remove(file_path)  # Delete the encrypted file

    elif mode in [3, 4]:
        # String encryption or decryption
        text = input("Enter the cleartext string: ")
        if mode == 3:
            encrypt_string(text, key)
        elif mode == 4:
            decrypt_string(text, key)

    elif mode == 5:
        # Encrypt a folder and its contents
        folder_path = input("Enter the folder path: ")
        encrypt_folder(folder_path, key)
        print("Folder encrypted successfully.")

    elif mode == 6:
        # Decrypt a folder and its contents
        folder_path = input("Enter the folder path: ")
        decrypt_folder(folder_path, key)
        print("Folder decrypted successfully.")

if __name__ == "__main__":
    main()

#RESOURCE: https://github.com/SteezyLoh/401-OpsChallenge/blob/main/Ops-401Challenge-class06.py
