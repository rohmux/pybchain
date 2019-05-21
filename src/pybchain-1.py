from bitcoin import *

my_private_key_1 = random_key()
my_private_key_2 = random_key()
my_private_key_3 = random_key()

my_public_key = privtopub(my_private_key_1)
my_btc_address = pubtoaddr(my_public_key)

my_multi_sig = mk_multisig_script(my_private_key_1, my_private_key_2, my_private_key_3, 2, 3)
my_multi_addr = scriptaddr(my_multi_sig)

print("Private Key 1: %s" % my_private_key_1)
print("Private Key 2: %s" % my_private_key_2)
print("Private Key 3: %s" % my_private_key_3)
print("\n")

print("Public Key: %s" % my_public_key)
print("BTC Address: %s" % my_btc_address)

print("Multi signature address: %s" % my_multi_addr)