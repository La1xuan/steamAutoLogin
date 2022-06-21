import os
import json
import pyautogui


try:
    f = open("LoginInfo.json","r")
    temp = f.read(99999)
    loginInfo = json.loads(temp)
    f.close()
except:
    loginInfo = [[],[]]
loginInfo[0].append("Add")
res = pyautogui.confirm(text="Which to Login?", buttons=loginInfo[0])
if res == "Add":
    loginInfo[0][-1] = pyautogui.prompt(text="Username")
    loginInfo[1].append(pyautogui.prompt(text="Password"))
    temp = json.dumps(loginInfo)
    
    f = open("LoginInfo.json","w+")
    f.write(temp)
    f.close()
    exit()

f.close()
ind = loginInfo[0].index(res)
os.popen("steam.exe -login " + loginInfo[0][ind] + " " + loginInfo[1][ind])
exit()

