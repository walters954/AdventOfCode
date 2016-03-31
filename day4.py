__author__ = 'Warren'

import hashlib

key_start = 'ckczppom'

for num in range(1000000):
    digest = hashlib.md5((key_start + str(num)).encode())
    result = digest.hexdigest()
    if result[:5] == '00000':
        print(result)
        print(key_start + str(num))

for num in range(10000000):
    digest = hashlib.md5((key_start + str(num)).encode())
    result = digest.hexdigest()
    if result[:6] == '000000':
        print(result)
        print(key_start + str(num))
