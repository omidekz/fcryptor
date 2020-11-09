import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="Input File/stdin [for stdin pass -si | --stdin]", required=True)
parser.add_argument("-o", "--output", help="Output File")
parser.add_argument("-si", "--stdin", help="when stdin is true", action="store_true")
parser.add_argument("-k", "--key", help="key of/for file")
crypt_or_decryot = parser.add_mutually_exclusive_group()
crypt_or_decryot.add_argument("-c", "--crypt", action="store_true",help="Crypt File")
crypt_or_decryot.add_argument("-d", "--decrypt", action="store_true", help="Decrypt File")

args = parser.parse_args()

key = args.key or Fernet.generate_key().decode()
show_key = not bool(args.key)

fc = FCryptor(key.encode())
output = getattr(fc, "crypt" if args.crypt else "decrypt")(args.input, args.output, args.stdin)

if show_key:
    print("Key is:", key)

if not args.output:
    print ("output:")
    print(output)