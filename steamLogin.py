import os
import json
import pyautogui
from cryptography.fernet import Fernet


def finalize():
    temp = json.dumps(loginInfo)
    f = open("LoginInfo.json","w+")
    f.write(temp)
    f.close()
    quit()

try:
    f = open("LoginInfo.json","r")
    temp = f.read(99999)
    loginInfo = json.loads(temp)
    f.close()
except:
    loginInfo = [[],[]]
loginInfo[0].append("Modifying")
res = pyautogui.confirm(text="Which to Login?", buttons=loginInfo[0])
key = b'K2aBpbOdh0pbpMTht24sxJKuZtcfwVOUw7dD1aGJCu8='
fernet = Fernet(key)
if res == "Modifying":
    res = pyautogui.confirm(text="Choose your move", buttons=["Add", "Change Username", "Change Password", "Delete Account"])
    if res == "Add":
        loginInfo[0][-1] = pyautogui.prompt(text="Username")
        password = pyautogui.prompt(text="Password")
        loginInfo[1].append(fernet.encrypt(password.encode()).decode("utf-8"))
        finalize()
    if res == "Change Username":
        loginInfo[0].pop()
        res = pyautogui.confirm(text="Which account to change?", buttons=loginInfo[0])
        ind = loginInfo[0].index(res)

        loginInfo[0][ind] = pyautogui.prompt(text="new username")
        finalize()
    if res == "Change Password":
        loginInfo[0].pop()
        res = pyautogui.confirm(text="Which account to change?", buttons=loginInfo[0])
        ind = loginInfo[0].index(res)

        password = pyautogui.prompt(text="new password")
        loginInfo[1][ind] = (fernet.encrypt(password.encode()).decode("utf-8"))
        finalize()
    if res == "Delete Account":
        loginInfo[0].pop()
        res = pyautogui.confirm(text="Which account to delete?", buttons=loginInfo[0])
        ind = loginInfo[0].index(res)

        loginInfo[0].pop(ind)
        loginInfo[1].pop(ind)
        finalize()

f.close()
ind = loginInfo[0].index(res)
#print("Encrypted: " + loginInfo[0][ind] + " " + loginInfo[1][ind])
#print("Decrypted: " + loginInfo[0][ind] + " " + fernet.decrypt(loginInfo[1][ind].encode()).decode())
os.popen("steam.exe -login " + loginInfo[0][ind] + " " + fernet.decrypt(loginInfo[1][ind].encode()).decode())
quit()
