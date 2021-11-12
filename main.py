import hashlib
import requests

url= 'http://www.google.com'

def request_and_write(url):

    response = requests.get(url)
    f = open("wepPage.html", "w")
    f.write(response.text)
    f.close()

    return response

def checksum():
    f = open("wepPage.html", "r")
    f2 = open("checksum.txt", "w")
    f2.write(hashlib.sha256(f.read().encode('utf-8')).hexdigest())
    f.close()
    f2.close()

if __name__ == '__main__':
    request_and_write(url)
    checksum()


