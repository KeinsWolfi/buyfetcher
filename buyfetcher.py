import requests as req
import time
from datetime import datetime
from colorama import Fore
import os


os.system("")

userinput = str(input("Enter the item_id (UPPERCASE!) you want to request- "))

TextColBuy=Fore.RED
TextColSell=Fore.GREEN
changeBuy = 0
changeBuyOld = 0
changeSell = 0
changeSellOld = 0

  
#read webhook from file
webhookurlfile= open("webhook.txt","r")
webhookurl=webhookurlfile.read()
webhookurlfile.close()



#apikey
while True:
    #api request !!!DONT TOUCH!!!
    bazaar = req.get("https://api.hypixel.net/skyblock/bazaar?key=865b2506-9e10-4f9c-9e4d-df99272960ec").json()

    #Calculate pirce change
    changeBuy=(bazaar['products'][userinput]['quick_status']['buyPrice'])-changeBuyOld
    changeSell=(bazaar['products'][userinput]['quick_status']['sellPrice'])-changeSellOld

    
    #Webhook message content
    embed = {
        "description": "Instabuy: " + f"{(bazaar['products'][userinput]['quick_status']['buyPrice']):,}" + " | Change: " + f"{(round(changeBuy, 3)):,}" + "\n" + "Instasell: " + f"{(bazaar['products'][userinput]['quick_status']['sellPrice']):,}" + " | Change: " + f"{(round(changeSell, 3)):,}" + "\n" + "Sellorders: " + f"{(bazaar['products'][userinput]['quick_status']['sellOrders']):,}",
        "title": userinput
    }

    data = {
    "embeds": [
        embed
    ]
    }

    #send message to webhook
    result = req.post(webhookurl, json = data)

    if changeBuy<=0:
        TextColBuy=Fore.GREEN
    else:
        TextColBuy=Fore.RED

    if changeSell>=0:
        TextColSell=Fore.GREEN
    else:
        TextColSell=Fore.RED

    #Print
    print(userinput + ":")
    print("Instabuy: " + f"{(bazaar['products'][userinput]['quick_status']['buyPrice']):,}".format() + " | Change: " + TextColBuy + f"{(round(changeBuy, 3)):,}" + Fore.WHITE)
    print("Instasell: " + f"{(bazaar['products'][userinput]['quick_status']['sellPrice']):,}" + " | Change: " + TextColSell + f"{(round(changeSell, 3)):,}" + Fore.WHITE)

    print("Sellorders: " + f"{(bazaar['products'][userinput]['quick_status']['sellOrders']):,}")
    
    #set changes
    changeBuyOld=bazaar['products'][userinput]['quick_status']['buyPrice']
    changeSellOld=bazaar['products'][userinput]['quick_status']['sellPrice']

    time.sleep(60)

