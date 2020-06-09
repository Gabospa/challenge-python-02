# Resolve the problem!!
import string
from random import randint


SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    # Start coding here
    #selecciona longitud
    longitud = randint(8, 16) 
    password = ''   

    for i in range(longitud):
        selector = randint(0,3)
        if selector == 0:
        #seleccion de caracter lowercase
            index_char_low = randint(0, len(string.ascii_lowercase))
            char_low = string.ascii_lowercase[index_char_low -1]
            password += char_low
        elif selector == 1:
        #seleccion de caracter uppercase
            index_char_upp = randint(0, len(string.ascii_uppercase))
            char_upp = string.ascii_uppercase[index_char_upp -1]
            password += char_upp
        elif selector == 2:
        #seleccion de caracter digits
            index_char_dig = randint(0, len(string.digits))
            char_dig = string.digits[index_char_dig -1]
            password += char_dig
        else :
        #seleccion de caracter SYMBOLS
            index_char_sym = randint(0, len(SYMBOLS))
            char_sym = SYMBOLS[index_char_sym -1]
            password += char_sym
    print (password)
    return password

def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
