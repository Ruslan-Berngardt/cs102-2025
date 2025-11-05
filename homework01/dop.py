"""Has a module that encrypts the text"""


def encrypt_growing_shift(plaintext, start, delta):
    """Encrypts the text"""
    alphabet_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    alphabet_upper = alphabet_lower.upper()
    result = []
    shift = start
    for char in plaintext:
        if char in alphabet_lower:
            idx = alphabet_lower.index(char)
            new_idx = (idx + shift) % len(alphabet_lower)
            result.append(alphabet_lower[new_idx])
            shift += delta
        elif char in alphabet_upper:
            idx = alphabet_upper.index(char)
            new_idx = (idx + shift) % len(alphabet_upper)
            result.append(alphabet_upper[new_idx])
            shift += delta
        else:
            result.append(char)
    return "".join(result)
