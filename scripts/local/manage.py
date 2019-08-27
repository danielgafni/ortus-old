import os
from base64 import urlsafe_b64encode
from uuid import uuid4
from json import dumps, loads
from shutil import rmtree
from hashlib import new
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Core:
    def __init__(self):
        self.path = os.path.abspath(r'..')
        if not os.path.exists(f'{self.path}//data//appdata'):
            os.makedirs(f'{self.path}//data//appdata')
        if not os.path.exists(f'{self.path}//data//users'):
            os.makedirs(f'{self.path}//data//users')

        self.default_user = User('default', 'default', '')

        self.passwords = {}
        self.logged = False
        self.user = self.default_user
        self.auto_save = True
        self.logmessage = f'Welcome to Ortus!\nProgram is running at {self.path}'

    def load_passwords(self, path=None):
        if self.logged:
            self.log('loading passwords')
            if path is None:
                path = f'{self.path}\\data\\users\\{self.user.userfoldername}'
            self.passwords = load_dict(path, 'passwords', self.user.username + self.user.master_password)
        else:
            self.log('You have to log in before loading passwords!')

    def save_passwords(self, path=None, method='encrypt'):
        if self.logged:
            if path is None:
                path = f'{self.path}\\data\\users\\{self.user.userfoldername}'
            save_dict(self.passwords, path, 'passwords', self.user.username + self.user.master_password,
                          method=method)
        else:
            self.log('You have to log in before saving passwords!')

    def add_password(self, keyword, length=20, log=True, method='generated'):
        if self.logged:
            self.log('adding password')
            if method == 'generated':
                password = encrypt(keyword, self.user.username + self.user.master_password)[-length-2:-2]
            if method == 'given':
                password = keyword
            self.passwords[keyword] = password
            if log:
                self.log(f'Password for {keyword}: {password}')
            return password

    def get_password(self, keyword, log=True):
        if self.logged:
            if log:
                self.log('getting password')
                self.log(f'Password for {keyword}: {self.passwords[keyword]}')
            return self.passwords[keyword]
        else:
            self.log('You have to log in before getting passwords!')

    def delete_password(self, keyword, log=True):
        if self.logged:
            if log:
                self.log('deleting password')
            self.passwords.pop(keyword)
        else:
            self.log('You have to log in before deleting passwords!')

    def show_passwords(self):
        if self.logged:
            self.log('showing passwords')
            for keyword in self.passwords.keys():
                self.log(f'Password for {keyword} is {self.get_password(keyword, log=False)}')
        else:
            self.log('You have to log in before showing passwords!')

    #def register_user(self, username, master_password, email):
    #    if not self.logged:
    #        self.log('registering user')
    #        user = User(username, master_password, email)
    #        userfoldername = user.userfoldername
    #        users = load_dict(f'{self.path}//data//appdata', 'registered_users')
    #        users[userfoldername] = True
    #        save_dict(users, f'{self.path}//data//appdata', 'registered_users')
    #        self.logged = True
    #        self.user = user
    #        self.save_user(user)
    #    else:
    #        self.log('You have to be logged out to register a new user!')

    def register_user_temporary(self, username, master_password):
        email = 'TEMPORARY'
        if not self.logged:
            registered, userfoldername = self.check_registration(username)
            if not registered:
                self.log('registering user')
                user = User(username, master_password, email)
                userfoldername = user.userfoldername
                users = load_dict(f'{self.path}//data//appdata', 'registered_users')
                users[userfoldername] = True
                save_dict(users, f'{self.path}//data//appdata', 'registered_users')
                self.logged = True
                self.user = user
                self.save_user(user)
                self.log(f'User {username} successfully registered!')
                self.log(f'Master password for {username} is {master_password}.')
            else:
                self.log(f'User {username} is already registered!')
        else:
            self.log('You have to be logged out to register a new user!')

    def load_user(self, username, master_password):
        if not self.logged:
            self.log('loading user')
            registered, userfoldername = self.check_registration(username)
            info = load_dict(f'{self.path}//data//users//{userfoldername}', 'info')
            user = User(username, master_password)
            user.master_password_hash = info['master_password_hash']
            user.email = info['email']
            user.data = {
                'username': user.username,
                'master_password_hash': user.master_password_hash,
                'email': user.email,
                'userfoldername': userfoldername
                }
            user.userfoldername = userfoldername
            return user
        else:
            self.log('You have to log out before loading users!')

    def save_user(self, user=None):
        if user is None:
            user = self.user
        if self.logged:
            self.log('saving user')
            dict_to_save = {'username': user.username,
                            'master_password_hash': user.master_password_hash,
                            'email': user.email,
                            'userfoldername': user.userfoldername}
            save_dict(dict_to_save, f'{self.path}//data//users//{user.userfoldername}', 'info')
        else:
            self.log('You have to log in before saving users!')

    def remove_current_user(self):
        if self.logged:
            self.log('deleting user')
            users = load_dict(f'{self.path}//data//appdata', 'registered_users')
            users.pop(self.user.userfoldername)
            save_dict(users, f'{self.path}//data//appdata', 'registered_users')
            rmtree(f'{self.path}//data//users//{self.user.userfoldername}')
            self.log(f'User {self.user.username} is successfully deleted!')
            self.logout()
        else:
            self.log('You have to log in before deleting users!')

    def check_registration(self, username):
        self.log('checking registration')
        users = load_dict(f'{self.path}//data//appdata', 'registered_users')
        if users is None:
            self.log('User not found...')
            return False, ''
        for key in users.keys():
            if check_hash(username, key):
                self.log(f'User {username} is registered.')
                return True, key
        return False, ''

    def login(self, username, master_password):
        if not self.logged:
            registered, userfoldername = self.check_registration(username)
            info = load_dict(f'{self.path}//data//users//{userfoldername}', 'info')
            if info != {} and info is not None:
                if not check_hash(master_password, info['master_password_hash']):
                    self.log('Incorrect password. Try again...')
                else:
                    self.log('Successfully logged in!')
                    self.user = self.load_user(username, master_password)
                    self.logged = True
                    self.load_passwords()
            else:
                self.log(f'User {username} does not exist!')
                self.logged = False
        else:
            self.log('You must log out before logging in!')

    def logout(self):
        self.passwords = {}
        self.logged = False
        self.user = self.default_user
        self.logmessage = f'Welcome to Ortus!\nProgram is running at {self.path}'

    def auto_save_behavior(self, ans=True):
        self.auto_save = ans

    def log(self, message):
        self.logmessage += '\n' + str(message)
        print(message)

    def exit(self):
        self.log('Bye!')
        self.logmessage = ''


class User:
    def __init__(self, username='username', master_password='password', email='username@mail.com'):
        self.userfoldername = salted_hash(username)
        self.master_password = master_password
        self.username = username
        self.email = email
        self.master_password_hash = salted_hash(master_password)
        self.data = {
            'username': self.username,
            'master_password_hash': self.master_password_hash,
            'email': self.email,
            'userfoldername': self.userfoldername
            }


def error():
    print('Oops! Something went wrong:\n')


def encrypt(word, keyword):
    key = bytes(keyword, 'utf8')
    salt = bytes()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
        )
    key_for_fernet = urlsafe_b64encode(kdf.derive(key))
    fernet = Fernet(key_for_fernet)
    return fernet.encrypt(bytes(word, 'utf8')).decode('utf8')


def decrypt(word_encrypted, keyword):
    key = bytes(keyword, 'utf8')
    salt = bytes()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
        )
    key_for_fernet = urlsafe_b64encode(kdf.derive(key))
    fernet = Fernet(key_for_fernet)
    return fernet.decrypt(word_encrypted).decode('utf8')


def save_dict(data, path, dict_file_name, keyword=None, method='encrypt'):
    if not os.path.exists(path):
        os.makedirs(path)
    if keyword is None:
        keyword = 'rofl'
    if method == 'encrypt':
        json_string_to_save = encrypt(dumps(data), keyword)
    else:
        json_string_to_save = dumps(data)
    with open(f'{path}//{dict_file_name}', 'w') as file:
        file.write(json_string_to_save)
        file.close()


def load_dict(path, dict_file_name, keyword=None):
    try:
        if not os.path.exists(f'{path}//{dict_file_name}'):
            return {}
        if keyword is None:
            keyword = 'rofl'
        with open(f'{path}//{dict_file_name}', 'r') as file:
            json_string = decrypt(file.read().encode('utf8'), keyword)
            file.close()
        return loads(json_string)
    except:
        return None



def salted_hash(word, method='whirlpool', n=10):
    salt = uuid4().hex
    h = new(method, bytes(word, encoding='utf8'))
    h.update(bytes(salt, 'utf8'))
    if method == 'shake_128':
        true_hash = h.hexdigest(n)
        return true_hash + '_' + str(salt) + '_' + str(n)
    else:
        true_hash = h.hexdigest()
        return true_hash + '_' + str(salt)


def check_hash(word, salted_hash, method='whirlpool'):
    args = salted_hash.split('_')
    true_hash, salt = args[0], args[1]
    h = new(method, bytes(word, encoding='utf8'))
    h.update(bytes(salt, 'utf8'))
    if method != 'shake_128':
        if h.hexdigest() == true_hash:
            return True
        else:
            return False
    else:
        n = int(args[2])
        if h.hexdigest(n) == true_hash:
            return True
        else:
            return False


if __name__ == '__main__':
    print('You are not supposed to run this... get out!')
