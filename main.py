import MerkleHellman
import Sha1


SHA = Sha1.SHA1()
hash = SHA.hashing("word")
print("Hash: ", hash)

MerkleHellmanInstanceClass = MerkleHellman.MerkleHellmanAlgoritm()
#задать размер ключа
keyLength = input("Введите размер ключа: ")

MerkleHellmanInstanceClass.initSecretKey(keyLength)
MerkleHellmanInstanceClass.initilization_Q()
MerkleHellmanInstanceClass.initilization_R()
MerkleHellmanInstanceClass.setWord(False, hash)
MerkleHellmanInstanceClass.setBinaryInput()
MerkleHellmanInstanceClass.generatePublicKey()

MerkleHellmanInstanceClass.encryption()
MerkleHellmanInstanceClass.decryption()

MerkleHellmanInstanceClass.showResults()
