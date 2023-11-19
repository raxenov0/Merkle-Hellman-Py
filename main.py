import MerkleHellman
import Sha1

MerkleHellmanInstanceClass = MerkleHellman.MerkleHellmanAlgoritm()
MerkleHellmanInstanceClass.initSecretKey()
MerkleHellmanInstanceClass.initilization_Q()
MerkleHellmanInstanceClass.initilization_R()
MerkleHellmanInstanceClass.setWord()
MerkleHellmanInstanceClass.setBinaryInput()
MerkleHellmanInstanceClass.generatePublicKey()

MerkleHellmanInstanceClass.encryption()
MerkleHellmanInstanceClass.decryption()

MerkleHellmanInstanceClass.showResults()

SHA = Sha1.SHA1()
word = input("Ввод слова: ")
hash = SHA.hashing(word)
print(hash)


#Merkle