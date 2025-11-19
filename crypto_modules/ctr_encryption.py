# Simple CTR Encryption (XOR-based)
from .utils import DEFAULT_SEED, generate_lcg_bytes

BLOCK_SIZE = 8


def pad(data: bytes) -> bytes:
    pad_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    if pad_len == 0:
        pad_len = BLOCK_SIZE
    return data + bytes([pad_len] * pad_len)


def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))


def increment_counter(counter: bytes) -> bytes:
    """Increment counter by 1 (big-endian)"""
    counter_int = int.from_bytes(counter, 'big')
    counter_int = (counter_int + 1) % (256 ** len(counter))
    return counter_int.to_bytes(len(counter), 'big')


def encrypt_blocks(data: bytes, key: bytes, nonce: bytes) -> bytes:
    ciphertext = bytearray()
    counter = nonce
    for i in range(0, len(data), BLOCK_SIZE):
        block = data[i:i + BLOCK_SIZE]
        # Encrypt the counter to generate keystream
        keystream = xor_bytes(counter, key)
        # XOR plaintext with keystream
        cipher_block = xor_bytes(block, keystream)
        ciphertext.extend(cipher_block)
        # Increment counter for next block
        counter = increment_counter(counter)
    return bytes(ciphertext)


def process_text(text: str) -> str:
    if not text:
        return "ERROR: Input text is empty."

    key = generate_lcg_bytes(DEFAULT_SEED, BLOCK_SIZE)
    nonce = generate_lcg_bytes(DEFAULT_SEED + 1, BLOCK_SIZE)
    padded = pad(text.encode("utf-8"))
    cipher = encrypt_blocks(padded, key, nonce)
    return (
        f"Ciphertext (hex): {cipher.hex()}\n"
        f"Key (hex): {key.hex()}\n"
        f"Nonce (hex): {nonce.hex()}\n"
        f"Seed: {DEFAULT_SEED}"
    )

