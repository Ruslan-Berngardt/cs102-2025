def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    A = ord("A")
    a = ord("a")
    for char in plaintext:
        if "A" <= char <= "Z":
            ciphertext += chr((ord(char) - A + shift) % 26 + A)
        elif "a" <= char <= "z":
            ciphertext += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        else:
            ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    A = ord("A")
    a = ord("a")
    for char in ciphertext:
        if "A" <= char <= "Z":
            plaintext += chr((ord(char) - A - shift) % 26 + A)
        elif "a" <= char <= "z":
            plaintext += chr((ord(char) - a - shift) % 26 + a)
        else:
            plaintext += char
    return plaintext
