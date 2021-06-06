from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.adapters.abenc_adapt_hybrid import HybridABEnc
from json import dumps, loads
import sys
import hashlib


def do_sk(attributes: list):
    group = PairingGroup('SS512')
    cp_abe = CPabe_BSW07(group)
    hyb_abe = HybridABEnc(cp_abe, group)
    pk_fp = open('/var/www/html/pk.json', 'r')
    r_pk = pk_fp.read()
    re_pk = loads(r_pk)
    pk_fp.close()
    re_pk['g'] = group.deserialize(re_pk['g'].encode('utf-8'))
    re_pk['g2'] = group.deserialize(re_pk['g2'].encode('utf-8'))
    re_pk['h'] = group.deserialize(re_pk['h'].encode('utf-8'))
    re_pk['f'] = group.deserialize(re_pk['f'].encode('utf-8'))
    re_pk['e_gg_alpha'] = group.deserialize(re_pk['e_gg_alpha'].encode('utf-8'))

    sk_fp = open('/var/www/html/msk.json', 'r')
    r_msk = sk_fp.read()
    msk = loads(r_msk)
    sk_fp.close()
    msk['beta'] = group.deserialize(msk['beta'].encode('utf-8'))
    msk['g2_alpha'] = group.deserialize(msk['g2_alpha'].encode('utf-8'))

    usk = hyb_abe.keygen(re_pk, msk, attributes)
    usk['D'] = group.serialize(usk['D']).decode('utf-8')
    for i in usk['Dj']:
        usk['Dj'][i] = group.serialize(usk['Dj'][i]).decode('utf-8')

    for j in usk['Djp']:
        usk['Djp'][j] = group.serialize(usk['Djp'][j]).decode('utf-8')

    usk = dumps(usk)
    return usk, r_pk


school: str = sys.argv[1]
username: str = sys.argv[2]
identity: str = sys.argv[3]

rp = open('/var/www/html/uid.txt', 'r')
uid = rp.read()
rp.close()

data = school+username+identity+uid
re_id = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
attr = [school, username, identity, re_id]
wp = open('/var/www/html/uid.txt', 'w')
wp.write(str(int(uid)+1))
wp.close()

(sk, pk) = do_sk(attr)
print(sk)
print(pk)
print(re_id)

