import MerkleHellman
import Sha1


SHA = Sha1.SHA1()
hash = SHA.hashing("wordPass")
print("Hash: ", hash)

MerkleHellmanInstanceClass = MerkleHellman.MerkleHellmanAlgoritm()
MerkleHellmanInstanceClass.initSecretKey(8)
MerkleHellmanInstanceClass.initilization_Q()
MerkleHellmanInstanceClass.initilization_R()
MerkleHellmanInstanceClass.setWord(False, hash)
MerkleHellmanInstanceClass.setBinaryInput()
MerkleHellmanInstanceClass.generatePublicKey()

MerkleHellmanInstanceClass.encryption()
MerkleHellmanInstanceClass.decryption()

MerkleHellmanInstanceClass.showResults()





#Merkle