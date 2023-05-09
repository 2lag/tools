import requests
import time

def getmethod(methodchoice, url):
    if methodchoice == "1":
        cookies = input("\ninput cookies: ")
        r = requests.get(url, cookies=cookies)
        print("solo user request : " + str(r.status_code))
    elif methodchoice == "2":
        cookies = input("\ninput 1st cookies: ")
        cookies2 = input("\ninput 2nd cookies: ")
        r = requests.get(url, cookies=cookies)
        r2 = requests.get(url, cookies=cookies2)
        print("1st user request : " + str(r.status_code))
        print("2nd user request : " + str(r2.status_code))
    elif methodchoice == "3":
        r = requests.get(url)
        print("unauthenticated request : " + str(r.status_code))
    elif methodchoice == "4":
        cookies = input("\ninput cookies: ")
        cookies2 = input("\ninput 2nd cookies: ")
        r = requests.get(url, cookies=cookies)
        r2 = requests.get(url, cookies=cookies2)
        r3 = requests.get(url)
        print("1st user request : " + str(r.status_code))
        print("2nd user request : " + str(r2.status_code))
        print("unauthenticated request : " + str(r3.status_code))

def postmethod(methodchoice, url):
    if methodchoice == "1":
        cookies = input("\ninput cookies: ")
        r = requests.post(url, cookies=cookies)
        print("solo user request : " + str(r.status_code))
    elif methodchoice == "2":
        cookies = input("\ninput 1st cookies: ")
        cookies2 = input("\ninput 2nd cookies: ")
        r = requests.post(url, cookies=cookies)
        r2 = requests.post(url, cookies=cookies2)
        print("1st user request : " + str(r.status_code))
        print("2nd user request : " + str(r2.status_code))
    elif methodchoice == "3":
        r = requests.post(url)
        print("unauthenticated request : " + str(r.status_code))
    elif methodchoice == "4":
        cookies = input("\ninput cookies: ")
        cookies2 = input("\ninput 2nd cookies: ")
        r = requests.post(url, cookies=cookies)
        r2 = requests.post(url, cookies=cookies2)
        r3 = requests.post(url)
        print("1st user request : " + str(r.status_code))
        print("2nd user request : " + str(r2.status_code))
        print("unauthenticated request : " + str(r3.status_code))

def putmethod(methodchoice, url):
    if methodchoice == "1":
        cookies = input("\ninput cookies: ")
        r = requests.put(url, cookies=cookies)
        print("solo user request : " + str(r.status_code))
    elif methodchoice == "2":
        cookies = input("\ninput 1st cookies: ")
        cookies2 = input("\ninput 2nd cookies: ")
        r = requests.put(url, cookies=cookies)
        r2 = requests.put(url, cookies=cookies2)
        print("1st user request : " + str(r.status_code))
        print("2nd user request : " + str(r2.status_code))
    elif methodchoice == "3":
        r = requests.put(url)
        print("unauthenticated request : " + str(r.status_code))
    elif methodchoice == "4":
        cookies = input("\ninput cookies: ")
        cookies2 = input("\ninput 2nd cookies: ")
        r = requests.put(url, cookies=cookies)
        r2 = requests.put(url, cookies=cookies2)
        r3 = requests.put(url)
        print("1st user request : " + str(r.status_code))
        print("2nd user request : " + str(r2.status_code))
        print("unauthenticated request : " + str(r3.status_code))

def deletemethod(methodchoice, url):
    if methodchoice == "1":
        cookies = input("\ninput cookies: ")
        r = requests.delete(url, cookies=cookies)
        print("solo user request : " + str(r.status_code))
    elif methodchoice == "2":
        cookies = input("\ninput 1st cookies: ")
        cookies2 = input("\ninput 2nd cookies: ")
        r = requests.delete(url, cookies=cookies)
        r2 = requests.delete(url, cookies=cookies2)
        print("1st user request : " + str(r.status_code))
        print("2nd user request : " + str(r2.status_code))
    elif methodchoice == "3":
        r = requests.delete(url)
        print("unauthenticated request : " + str(r.status_code))
    elif methodchoice == "4":
        cookies = input("\ninput cookies: ")
        cookies2 = input("\ninput 2nd cookies: ")
        r = requests.delete(url, cookies=cookies)
        r2 = requests.delete(url, cookies=cookies2)
        r3 = requests.delete(url)
        print("1st user request : " + str(r.status_code))
        print("2nd user request : " + str(r2.status_code))
        print("unauthenticated request : " + str(r3.status_code))

def method1thru3(methodchoice, url):
    if methodchoice == "1":
        cookies = input("\ninput cookies: ")
        r = requests.get(url, cookies=cookies)
        r2 = requests.post(url, cookies=cookies)
        r3 = requests.put(url, cookies=cookies)
        print("solo user GET request : " + str(r.status_code))
        print("solo user POST request : " + str(r2.status_code))
        print("solo user PUT request : " + str(r3.status_code))
    elif methodchoice == "2":
        cookies = input("\ninput 1st cookies: ")
        cookies2 = input("\ninput 2nd cookies: ")
        r = requests.get(url, cookies=cookies)
        r2 = requests.post(url, cookies=cookies)
        r3 = requests.put(url, cookies=cookies)
        r4 = requests.get(url, cookies=cookies2)
        r5 = requests.post(url, cookies=cookies2)
        r6 = requests.put(url, cookies=cookies2)
        print("1st user GET request : " + str(r.status_code))
        print("1st user POST request : " + str(r2.status_code))
        print("1st user PUT request : " + str(r3.status_code))
        print("2nd user GET request : " + str(r4.status_code))
        print("2nd user POST request : " + str(r5.status_code))
        print("2nd user PUT request : " + str(r6.status_code))
    elif methodchoice == "3":
        r = requests.get(url)
        r2 = requests.post(url)
        r3 = requests.put(url)
        print("unauthenticated GET request : " + str(r.status_code))
        print("unauthenticated POST request : " + str(r2.status_code))
        print("unauthenticated PUT request : " + str(r3.status_code))
    elif methodchoice == "4":
        cookies = input("\ninput cookies: ")
        cookies2 = input("\ninput 2nd cookies: ")
        r = requests.get(url, cookies=cookies)
        r2 = requests.post(url, cookies=cookies)
        r3 = requests.put(url, cookies=cookies)
        r4 = requests.get(url, cookies=cookies2)
        r5 = requests.post(url, cookies=cookies2)
        r6 = requests.put(url, cookies=cookies2)
        r7 = requests.get(url)
        r8 = requests.post(url)
        r9 = requests.put(url)
        print("1st user GET request : " + str(r.status_code))
        print("1st user POST request : " + str(r2.status_code))
        print("1st user PUT request : " + str(r3.status_code))
        print("2nd user GET request : " + str(r4.status_code))
        print("2nd user POST request : " + str(r5.status_code))
        print("2nd user PUT request : " + str(r6.status_code))
        print("unauthenticated GET request : " + str(r7.status_code))
        print("unauthenticated POST request : " + str(r8.status_code))
        print("unauthenticated PUT request : " + str(r9.status_code))

def runallmethods(methodchoice, url):
    if methodchoice == "1":
        cookies = input("\ninput cookies: ")
        r = requests.get(url, cookies=cookies)
        r2 = requests.post(url, cookies=cookies)
        r3 = requests.put(url, cookies=cookies)
        r4 = requests.delete(url, cookies=cookies)
        print("solo user GET request : " + str(r.status_code))
        print("solo user POST request : " + str(r2.status_code))
        print("solo user PUT request : " + str(r3.status_code))
        print("solo user DELETE request : " + str(r4.status_code))
    elif methodchoice == "2":
        cookies = input("\ninput 1st cookies: ")
        cookies2 = input("\ninput 2nd cookies: ")
        r = requests.get(url, cookies=cookies)
        r2 = requests.post(url, cookies=cookies)
        r3 = requests.put(url, cookies=cookies)
        r4 = requests.delete(url, cookies=cookies)
        r5 = requests.get(url, cookies=cookies2)
        r6 = requests.post(url, cookies=cookies2)
        r7 = requests.put(url, cookies=cookies2)
        r8 = requests.delete(url, cookies=cookies2)
        print("1st user GET request : " + str(r.status_code))
        print("1st user POST request : " + str(r2.status_code))
        print("1st user PUT request : " + str(r3.status_code))
        print("1st user DELETE request : " + str(r4.status_code))
        print("2nd user GET request : " + str(r5.status_code))
        print("2nd user POST request : " + str(r6.status_code))
        print("2nd user PUT request : " + str(r7.status_code))
        print("2nd user DELETE request : " + str(r8.status_code))
    elif methodchoice == "3":
        r = requests.get(url)
        r2 = requests.post(url)
        r3 = requests.put(url)
        r4 = requests.delete(url)
        print("unauthenticated GET request : " + str(r.status_code))
        print("unauthenticated POST request : " + str(r2.status_code))
        print("unauthenticated PUT request : " + str(r3.status_code))
        print("unauthenticated DELETE request : " + str(r4.status_code))
    elif methodchoice == "4":
        cookies = input("\ninput cookies: ")
        cookies2 = input("\ninput 2nd cookies: ")
        r = requests.get(url, cookies=cookies)
        r2 = requests.post(url, cookies=cookies)
        r3 = requests.put(url, cookies=cookies)
        r4 = requests.delete(url, cookies=cookies)
        r5 = requests.get(url, cookies=cookies2)
        r6 = requests.post(url, cookies=cookies2)
        r7 = requests.put(url, cookies=cookies2)
        r8 = requests.delete(url, cookies=cookies2)
        r9 = requests.get(url)
        r10 = requests.post(url)
        r11 = requests.put(url)
        r12 = requests.delete(url)
        print("1st user GET request : " + str(r.status_code))
        print("1st user POST request : " + str(r2.status_code))
        print("1st user PUT request : " + str(r3.status_code))
        print("1st user DELETE request : " + str(r4.status_code))
        print("2nd user GET request : " + str(r5.status_code))
        print("2nd user POST request : " + str(r6.status_code))
        print("2nd user PUT request : " + str(r7.status_code))
        print("2nd user DELETE request : " + str(r8.status_code))
        print("unauthenticated GET request : " + str(r9.status_code))
        print("unauthenticated POST request : " + str(r10.status_code))
        print("unauthenticated PUT request : " + str(r11.status_code))
        print("unauthenticated DELETE request : " + str(r12.status_code))

print('''
 ▄████████    ▄████████ ███    █▄  ████████▄  ████████▄     ▄████████    ▄████████ 
███    ███   ███    ███ ███    ███ ███   ▀███ ███   ▀███   ███    ███   ███    ███ 
███    █▀    ███    ███ ███    ███ ███    ███ ███    ███   ███    █▀    ███    ███ 
███         ▄███▄▄▄▄██▀ ███    ███ ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
███        ▀▀███▀▀▀▀▀   ███    ███ ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
███    █▄  ▀███████████ ███    ███ ███    ███ ███    ███   ███    █▄  ▀███████████ 
███    ███   ███    ███ ███    ███ ███   ▄███ ███   ▄███   ███    ███   ███    ███ 
████████▀    ███    ███ ████████▀  ████████▀  ████████▀    ██████████   ███    ███ 
             ███    ███                                                 ███    ███
''')


print("pick:\n1) 1 user\n2) 2 users\n3) unauthenticated\n4) all of the above")
methodchoice = input("\nchoice: ")
print("\npick:\n1) GET\n2) POST\n3) PUT\n4) DELETE\n5) 1-3\n6) ALL")
method = input("choice: ")
url = input("\ninput url: ")

if method == "1":
    getmethod(methodchoice, url)
elif method == "2":
    postmethod(methodchoice, url)
elif method == "3":
    putmethod(methodchoice, url)
elif method == "4":
    deletemethod(methodchoice, url)
elif method == "5":
    method1thru3(methodchoice, url)
elif method == "6":
    runallmethods(methodchoice, url)

time.sleep(30)
