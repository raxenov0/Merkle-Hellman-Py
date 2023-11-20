import MerkleHellman
import Sha1


SHA = Sha1.SHA1()
hash = SHA.hashing("word")
print("Hash: ", hash)

MerkleHellmanInstanceClass = MerkleHellman.MerkleHellmanAlgoritm()
MerkleHellmanInstanceClass.initSecretKey()
MerkleHellmanInstanceClass.initilization_Q()
MerkleHellmanInstanceClass.initilization_R()
MerkleHellmanInstanceClass.setWord(False, hash)
MerkleHellmanInstanceClass.setBinaryInput()
MerkleHellmanInstanceClass.generatePublicKey()

MerkleHellmanInstanceClass.encryption()
MerkleHellmanInstanceClass.decryption()

MerkleHellmanInstanceClass.showResults()





#Merkle