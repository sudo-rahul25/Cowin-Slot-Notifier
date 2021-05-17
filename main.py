import http.client
import json
from time import sleep
from datetime import datetime

data = 0
while 1:
    print("Starting execution of script")
    conn = http.client.HTTPSConnection("cdn-api.co-vin.in")
    payload = ''
    headers = {
        'accept': 'application/json'
    }
    conn.request("GET", "/api/v2/appointment/sessions/public/findByPin?pincode=800020&date=17-05-2021", payload, headers)
    res = conn.getresponse()
    data = res.read()
    real_data = data.decode("utf-8")
    print(real_data)

    # clock time print
    now = datetime.now()
    print(now)

    f = open("demofile3.txt", "w")
    f.write(real_data)
    f.close()

    with open("demofile3.txt") as f:
        temp_data = json.load(f)
    #   data=simplejson.load(f)
    f.close()

    # print(temp_data)
    for i in temp_data.keys():
        for j in temp_data[i]:
            # print(j['center_id'])
            print(j['name'])
            print("Age group:- ", end=" "),
            print(j['min_age_limit'])
            print("Available seats:- ", end=" "),
            print(j['available_capacity'])
            print("------------------------")
            if j['min_age_limit'] == 18:
                print(j)

                # system time print
                print("*********************SLOT FOUND***********************************")
                now = datetime.now()
                print(now)

                conn = http.client.HTTPSConnection("cdn-api.co-vin.in")
                payload = "{\"mobile\":\"94XXXXX\"}"
                headers = {
                    'accept': 'application/json',
                    'Content-Type': 'application/json'
                }
                conn.request("POST", "/api/v2/auth/public/generateOTP", payload, headers)
                res = conn.getresponse()
                data = res.read()
                # SMS metadata
                print(data.decode("utf-8"))
                print("*********************************************************")
                sleep(10)
    print("Sleep for 5 seconds :: Halting execution of script")
    print("=======================================================================================================")
    sleep(5)

print("execution of script ended")
