from charm.toolbox.pairinggroup import PairingGroup
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.adapters.abenc_adapt_hybrid import HybridABEnc
import pickle
from time import *
from numpy import *

filenames = ['Data1k.txt', 'Data10k.txt', 'Data100k.txt', 'Data1m.txt', 'Data10m.txt', 'Data100m.txt']

if __name__ == "__main__":
    groupObj = PairingGroup('SS512')
    cpabe = CPabe_BSW07(groupObj)
    hyb_abe = HybridABEnc(cpabe, groupObj)
    (pk, mk) = hyb_abe.setup()
    access_policy = '((four or three) and (two or one))'
    sk = hyb_abe.keygen(pk, mk, ['ONE', 'TWO', 'THREE'])
    
    ETime = []
    DTime = []

    for i in range(len(filenames)):
        enc_time = []
        dec_time = []

        for _ in range(10): # test for 10 times
            sourcefile = open(filenames[i], 'rb')
            plaintext = sourcefile.read()
            sourcefile.close()

            encryptedfile = open(filenames[i] + ".enc", 'wb')
            
            start_time = time()
            ciphertext = hyb_abe.encrypt(pk, plaintext, access_policy)
            ciphertext["c1"]["C"] = groupObj.serialize(ciphertext["c1"]["C"])
            for key in ciphertext["c1"]["Cy"] :
                ciphertext["c1"]["Cy"][key] = groupObj.serialize(ciphertext["c1"]["Cy"][key])
            ciphertext["c1"]["C_tilde"] = groupObj.serialize(ciphertext["c1"]["C_tilde"])
            for key in ciphertext["c1"]["Cyp"] :
                ciphertext["c1"]["Cyp"][key] = groupObj.serialize(ciphertext["c1"]["Cyp"][key])
            end_time = time()
            enc_time.append(end_time - start_time)    


            pickle.dump(ciphertext, encryptedfile)
            encryptedfile.close()

            encryptedfile = open(filenames[i] + ".enc", 'rb')
            ciphertext2 = pickle.load(encryptedfile)
            
            start_time = time()
            ciphertext2["c1"]["C"] = groupObj.deserialize(ciphertext2["c1"]["C"])
            for key in ciphertext2["c1"]["Cy"]:
                ciphertext2["c1"]["Cy"][key] = groupObj.deserialize(ciphertext2["c1"]["Cy"][key])
            ciphertext2["c1"]["C_tilde"] = groupObj.deserialize(ciphertext2["c1"]["C_tilde"])
            for key in ciphertext2["c1"]["Cyp"]:
                ciphertext2["c1"]["Cyp"][key] = groupObj.deserialize(ciphertext2["c1"]["Cyp"][key])
            
            recovertext = hyb_abe.decrypt(pk, sk, ciphertext2)
            end_time = time()
            dec_time.append(end_time - start_time)

            print(recovertext == plaintext)
            encryptedfile.close()

        ETime.append(mean(enc_time))
        DTime.append(mean(dec_time))
    
    print(ETime)
    print()
    print(DTime)