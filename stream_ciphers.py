import random 

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
def string_to_xor(string_1, string_2):
    print("         string_to_xor():")
    binary_1 = int.from_bytes(string_1.encode(), 'big')
    binary_2 = int.from_bytes(string_2.encode(), 'big')
    print(f"         {string_1} = {binary_1}")
    print(f"         {string_2} = {binary_2}")
    xor_result = binary_1 ^ binary_2
    print(f"         xor_result = {xor_result}")
    result = xor_result.to_bytes((xor_result.bit_length() + 7) // 8, 'big').decode()
    print(f"         result = {result}")

    return result



answer= True
while answer :
    print ("""
    -------------------------------------------
    Szyfry strumieniowe

    1. Zakoduj tekst
    2. Dekoduj tekst
    3. Zamknij
    """)
    answer = input("    Co wykonać? ")
    if answer=="1" : 
        print("\n         KODOWANIE") 
        try : 
            text = str(input("         Jaki tekst chcesz zakodować? "))
            key = str(create_random_key_stream(len(text)))
            string_to_xor(text, key)
        except ValueError:
            print("Coś poszło nie tak.")
    elif answer=="2" :

        print("\n         DEKODOWANIE")
        try : 
            xor = str(input("         Podaj zakodowany wyraz? "))
            key = str(input("         Podaj kod? "))
            string_to_xor(xor, key)
        except ValueError:
            print("Coś poszło nie tak.")
    elif answer=="3" :
        print("\n Zamknięto!") 
    elif answer !="" :
        print("\n Zła opcja. ") 
