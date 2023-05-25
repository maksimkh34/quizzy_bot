import random
import string

letters = string.ascii_letters
digits = string.digits
special_chars = list(string.punctuation)
special_chars.remove('-')
special_chars = ''.join(special_chars)

#  id: AAAA000-XXXXXX-000000
#  where:
#       A - any letter
#       0 - any number or letter
#       X - any symbol


def generate_id(taken_ids):
    id_ = ''.join([random.choice(letters) for _ in range(3)]) + \
        ''.join([random.choice(digits) for _ in range(3)]) + '-' + \
        ''.join([random.choice(letters + digits + special_chars) for _ in range(3)]) + '-' + \
        ''.join([random.choice(digits) for _ in range(6)])
    if id_ not in taken_ids:
        return id_
    else:
        return generate_id(taken_ids)
