def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = (keyword * ((len(plaintext) // len(keyword)) + 1))[: len(plaintext)]
    for p, k in zip(plaintext, keyword):
        if p.isalpha():
            base = ord("A") if p.isupper() else ord("a")
            shift = ord(k.upper()) - ord("A")
            encrypted_char = chr((ord(p) - base + shift) % 26 + base)
            ciphertext += encrypted_char
        else:
            ciphertext += p
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = (keyword * ((len(ciphertext) // len(keyword)) + 1))[: len(ciphertext)]
    for c, k in zip(ciphertext, keyword):
        if c.isalpha():
            base = ord("A") if c.isupper() else ord("a")
            shift = ord(k.upper()) - ord("A")
            decrypted_char = chr((ord(c) - base - shift) % 26 + base)
            plaintext += decrypted_char
        else:
            plaintext += c
    return plaintext
