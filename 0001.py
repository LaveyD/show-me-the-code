from random import choice
from functools import partial

def generate (time = 200, length = 8):
    return [''.join(choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length)) for _ in range(time)]

gen = partial(generate, length = 10)
print(gen())