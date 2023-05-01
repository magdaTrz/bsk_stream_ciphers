with open('test.bin', 'rb') as plik:
    address = 0
    while True:
        data = plik.read(16)
        if (not data):
            break
        if data == 0010 00002:
            print(f"dsada")
        print(f'',data.hex(' '))
        address += 16

# with open('test.bin', 'rb') as f:
#     data = f.read()

# new_data = b''
# for byte in data:
#     if byte != 0:
#         new_data += bytes([byte])
#         print(new_data.hex(' '))