

from helper import *
import os

fileName = 'output_file.txt'
def generate_file():
    open(fileName, 'w')
    fileSize = os.stat(fileName).st_size
    with open(fileName, 'a') as File:
        while fileSize <= 2000000:
            function_list = [random_alphanumerics, random_string, random_int, random_float]
            dataType = random.choice(function_list)
            if dataType == random_alphanumerics:
                output = random_alphanumerics()
                i = random.randint(0, 9)
                output = ' '*i + output + ' '*i
            else:
                output = dataType()
            File.write(output + ', ')
            fileSize = os.stat(fileName).st_size
        File.close()
    return fileName

def get_object_count():
    count_integers = 0
    count_real_numbers = 0
    count_alphabetical_strings = 0
    count_alphanumerics = 0
    try:
        with open(fileName) as file:
            result = file.read()
            for item in result.split(','):
                _item = item.strip()
                if is_float(_item):
                    count_real_numbers += 1
                elif is_Integer(_item):
                    count_integers += 1
                elif _item.isalpha():
                    count_alphabetical_strings += 1
                else:
                    count_alphanumerics += 1
    except ValueError:
        return ValueError
    return {'alphabetical_strings': count_alphabetical_strings, 'real_numbers': count_real_numbers, 'integers': count_integers, 'alphanumerics': count_alphanumerics}