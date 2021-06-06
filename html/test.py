from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.adapters.abenc_adapt_hybrid import HybridABEnc
from json import dumps, loads


def main():
    group = PairingGroup('SS512')
    cp_abe = CPabe_BSW07(group)
    hyb_abe = HybridABEnc(cp_abe, group)
    (pk, msk) = hyb_abe.setup()
    pk['g'] = group.serialize(pk['g']).decode('utf-8')
    pk['g2'] = group.serialize(pk['g2']).decode('utf-8')
    pk['h'] = group.serialize(pk['h']).decode('utf-8')
    pk['f'] = group.serialize(pk['f']).decode('utf-8')
    pk['e_gg_alpha'] = group.serialize(pk['e_gg_alpha']).decode('utf-8')

    msk['beta'] = group.serialize(msk['beta']).decode('utf-8')
    msk['g2_alpha'] = group.serialize(msk['g2_alpha']).decode('utf-8')

    pk_json = dumps(pk)
    msk_json = dumps(msk)
    with open('/var/www/html/pk.json', 'wt') as fp:
        fp.write(pk_json)

    with open('/var/www/html/msk.json', 'wt') as fp:
        fp.write(msk_json)


if __name__ == "__main__":
    main()

