import random
import string

characters = string.ascii_letters + string.digits
password = ''.join(random.choice(characters) for i in range(0, 8))
print("Random password:", password)
