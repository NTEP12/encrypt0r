import hashlib

menu_options = {
    1: 'SHA256 Encryption',
    2: 'MD5 Encryption',
    3: 'SHA1 Encryption',
    4: 'Exit',
}
def print_menu():
    banner = '''

  _   _ _______ ______ _____  __ ___  
 | \ | |__   __|  ____|  __ \/_ |__ \ 
 |  \| |  | |  | |__  | |__) || |  ) |
 | . ` |  | |  |  __| |  ___/ | | / / 
 | |\  |  | |  | |____| |     | |/ /_ 
 |_| \_|  |_|  |______|_|     |_|____|  
 
'''
    print(banner)
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

def encrypt_sha1():
    password = input('Please enter the text you want to encrypt: ')
    i = hashlib.sha1()
    password_b = bytes(password, 'utf-8')
    i.update(password_b)
    i.digest()
    key = i.hexdigest()
    print('Here is your encrypted text: ', key)

def encrypt_sha256():
    password = input('Please enter the text you want to encrypt: ')
    i = hashlib.sha256()
    password_b = bytes(password, 'utf-8')
    i.update(password_b)
    i.digest()
    key = i.hexdigest()
    print('Here is your encrypted text: ', key)

def encrypt_md5():
    password = input('Please enter the text you want to encrypt: ')
    i = hashlib.md5()
    password_b = bytes(password, 'utf-8')
    i.update(password_b)
    i.digest()
    key = i.hexdigest()
    print('Here is your encrypted text: ', key)

if __name__ == '__main__':
    while (True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number.')
        if option == 1:
            encrypt_sha256()
        elif option == 2:
            encrypt_md5()
        elif option == 3:
            encrypt_sha1()
        elif option == 4: 
            print('Thanks for using my encryption program.')
        exit()