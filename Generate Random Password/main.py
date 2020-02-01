import random
import string


def randomPassword(pswdlen=10):
    letter = string.ascii_lowercase

    return ' '.join(random.choice(letter) for i in range(pswdlen))


print(randomPassword())
print(randomPassword())
print(randomPassword())
