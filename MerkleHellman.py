import os
import random

class MerkleHellmanAlgoritm:
    word = ""
    q = 0
    r = 0
    secretKey = [] 
    publicKey = []
    binaryInput = []
    binaryEncryptedInput = []
    binaryDecryptedOutput = []
    decryptedOutput = []
    reverseMultiplicate = 0

    def decimalToBinary(self, decimal):
        binary = ""
        while decimal > 0:
            binary = str(decimal % 2) + binary
            decimal //= 2
        while len(binary) < 7:
            binary = "0" + binary
        return binary
    
    def binaryToDecimal(self, binaryValues):
        decimals = []
        for binary in binaryValues:
            decimal = 0
            pow2Value = 1
            for i in range(len(binary) - 1, -1, -1):
                if binary[i] == '1':
                    decimal += pow2Value
                pow2Value *= 2
            decimals.append(decimal)
        return decimals

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def initSecretKey(self):
        for i in range(8):
            self.secretKey.append(2 ** i)

    def initilization_Q(self):
        self.q = random.randint(0, 100) + sum(self.secretKey)
        return self.q

    def initilization_R(self):
        self.r = random.randint(1, 100)
        while not self.is_prime(self.r):
            self.r = random.randint(1, 100)
        return self.r

    def setWord(self, withDocker = True, Word = ""):
        if withDocker:
            self.word = os.getenv("temp")
        else:
            self.word = Word
        # self.word = input("Введите данные: ")

    def getWord(self):
        return self.word

    def setBinaryInput(self):
        word = self.getWord()
        for i in range(len(word)):
            unicodeSym = ord(word[i])
            self.binaryInput.append(self.decimalToBinary(unicodeSym))

    def generatePublicKey(self):
        for c in self.secretKey:
            self.publicKey.append(c * self.r % self.q)

    def encryption(self):
        for str in self.binaryInput:
            sum = 0
            for i in range(len(str)):
                if str[i] == '1':
                    sum += self.publicKey[i]
            self.binaryEncryptedInput.append(sum)
        return self.binaryEncryptedInput

    def decryption(self):
        self.reverseMultiplicate = self.multiplicativeInverse(self.r, self.q)
        self.secretKey.sort(reverse=True)

        temp = []
        for i in self.binaryEncryptedInput:
            temp.append(i * self.reverseMultiplicate % self.q)

        for i in range(len(temp)):
            index = ""
            while temp[i] != 0:
                for c in range(len(self.secretKey)):
                    if c == 0:
                        continue
                    if temp[i] < self.secretKey[c]:
                        index += "0"
                        continue
                    else:
                        index += "1"
                        temp[i] -= self.secretKey[c]
                index = index[::-1]
                self.binaryDecryptedOutput.append(index)

        decimals = self.binaryToDecimal(self.binaryDecryptedOutput)
        self.decryptedOutput = ''.join([chr(c) for c in decimals])
        return self.decryptedOutput

    def calculateNOD(self, a, b):
        if a == 0:
            return b, 0, 1
        NOD, x1, y1 = self.calculateNOD(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return NOD, x, y

    def multiplicativeInverse(self, a, m):
        NOD, x, _ = self.calculateNOD(a, m)
        if NOD != 1:
            return -1
        else:
            return (x % m + m) % m


    def showResults(self):
        print("Q:\t\t", self.q)
        print("R:\t\t", self.r)
        print("Reverse R:':\t", self.reverseMultiplicate)
        print("secretKey:\t", self.secretKey)
        print("publicKey:\t", self.publicKey)
        print("Word: \t\t", self.getWord())
        print("Binary word:\t", self.binaryInput)
        print("Encryption:\t", self.binaryEncryptedInput)
        print("Bin string:\t", self.binaryDecryptedOutput)
        print("Decryption:\t", self.decryptedOutput)