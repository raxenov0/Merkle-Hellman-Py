import struct

class SHA1:

    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476
    E = 0xC3D2E1F0

    def left_rotate(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xffffffff
    
    def hashing(self, message):
        message = message.encode('utf-8')
        padding = chr(128) + chr(0) * (55 - len(message) % 64)
        if len(message) % 64 > 55:
            padding += chr(0) * (64 + 55 - len(message) % 64)
            message = message + padding + struct.pack('>Q', 8 * len(message))

        for i in range(0, len(message), 64): #размер блока 64 бит
            w = [0] * 80 #пустой список на 80 символов
            for j in range(16):
                w[j] = struct.unpack('>I', message[i+j*4 : i+j*4+4])[0] #определяем число из 4 байт
            for j in range(16, 80):
                w[j] = self.left_rotate(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1)

        a = self.A
        b = self.B
        c = self.C
        d = self.D
        e = self.E

        for j in range(80):
            if j <= 19:
                f = (b & c) | (~b & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = self.left_rotate(a, 5) + f + w[j] + k & 0xffffffff
            e = d
            d = c
            c = self.left_rotate(b, 30)
            b = a
            a = temp

        self.A = self.A + a & 0xffffffff
        self.B = self.B + b & 0xffffffff
        self.C = self.C + c & 0xffffffff
        self.D = self.D + d & 0xffffffff
        self.E = self.E + e & 0xffffffff

        return '%08x%08x%08x%08x%08x' % (self.A, self.B, self.C, self.D, self.E)
