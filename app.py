# app.py
from flask import Flask, request, render_template
from encryption_algorithms import EncryptionAlgorithms

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        text = request.form.get('text')
        algorithm = request.form.get('algorithm')
        action = request.form.get('action')
        shift = int(request.form.get('shift')) if algorithm == 'caesar' and request.form.get('shift') else None
        key = request.form.get('key') if algorithm in ['vigenere', 'transposition', 'simple_substitution', 'rail_fence'] else None
        if action == 'encrypt':
            if algorithm == 'caesar':
                result = EncryptionAlgorithms.caesar_encrypt(text, shift)
            elif algorithm == 'reverse':
                result = EncryptionAlgorithms.reverse_encrypt(text)
            elif algorithm == 'atbash':
                result = EncryptionAlgorithms.atbash_encrypt(text)
            elif algorithm == 'vigenere':
                result = EncryptionAlgorithms.vigenere_encrypt(text, key)
            elif algorithm == 'transposition':
                result = EncryptionAlgorithms.transposition_encrypt(text, int(key))
            elif algorithm == 'rail_fence':
                result = EncryptionAlgorithms.rail_fence_encrypt(text, int(key))
            elif algorithm == 'simple_substitution':
                result = EncryptionAlgorithms.simple_substitution_encrypt(text, key)
            elif algorithm == 'rot13':
                result = EncryptionAlgorithms.rot13_encrypt(text)
            else:
                result = "Unknown algorithm"
        elif action == 'decrypt':
            if algorithm == 'caesar':
                result = EncryptionAlgorithms.caesar_decrypt(text, shift)
            elif algorithm == 'reverse':
                result = EncryptionAlgorithms.reverse_decrypt(text)
            elif algorithm == 'atbash':
                result = EncryptionAlgorithms.atbash_decrypt(text)
            elif algorithm == 'vigenere':
                result = EncryptionAlgorithms.vigenere_decrypt(text, key)
            elif algorithm == 'transposition':
                result = EncryptionAlgorithms.transposition_decrypt(text, int(key))
            elif algorithm == 'rail_fence':
                result = EncryptionAlgorithms.rail_fence_decrypt(text, int(key))
            elif algorithm == 'simple_substitution':
                result = EncryptionAlgorithms.simple_substitution_decrypt(text, key)
            elif algorithm == 'rot13':
                result = EncryptionAlgorithms.rot13_decrypt(text)
            else:
                result = "Unknown algorithm"
        else:
            result = "Unknown action"
        return render_template('index.html', result=result, algorithm=algorithm)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)