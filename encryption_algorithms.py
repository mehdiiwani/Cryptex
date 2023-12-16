# encryption_algorithms.py
import math


class EncryptionAlgorithms:
    @staticmethod
    def caesar_encrypt(text, shift):
        # Implement Caesar encryption
        return ''.join(chr((ord(char) - 97 + shift) % 26 + 97) for char in text)

    @staticmethod
    def caesar_decrypt(text, shift):
        # Implement Caesar decryption
        return ''.join(chr((ord(char) - 97 - shift) % 26 + 97) for char in text)

    @staticmethod
    def reverse_encrypt(text):
        # Implement Reverse encryption
        return text[::-1]

    @staticmethod
    def reverse_decrypt(text):
        # Implement Reverse decryption
        return text[::-1]

    @staticmethod
    def atbash_encrypt(text):
        # Implement Atbash encryption
        return ''.join(chr(219 - ord(char)) if 'a' <= char <= 'z' else char for char in text)

    @staticmethod
    def atbash_decrypt(text):
        # Implement Atbash decryption
        return ''.join(chr(219 - ord(char)) if 'a' <= char <= 'z' else char for char in text)
    
    @staticmethod
    def transposition_encrypt(text, key):
        return ''.join(text[i::key] for i in range(key))

    @staticmethod
    def transposition_decrypt(text, key):
        num_columns = math.ceil(len(text) / key)
        num_rows = key
        num_shaded_boxes = (num_columns * num_rows) - len(text)
        plaintext = [''] * num_columns
        col = 0
        row = 0
        for symbol in text:
            plaintext[col] += symbol
            col += 1
            if (col == num_columns) or (col == num_columns - 1 and row >= num_rows - num_shaded_boxes):
                col = 0
                row += 1
        return ''.join(plaintext)
    
    @staticmethod
    def vigenere_encrypt(text, key):
        encrypted_text = ""
        for i in range(len(text)):
            shift = ord(key[i % len(key)]) - 97
            encrypted_char = chr((ord(text[i]) - 97 + shift) % 26 + 97)
            encrypted_text += encrypted_char
        return encrypted_text

    @staticmethod
    def vigenere_decrypt(text, key):
        decrypted_text = ""
        for i in range(len(text)):
            shift = ord(key[i % len(key)]) - 97
            decrypted_char = chr((ord(text[i]) - 97 - shift) % 26 + 97)
            decrypted_text += decrypted_char
        return decrypted_text
    
    @staticmethod
    def affine_encrypt(text, a, b):
        # Implement Affine encryption
        return ''.join(chr(((a * (ord(char) - 97) + b) % 26) + 97) for char in text)

    @staticmethod
    def affine_decrypt(text, a, b):
        # Implement Affine decryption
        a_inv = pow(a, -1, 26)
        return ''.join(chr(((a_inv * ((ord(char) - 97) - b)) % 26) + 97) for char in text)

    @staticmethod
    def simple_substitution_encrypt(text, key):
        # Implement Simple Substitution encryption
        return ''.join(chr((ord(key[ord(char) - 97]) - 97) % 26 + 97) for char in text)

    @staticmethod
    def simple_substitution_decrypt(text, key):
        # Implement Simple Substitution decryption
        return ''.join(chr((key.index(chr((ord(char) - 97) % 26 + 97))) + 97) for char in text)
    @staticmethod
    def rail_fence_encrypt(text, key):
        # Implement Rail Fence encryption
        rail = [['\n' for i in range(len(text))] for j in range(key)]
        dir_down = False
        row, col = 0, 0
        for i in range(len(text)):
            if (row == 0) or (row == key - 1):
                dir_down = not dir_down
            rail[row][col] = text[i]
            col += 1
            if dir_down:
                row += 1
            else:
                row -= 1
        result = []
        for i in range(key):
            for j in range(len(text)):
                if rail[i][j] != '\n':
                    result.append(rail[i][j])
        return "".join(result)

    @staticmethod
    def rail_fence_decrypt(text, key):
        # Implement Rail Fence decryption
        rail = [['\n' for i in range(len(text))] for j in range(key)]
        dir_down = None
        row, col = 0, 0
        for i in range(len(text)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False
            rail[row][col] = '*'
            col += 1
            if dir_down:
                row += 1
            else:
                row -= 1
        index = 0
        for i in range(key):
            for j in range(len(text)):
                if ((rail[i][j] == '*') and (index < len(text))):
                    rail[i][j] = text[index]
                    index += 1
        result = []
        row, col = 0, 0
        for i in range(len(text)):
            if row == 0:
                dir_down = True
            if row == key-1:
                dir_down = False
            if (rail[row][col] != '*'):
                result.append(rail[row][col])
                col += 1
            if dir_down:
                row += 1
            else:
                row -= 1
        return "".join(result)

    @staticmethod
    def rot13_encrypt(text):
        # Implement ROT13 encryption
        result = ""
        for i in range(len(text)):
            char = text[i]
            if (char.isupper()):
                result += chr((ord(char) + 13 - 65) % 26 + 65)
            else:
                result += chr((ord(char) + 13 - 97) % 26 + 97)
        return result

    @staticmethod
    def rot13_decrypt(text):
        # Implement ROT13 decryption
        return EncryptionAlgorithms.rot13_encrypt(text)  # ROT13 is its own inverse