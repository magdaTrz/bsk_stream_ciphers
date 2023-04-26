import random 
import base64
from simple_colors import *

# tablica znaków która służy do generowania losowego hasła którym bedziemy kodować text
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
           't', 'u', 'v','w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# generowanie losowego hasła
def create_random_key_stream(length):
    password_str = ''
    password = []
    while len(password) != length :
        # wybieramy losowo kolejność liczby lub litery
        random_symbol = random.randint(0,1) 
        if random_symbol == 0 :
            password.append(random.choice(letters))
        if random_symbol == 1 : 
            password.append(random.choice(numbers))
    for i in password:
        password_str += i

    return password_str


# zamiana string na xor 
def encode_string_to_xor(string_1, string_2):

    binary_1 = int.from_bytes(string_1.encode(), 'big')
    binary_2 = int.from_bytes(string_2.encode(), 'big')
    xor_result = binary_1 ^ binary_2
    result = base64.b64encode(xor_result.to_bytes((xor_result.bit_length() + 7) // 8, 'big')).decode()

    print(f"\n         Pseudo losowy Klucz: {string_2}")
    print(f"         Szyfr: \033[91m{result}\033[0m")
    return result


def decode_xor_to_string(xor_result, key):
    bytes_1 = base64.b64decode(xor_result.encode())
    binary_1 = int.from_bytes(bytes_1, 'big')
    binary_2 = int.from_bytes(key.encode(), 'big')
    xor_result = binary_1 ^ binary_2
    result_bytes = xor_result.to_bytes((xor_result.bit_length() + 7) // 8, 'big')
    result = xor_result.to_bytes((xor_result.bit_length() + 7) // 8, 'big').decode()

    print(f"\n         Tekst odkodowany: \033[91m{result}\033[0m")

    return result

answer = True
while answer :
    print ("""
    ______________________________________________
    \033[1m S z y f r y  s t r u m i e n i o w e \033[0m

    1. Zakoduj tekst
    2. Dekoduj tekst
    3. Zamknij
    """)
    answer = input("    Co wykonać? ")
    if answer=="1" : 
        print("\033[1m" + "\n         KODOWANIE" + "\033[0m") 
        try : 
            text = str(input("         Jaki tekst chcesz zakodować?  \n         Tekst który chcemy zakodować:  "))
            key = str(create_random_key_stream(len(text)))
            encode_string_to_xor(text, key)
        except ValueError:
            print("\n    Kodowanie - Coś poszło nie tak.")
    elif answer=="2" :

        print("\033[1m" + "\n         DEKODOWANIE" + "\033[0m")
        try : 
            xor = str(input("         Jaki szyfr chcesz odkodować?  \n         Podaj szyfr:  "))
            key = str(input("         Podaj klucz:  "))
            decode_xor_to_string(xor, key)
        except ValueError:
            print("\n    Dekodowanie - Coś poszło nie tak.")
    elif answer=="3" :
        print("\n    Zamknięto!")
        answer = False 
    elif answer !="" :
        print("\n    Zła opcja. ") 
