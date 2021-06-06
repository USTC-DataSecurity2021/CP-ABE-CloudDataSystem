# produce the secret key and handle the dic of users
import string
import sys
import base64

username: str = sys.argv[1]
password: str = sys.argv[2]
OK = 0
letter_list = string.ascii_letters + string.digits
if len(username) > 10:
    OK = 1

for i in username:
    if i not in letter_list:
        OK = 2
        break

pass_list_1 = string.ascii_uppercase
pass_list_2 = string.ascii_lowercase
pass_list_3 = string.digits
pass_list_4 = string.punctuation
pass_list = [0, 0, 0, 0]
for i in password:
    if i in pass_list_1:
        pass_list[0] = 1

    elif i in pass_list_2:
        pass_list[1] = 1

    elif i in pass_list_3:
        pass_list[2] = 1

    elif i in pass_list_4:
        pass_list[3] = 1

    else:
        OK = 3

pass_check = 0
for i in pass_list:
    pass_check += i

if pass_check < 3:
    OK = 4

if OK == 0:
    fp = open('/var/www/html/users/' + username, 'w')
    username = base64.encodebytes(bytes(username.encode('utf-8'))).decode('utf-8')
    password = base64.encodebytes(bytes(password.encode('utf-8'))).decode('utf-8')
    fp.write(username + '\n' + password + '\n')
    print("success")

elif OK == 1:
    print('username too long')

elif OK == 2:
    print('only letters and digits allowed in username')

elif OK == 3:
    print('only printable allowed in password')

elif OK == 4:
    print('password must include 3 of the 4 kinds(uppercase, lowercase, digits, punctuation)')
