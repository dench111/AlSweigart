import os

pingServer = 'ping -c 3 192.168.0.1'

def checkServerHealth(param):
    result = (os.popen(param).read())
    print(result)

checkServerHealth(pingServer)