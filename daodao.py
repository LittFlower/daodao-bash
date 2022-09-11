#-*- coding:UTF-8 -*-
#@update:2022/9/7
#@update:2022/9/8
# TODO：提交PR

from re import S
from unittest import expectedFailure
from urllib.error import URLError
import requests
import json
import time
from datetime import date,timedelta
import os
import sys
import urllib
from colorama import init, Fore, Back, Style

init(autoreset=True)

class Colored(object):
    def red(self, s):
        return Fore.RED + s + Fore.RESET
    def green(self, s):
        return Fore.GREEN + s + Fore.RESET
    def yellow(self, s):
        return Fore.YELLOW + s + Fore.RESET
    def blue(self, s):
        return Fore.BLUE + s + Fore.RESET
    def magenta(self, s):
        return Fore.MAGENTA + s + Fore.RESET
    def cyan(self, s):
        return Fore.CYAN + s + Fore.RESET
    def white(self, s):
        return Fore.WHITE + s + Fore.RESET
    def black(self, s):
        return Fore.BLACK
    def white_green(self, s):
        return Fore.WHITE + Back.GREEN + s + Fore.RESET + Back.RESET



def helloToUser():
    print("""
    ____                  _               ____            _
    |  _ \  __ _  ___   __| | __ _  ___   | __ )  __ _ ___| |__
    | | | |/ _` |/ _ \ / _` |/ _` |/ _ \  |  _ \ / _` / __| '_ \\
    | |_| | (_| | (_) | (_| | (_| | (_) | | |_) | (_| \__ \ | | |
    |____/ \__,_|\___/ \__,_|\__,_|\___/  |____/ \__,_|___/_| |_|
    --@update:2022/9/8                      --you need python3.8+
    """)
    print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.green('INFO'),"]","Please use a bigger bash window")
    print(color.magenta('Version alpha 0.7.0     Powered by JiuLER & lamaper'))

def checkUrl(): # 检查Url可用性
    try:
        r = requests.get('https://api.c12th.eu.org/')
        if r.status_code != 200:
            return 2
    except:
        print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.red('ERROR'),"]",'Check your internet!')
        sys.exit()


    if magicFirst == True:
        return
    try:
        r1 = requests.get(url+'c=DaoDaoBash_LoginCheck'+'&k='+password)
        if r1.status_code == 200 and r1.text == 'Execution: you did not send a message today, create an issue and add a comment!':
            requests.get(url+'dn=1'+'&k='+password)
    except:
        return 2

    
def autoLogin():
    global isAutoLogin
    global magicChain
    global username
    global password
    global url

    with open('log', 'r') as logfile:
        try: 
            magicChain = logfile.read()
        except:
            print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.red('ERROR'),"]",'Check your log!')
        if magicChain == "":
            isAutoLogin == False 
        else:
            username = magicChain[:magicChain.find(chr(36))]
            password = magicChain[magicChain.find(chr(36))+1:magicChain.find(chr(38))]
            url = magicChain[magicChain.find(chr(38))+1:]
            isAutoLogin = True
        logfile.close()

def inputInfo():
    global username
    global password
    global url
    global yoururl
    global magicChain
    global isAutoLogin

    username = ""
    magicCheck = 0

    while True:
        if isAutoLogin == False:
            yoururl = input("[YourUrl]:")
            username = input("[UserName]:")
            password = input("[Password]:")
            url = f'http://{urllib.parse.urlparse(yoururl).netloc}/api/?'
            magicCheck = checkUrl()
        
        if isAutoLogin == True:
            autoLogin()

        if magicCheck == 2:
            print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.red('ERROR'),"]",'Check your url!')
            os.system("exit()")
        

        elif magicCheck != 2 and username != "" and password != "":
            with open('log', 'w') as file:
                magicChain = username + chr(36) + password + chr(38) + url
                file.write(magicChain)
                file.close()
            break

        print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.red('ERROR'),"]",'Check your internet or your password!')
        print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.red('ERROR'),"]",'If you want to exit,please press \'CTRL\'+\'C\'')

def checkIntn():
    try:
        r = requests.get('https://api.c12th.eu.org/')
        if r.status_code != 200:
            return 2
    except:
        print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.red('ERROR'),"]",'Check your internet!')
        sys.exit()

def workInWhile():
    
    global auto
    global isAutoLogin
    global magicChain
    userBash = f"[$root / @{username}]>> "
    while True:
        
        opt = input(userBash)
        # print("8798982949\n")
        if opt == 'help':
            print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.green('OPTIONS'),"]",)
            print('查询：query\n发布：commit\n删除：delete\n编辑：edit\n清屏：clear\n设置自动登录：auto')
        
        elif opt == 'query' or opt == 'q':
            checkIntn()
            id = input("The size is: ")
            r = requests.get(url+'q='+str(id))
            if r.status_code == 200:
                print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.green('STATUE'),"]",'Success!')
                ret = json.loads(r.text)
                # print(ret)
                for i in range(len(ret)):
                    now = ret[i]['date']['$date']
                    # print(now)
                
                    timeArray = time.localtime(now)
                    print("[",color.green('INFO'),"]","NO.", i + 1)
                    print("[",color.green('INFO'),"]","time:", time.strftime("%Y-%m-%d %H:%M:%S", timeArray))
                    print("[",color.green('INFO'),"]","from:", ret[i]['from'])
                    print("[",color.green('INFO'),"]","content:", ret[i]['content'])
                    print()
                
            else:
                print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.red('ERROR'),"]",'Check your internet!')
        elif opt == 'commit' or opt == 'c':
            checkIntn()
            content = input("You want to daodao >> ")
            r = requests.get(url+'c='+str(content)+'&k='+password)
            if r.status_code == 200:
                print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.green('INFO'),"]",'Success!')
                print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.green('INFO'),"]",'You have already create a new daodao!')
                # ret = r.content.decode('utf-8')
                # print(ret)
            else:
                print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.red('ERROR'),"]",'Check your internet!')
            print()
        elif opt == 'delete' or opt == 'd':
            checkIntn()
            id = input("The number you want to delete is >> ")
            r = requests.get(url+'dn='+str(id)+'&k='+password)
            if r.status_code == 200:
                # print('Success!')
                ret = r.content.decode('utf-8')
                print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.green('INFO'),"]")
                print(ret)
            else:
                print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.red('ERROR'),"]",'Check your internet!')
            print()
        elif opt == 'edit' or opt == 'e':
            checkIntn()
            id = input("The number you want to edit is >> ")
            content = input("You want to replace >> ")
            r = requests.get(url+'e='+str(id)+','+content+'&k='+password)
            if r.status_code == 200:
                ret = r.content.decode('utf-8')
                print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.green('INFO'),"]",ret)
            else:
                print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.red('ERROR'),"]",'Check your internet!')
            print()
        elif opt == 'clear':
            os.system("cls")
            print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.blue('BASH'),"]","Successfully cleared!")
        elif opt == 'exit':
            print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.blue('BASH'),"]","Successfully exited!")
            sys.exit()
        elif opt == 'auto':
            text1 = f"please input statue (Y/N),now the autoLogin is {isAutoLogin}"
            print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.green('INFO'),"]",text1)
            while True:
                oop = input(">> ")
                if oop == "Y" or oop == "y":
                    isAutoLogin = True
                    with open('log', 'w') as f:
                        # print(magicChain)
                        f.write(magicChain)
                        f.close()
                    print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.yellow('WARNING'),"]","AutoLogin statue has been changed successfully!")  
                    break          
                elif oop == "N" or oop == "n":
                    isAutoLogin = False
                    with open('log', 'w') as f:
                        f.truncate() 
                        f.close()
                    print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.yellow('WARNING'),"]","fine.")    
                    break
                else:
                    print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.red('ERROR'),"]",'Check your input!')
                    break
        # elif opt == ''
        else:
            print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.yellow('WARNING'),"]","The command \'",opt,"\' is not exist!")


if __name__ == "__main__":
    global username
    global password
    global url
    global yoururl
    global isAutoLogin
    global magicChain
    global color
    global magicFirst
    global auto


    name = ""
    password = ""
    yoururl = ""
    url = ""
    magicChain = ""
    isAutoLogin = False
    magicFirst = True


    try:
        f = open('log', 'x')
        f.close()
    except:
        pass

    color = Colored()
    helloToUser()
    autoLogin()
    checkUrl()
    
    if isAutoLogin == False:
        print(color.magenta('You Need to Login!\n'))
        print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.yellow('WARNING'),"]",color.yellow("Enter a URL related to your Daodao for operation, and you can cancel it if you want!"))
    
    magicFirst = False
    print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.yellow('WARNING'),"]","Your autoLogin is",isAutoLogin,"!")
    inputInfo()
    

    print('\n[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.green('INFO'),"]","Internet has connected successfully!")
    print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.blue('WELCOME'),"]","Let's enjoy it now!")
    print('[',time.strftime('%H:%M:%S',time.localtime()),']',"[",color.blue('WELCOME'),"]","input 'help' to know how to use it...")

    workInWhile()