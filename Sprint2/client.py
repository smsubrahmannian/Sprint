import requests
import sys
import json

def send_request(server_address, data):
    """Send request to server"""
    r = requests.post(server_address,
                headers={'Content-Type': 'application/json'},
                 data=data)
    print(r.status_code, r.reason)

if __name__ == '__main__':
    #blob = {"name": "Kevin","prop": { "age": 12, "zipcode":94607,"DMID":388167}}
    json_file = "/home/ec2-user/t2.json"
    SERVER = sys.argv[1]
    with open(json_file, 'r') as jfile:
        json_text = jfile.read()
    send_request(SERVER,json_text)