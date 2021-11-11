import random
import string


def create_short_url():
    options = string.ascii_letters + string.digits
    my_list = random.sample(options, 5)
    return ''.join(my_list)
