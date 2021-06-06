from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.adapters.abenc_adapt_hybrid import HybridABEnc
from json import dumps, loads
import sys


if __name__ == "__main__":
    filename: str = sys.argv[1]
    cfile_path: str = sys.argv[2]
    fp = open('/var/www/html/tmp_key_attr/key_attr.txt', "r")
    attr = fp.read()
    rp = open(filename, 'rb')
    msg = rp.read()
    rp.close()

    group = PairingGroup('SS512')
    cp_abe = CPabe_BSW07(group)
    hyb_abe = HybridABEnc(cp_abe, group)
    pk_fp = open('/var/www/html/pk.json', 'r')
    re_pk = loads(pk_fp.read())
    pk_fp.close()
    re_pk['g'] = group.deserialize(re_pk['g'].encode('utf-8'))
    re_pk['g2'] = group.deserialize(re_pk['g2'].encode('utf-8'))
    re_pk['h'] = group.deserialize(re_pk['h'].encode('utf-8'))
    re_pk['f'] = group.deserialize(re_pk['f'].encode('utf-8'))
    re_pk['e_gg_alpha'] = group.deserialize(re_pk['e_gg_alpha'].encode('utf-8'))

    ciphertext = hyb_abe.encrypt(re_pk, msg, attr)
    print(ciphertext)
    ciphertext["c1"]["C"] = group.serialize(ciphertext["c1"]["C"]).decode('utf-8')
    for key in ciphertext["c1"]["Cy"]:
        ciphertext["c1"]["Cy"][key] = group.serialize(ciphertext["c1"]["Cy"][key]).decode('utf-8')
    ciphertext["c1"]["C_tilde"] = group.serialize(ciphertext["c1"]["C_tilde"]).decode('utf-8')
    for key in ciphertext["c1"]["Cyp"]:
        ciphertext["c1"]["Cyp"][key] = group.serialize(ciphertext["c1"]["Cyp"][key]).decode('utf-8')

    ciphertext = dumps(ciphertext)
    with open(cfile_path, 'w') as fp:
        fp.write(ciphertext)

