from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.adapters.abenc_adapt_hybrid import HybridABEnc
from json import dumps, loads
import sys

pk_path = 'your pk path'
sk_path = 'your sk path'

if __name__ == "__main__":
    filename: str = sys.argv[1]

    rp = open(filename, 'rb')
    cipher = loads(rp.read())
    rp.close()

    group = PairingGroup('SS512')
    cp_abe = CPabe_BSW07(group)
    hyb_abe = HybridABEnc(cp_abe, group)

    cipher["c1"]["C"] = group.deserialize(cipher["c1"]["C"].encode('utf-8'))
    for key in cipher["c1"]["Cy"]:
        cipher["c1"]["Cy"][key] = group.deserialize(cipher["c1"]["Cy"][key].encode('utf-8'))
    cipher["c1"]["C_tilde"] = group.deserialize(cipher["c1"]["C_tilde"].encode('utf-8'))
    for key in cipher["c1"]["Cyp"]:
        cipher["c1"]["Cyp"][key] = group.deserialize(cipher["c1"]["Cyp"][key].encode('utf-8'))

    print(cipher)
    pk_fp = open(pk_path, 'r')
    re_pk = loads(pk_fp.read())
    pk_fp.close()
    re_pk['g'] = group.deserialize(re_pk['g'].encode('utf-8'))
    re_pk['g2'] = group.deserialize(re_pk['g2'].encode('utf-8'))
    re_pk['h'] = group.deserialize(re_pk['h'].encode('utf-8'))
    re_pk['f'] = group.deserialize(re_pk['f'].encode('utf-8'))
    re_pk['e_gg_alpha'] = group.deserialize(re_pk['e_gg_alpha'].encode('utf-8'))

    sk_fp = open(sk_path, 'r')
    sk = loads(sk_fp.read())
    sk_fp.close()
    sk['D'] = group.deserialize(sk['D'].encode('utf-8'))
    for i in sk['Dj']:
        sk['Dj'][i] = group.deserialize(sk['Dj'][i].encode('utf-8'))

    for j in sk['Djp']:
        sk['Djp'][j] = group.deserialize(sk['Djp'][j].encode('utf-8'))

    msg = hyb_abe.decrypt(re_pk, sk, cipher)
    print(msg.decode('utf-8'))

