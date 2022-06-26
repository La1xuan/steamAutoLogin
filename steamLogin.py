from hashlib import sha256
#import os
from os import popen, mkdir
#import json
from json import dumps, loads
#import random
from random import randint
#import pyautogui
from pyautogui import prompt, confirm
from cryptography.fernet import Fernet


def finalize():
    temp = dumps(loginInfo)
    f = open("LoginInfo.json","w+")
    f.write(temp)
    f.close()
    return
    
def main(psw):
    f = open("keyStoring/" + str(sha256(psw.encode()).hexdigest()),"r")
    key = f.read(99).encode()
    #f.write(str(Fernet.generate_key()))
    f.close()
    loginInfo[0].append("Modifying")
    res = confirm(text="Which to Login?", buttons=loginInfo[0])
    
    fernet = Fernet(key)
    if res == "Modifying":
        res = confirm(text="Choose your move", buttons=["Add", "Change Username", "Change Password", "Delete Account"])
        if res == "Add":
            loginInfo[0][-1] = prompt(text="Username")
            password = prompt(text="Password")
            loginInfo[1].append(fernet.encrypt(password.encode()).decode("utf-8"))
            finalize()
            return
        if res == "Change Username":
            loginInfo[0].pop()
            res = confirm(text="Which account to change?", buttons=loginInfo[0])
            ind = loginInfo[0].index(res)

            loginInfo[0][ind] = prompt(text="new username")
            finalize()
            return
        if res == "Change Password":
            loginInfo[0].pop()
            res = confirm(text="Which account to change?", buttons=loginInfo[0])
            ind = loginInfo[0].index(res)

            password = prompt(text="new password")
            loginInfo[1][ind] = (fernet.encrypt(password.encode()).decode("utf-8"))
            finalize()
            return
        if res == "Delete Account":
            loginInfo[0].pop()
            res = confirm(text="Which account to delete?", buttons=loginInfo[0])
            ind = loginInfo[0].index(res)

            loginInfo[0].pop(ind)
            loginInfo[1].pop(ind)
            finalize()
            return

    f.close()
    ind = loginInfo[0].index(res)
    print("Encrypted: " + loginInfo[0][ind] + " " + loginInfo[1][ind])
    print("Decrypted: " + loginInfo[0][ind] + " " + fernet.decrypt(loginInfo[1][ind].encode()).decode())
    popen("steam.exe -login " + loginInfo[0][ind] + " " + fernet.decrypt(loginInfo[1][ind].encode()).decode())
    return


def setup(psw):
    try:
        mkdir("keyStoring")
    except:
        print()
    for _ in range(50000):
        f = open("keyStoring/" + str(sha256(str(randint(randint(100000), randint(100000) + 100000)).encode()).hexdigest()),"w+")
        f.write(Fernet.generate_key().decode())
        f.close()
    #psw = pyautogui.prompt("Enter your password")
    f = open("keyStoring/" + str(sha256(psw.encode()).hexdigest()),"w+")
    f.write(Fernet.generate_key().decode())
    f.close()
  
def setup2(psw):
    try:
        mkdir("keyStoring")
    except:
        print()
    #psw = pyautogui.prompt("Enter your password")
    f = open("keyStoring/" + str(sha256(psw.encode()).hexdigest()),"w+")
    f.write(Fernet.generate_key().decode())
    f.close()

password = prompt("Enter your password")

try:
    f = open("LoginInfo.json","r")
    temp = f.read(99999)
    loginInfo = loads(temp)
    f.close()

except:
    loginInfo = [[],[],sha256(sha256(password.encode()).hexdigest().encode()).hexdigest()]
    #setup(password)
    setup2(password)
    finalize()

if (sha256(sha256(password.encode()).hexdigest().encode()).hexdigest() == loginInfo[2]):
    main(password)
