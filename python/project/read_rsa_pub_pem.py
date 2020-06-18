
#!/usr/bin/env python3
# 1. arg parser
# 2. defining the main attribute for executable py
# 3. using array library
# 4. with as keyword to simplify the code
# 5. RSA crypto library

def get_args():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--key', required=True,
	help='Public key PEM file')
    parser.add_argument(
	'--outfile', required=True,
	help='Output file for key binary data')
    return parser.parse_args()


def main():
    import array
    from Crypto.PublicKey import RSA
    from Crypto.Util.number import long_to_bytes

    print('read_rsa_pub_pem')

    # get the command line arguments with the py
    args = get_args()

    with open(args.key, 'r') as f:
        pubkey = RSA.import_key(f.read())

    modlen=0
    for i in array.array('B', long_to_bytes(pubkey.n)):
        modlen += 1

    # Error if key is not 2048 bit length
    if modlen is not 256:
        print('ERROR: Key size is not 2048 !!!')
        return

    with open(args.outfile, 'wb') as f:
        f.write(modlen.to_bytes(4, byteorder='little'))
        f.write(array.array('B', long_to_bytes(pubkey.n)))
        f.write(pubkey.e.to_bytes(4, byteorder='little'))

    print('DONE...')
    quit()


if __name__ == "__main__":
    main()
