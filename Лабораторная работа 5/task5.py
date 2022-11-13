import random
import string

def get_random_password(password_size) -> str:
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits
    i = random.randrange(password_size, len(alphabet), 1)
    password = "".join(random.sample(alphabet, i))
    return password

password_result = get_random_password(8)


print(password_result)
