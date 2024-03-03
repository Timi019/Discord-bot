import random

def gen_pass(pass_length):
    elements = """1234567890-=qwertyuiop[]asdfghjkl;'\`zxcvbnm,./§£!@#$%^&*()_+QWERTYUIOP}{ASDFGHJKL:"|~ZXCVBNM<>?"""
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
def gen_emoji():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)


def flip_coin():
    flip = random.randint(0, 1)
    if flip == 0:
        return "HEADS"
    else:
        return "TAILS"
 