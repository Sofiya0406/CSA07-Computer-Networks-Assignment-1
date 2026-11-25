"""Hamming(7,4) single-bit error correction."""
def encode(d):
    p1 = d[0] ^ d[1] ^ d[3]
    p2 = d[0] ^ d[2] ^ d[3]
    p3 = d[1] ^ d[2] ^ d[3]
    return [p1, p2, d[0], p3, d[1], d[2], d[3]]

def decode(c):
    s1 = c[0] ^ c[2] ^ c[4] ^ c[6]
    s2 = c[1] ^ c[2] ^ c[5] ^ c[6]
    s3 = c[3] ^ c[4] ^ c[5] ^ c[6]
    pos = s1 + 2*s2 + 4*s3
    corrected = c[:]
    if pos:
        corrected[pos - 1] ^= 1
    data = [corrected[2], corrected[4], corrected[5], corrected[6]]
    return pos, data

if __name__ == "__main__":
    word = encode([1, 0, 1, 1])
    print("codeword        :", "".join(map(str, word)))
    for flip in (None, 5):
        rx = word[:]
        if flip:
            rx[flip - 1] ^= 1
        pos, data = decode(rx)
        print(f"error at {str(flip):<4}: syndrome {pos}, data {''.join(map(str, data))}")
