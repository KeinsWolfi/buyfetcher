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

#apikey
while True:
    #api request !!!DONT TOUCH!!!
    bazaar = req.get("https://api.hypixel.net/skyblock/bazaar?key=fe271ec9-3dcd-4b3f-8873-e33b46311e97").json()

    #Calculate pirce change
    changeBuy=(bazaar['products'][userinput]['quick_status']['buyPrice'])-changeBuyOld
    changeSell=(bazaar['products'][userinput]['quick_status']['buyPrice'])-changeSellOld

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
    print("Instabuy: " + str(bazaar['products'][userinput]['quick_status']['buyPrice']) + " | Change: " + TextColBuy + str(changeBuy) + Fore.WHITE)
    print("Instabuy: " + str(bazaar['products'][userinput]['quick_status']['sellPrice']) + " | Change: " + TextColSell + str(changeSell) + Fore.WHITE)

    print("Sellorders: " + str(bazaar['products'][userinput]['quick_status']['sellOrders']))
    
    changeBuyOld=bazaar['products'][userinput]['quick_status']['buyPrice']
    changeSellOld=bazaar['products'][userinput]['quick_status']['sellPrice']

    time.sleep(60)

