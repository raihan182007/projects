# import random
# import string

# val=string.ascii_letters+string.punctuation+string.digits

# pass_len=8
# password=""
# for i in range(pass_len):
#     password+=random.choice(val)
# print("Your random password :",password)

import random
import string

val = string.ascii_letters+string.digits

pass_len = 8
password = ""
for i in range(pass_len):
    password += random.choice(val)

print("Your random password is :",password)
