

from helper import *
import os

def generate_file():
    fileName = 'output_file.txt'
    open(fileName, 'w')
    fileSize = os.stat(fileName).st_size
    with open(fileName, 'a') as File:
        while fileSize <= 2000000:
            function_list = [random_alphanumerics, random_string, random_int, random_float]
            dataType = random.choice(function_list)
            if dataType == random_alphanumerics: # our alphanumeric string needs to have whitespaces before and after it so let's use an if statement for that
                output = random_alphanumerics()
                i = random.randint(0, 9) # the whitespaces shouldn't be more than 9
                output = ' '*i + output + ' '*i # put them altogether
            else:
                output = dataType()
            File.write(output + ', ')
            fileSize = os.stat(fileName).st_size
            print(fileSize)
        print('Final file size:', fileSize / 1000000, 'MB')
        File.close()
    return fileName

def get_object_count():
    count_integers = 0
    count_real_numbers = 0
    count_alphabetical_strings = 0
    count_alphanumerics = 0
    try:
        file = open('output_file.txt')
        result = file.read()
        file.close()
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