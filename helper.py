
import operator
import random
import string

def is_float(str):
    try:
        float(str)
    except ValueError:
        return False
    return operator.not_(float(str).is_integer())

def is_Integer(n):
    try:
        float(n)
    except ValueError:
        return False
    return float(n).is_integer()

def random_alphanumerics():
    length = random.randint(5, 30)
    output = ''
    for i in range(length):
        output += random.choice(string.ascii_lowercase + string.digits)
    return output

def random_string():
    length = random.randint(5, 30)
    output = ''.join(random.choice(string.ascii_lowercase) for x in range(length))
    return output

def random_int():
    output = random.randint(0, 10000)
    intToStr = '{}'.format(output)
    return intToStr

def random_float():
    length = random.randint(1, 10)
    output = round(random.uniform(0.0, 10000.0), length)
    floatToStr = '{}'.format(output)
    return floatToStr