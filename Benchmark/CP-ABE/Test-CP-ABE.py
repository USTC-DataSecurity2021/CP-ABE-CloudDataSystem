from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from time import *
from numpy import *

def Print_Time(T_encrypt: list, T_decrypt1: list, T_decrypt2:list):
    print('Time of Encryption:')
    for _ in range(len(T_encrypt)):
        print(T_encrypt[_], end = ' ')
    print('')
    print('Average time used: ', sum(T_encrypt) / len(T_encrypt), '\n')

    print('Time of Decryption#1:')
    for _ in range(len(T_decrypt1)):
        print(T_decrypt1[_], end = ' ')
    print('')
    print('Average time used: ', sum(T_decrypt1) / len(T_decrypt1), '\n')

    print('Time of Decryption#2:')
    for _ in range(len(T_decrypt2)):
        print(T_decrypt2[_], end = ' ')
    print('')
    print('Average time used: ', sum(T_decrypt2) / len(T_decrypt2), '\n')

def Round(ATTS: list, Policy: str):
    # instantiate a bilinear pairing map
    pairing_group = PairingGroup('SS512')
    
    # CP-ABE under DLIN (2-linear)
    cpabe = CPabe_BSW07(pairing_group)

    # run the set up
    (pk, msk) = cpabe.setup()

    # generate a secret_key
    attributes = ATTS
    secret_key = cpabe.keygen(pk, msk, attributes)

    times_enc = [] # DO encrypting time
    times_dec = [] # DO decrypting time 
    Rounds = 30
    policy_str = Policy

    for _ in range(Rounds):
        # choose a random message pretend to be owner's record
        msg = pairing_group.random(GT)
    
        # generate a ciphertext
        start_time = time()
        ctxt = cpabe.encrypt(pk, msg, policy_str)
        end_time = time()
        times_enc.append(end_time - start_time)

        # decryption as Owner
        start_time = time()
        rec_msg = cpabe.decrypt(pk, secret_key, ctxt)
        end_time = time()
        times_dec.append(end_time - start_time)
        if rec_msg == msg:
            print ("Successful decryption as Owner.")
            # pass
        else:
            print ("Decryption as a Owner failed.")
    

    # Print_Time(times_enc, times_dec, times_p1)
    # print(policy_str)
    time_enc = mean(times_enc)
    time_dec = mean(times_dec)

    return (time_enc, time_dec, times_enc, times_dec)
    
def main():
    Times_enc = []
    Times_dec = []
    for i in range(5, 105, 5):
        temp = range(i)
        ATTS = []
        Policy = '('
        for j in temp:
            ATTS.append(str(j))
            Policy += 'and ' + str(j) if j != 0 else '0'
            Policy += ' '
        Policy = Policy[:-1]
        Policy += ')' # Policy == (0 and 1 and 2 and ... and n)
        # print(Policy)
        time_enc, time_dec, times_enc, times_dec = Round(ATTS, Policy)

        Times_enc.append(time_enc)
        Times_dec.append(time_dec)
    
    for time in Times_enc:
        print(time)
    print()
    for time in Times_dec:
        print(time)
    print()




if __name__ == "__main__":
    main()

