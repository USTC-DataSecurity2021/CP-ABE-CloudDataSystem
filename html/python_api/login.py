# find is the username and password is true or wrong
import sys
import base64

username: str = sys.argv[1]
password: str = sys.argv[2]

with open('/var/www/html/users/'+username, 'r') as fp:
    con = fp.read()
    con = con.split('\n')
    password = base64.encodebytes(bytes(password.encode('utf-8'))).decode('utf-8')
    if con[1] != password:
        print(password)
