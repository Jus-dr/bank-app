import random
import time
import datetime
import sys
import requests
import json

# EXCHANGE API

url = "https://api.exchangerate.host/latest?base=USD"
response = requests.get(url)
data = response.json()
try_ = data["rates"]["TRY"]

# EXCHANGE API

class Bank():
    def __init__(self,name):
        self.name = name
        self.dollars = 0
        self.trys = 0
        self.acc_num = ""


        for i in range(0,7):
            random_num = random.randint(1,9)
            self.acc_num += str(random_num)
        
        self.acc_num = int(self.acc_num)

    def showMyInfos(self):
        print("\n---------------------------------\n")
        print(f"Name : {self.name}\nAccount Number : {self.acc_num}\nDollar Balance : {self.dollars}$\nTry Balance : {self.trys}TRY")

        self.chooseProcess()

    def wantReceipt(self,process_num,money = 0):
        print("\n---------------------------------\n")

        now = datetime.datetime.now()
        current = now.strftime("%H:%M:%S")

        if (process_num == 1):
            print(f"|------------JUSDR BANK------------|\n| Deposited money : {money}$\n| New Balance : {self.dollars}$\n| Process Time : {current}\n|------------JUSDR BANK------------|")

        elif (process_num == 2):
            print(f"|------------JUSDR BANK------------|\n| Withdrawed money : {money}$\n| New Balance : {self.dollars}$\n| Process Time : {current}\n|------------JUSDR BANK------------|")

        self.chooseProcess()

    def deposit(self):
        print("\n---------------------------------\n")
        money = int(input("How much dollars do you want to deposit : "))
        confirm = input(f"You wanted to deposit {money}$, do you confirm [y/n] ? : ")

        if (confirm in ["y","Y"]):
            print("Depositing your money...")
            self.dollars += money
            time.sleep(1)
            print(f"Deposited {money}$ to your account , your new balance {self.dollars}$")

            process = input("Do you want to print your receipt ? = [y/n] : ")
            if (process in ["y","Y"]):
                self.wantReceipt(1,money)
                self.chooseProcess()
            else:
                self.chooseProcess()
                

        elif (confirm in ["n","N"]):
            print("You did not confirmed your request")
            print("Exiting deposit page...")
            time.sleep(1)
            self.chooseProcess()

        else:
            print("Wrong input...")
            time.sleep(1)
            self.chooseProcess()

    def withdraw(self):
        print("\n---------------------------------\n")
        money = int(input("How much dollars do you want to deposit : "))
        confirm = input(f"You wanted to withdraw {money}$, do you confirm [y/n] ? : ")

        if (confirm in ["y","Y"]):

            if (self.dollars - money < 0):
                print("You do not have enough money for withdraw")
                print("Exiting withdraw page...")
                self.chooseProcess()

            print("Withdrawing your money...")
            self.dollars -= money
            time.sleep(1)
            print(f"Withdrawed {money}$ from your account , your new balance {self.dollars}$")
            process = input("Do you want to print your receipt ? = [y/n] : ")

            if (process in ["y","Y"]):
                self.wantReceipt(2,money)
                self.chooseProcess()
            else:
                self.chooseProcess()
                
        elif (confirm in ["n","N"]):
            print("You did not confirmed your request")
            print("Exiting withdraw page...")
            time.sleep(1)
            self.chooseProcess()
        else:
            print("Wrong input...")
            time.sleep(1)
            self.chooseProcess()
        
            

    def changeTRY(self):
        print("\n---------------------------------\n")
        money = int(input("How much dollars do you want to change to Turkish Liras : "))
        confirm = input(f"You wanted to change {money}$ to Turkish Liras , do you confirm [y/n] ? : ")

        if (money > self.dollars or self.dollars <= 0):
            print("You do not have enough Dollars")
            time.sleep(1)
            self.chooseProcess()

        else:
            if (confirm in ["y","Y"]):
                print("Changing your money...")
                time.sleep(1)
                print(f"Changed {money}$ to {money * try_}TRY")
                self.dollars -= money
                self.trys += money * try_

            elif (confirm in ["n","N"]):
                print("You did not confirmed your request")
                print("Exiting changeTRY page...")
                time.sleep(1)
                self.chooseProcess()

            else:
                print("Wrong input...")
                time.sleep(1)
                self.chooseProcess()

    def exit(self):
        print("\n---------------------------------\n")
        print("Have a good day...")
        sys.exit()

    def chooseProcess(self):
        """
            1.Deposit Money
            2.Withdraw Money
            3.Print Information
            4.Change TRY
            5.Exit

        """
        print("\n---------------------------------\n")
        print(f"Welcome {self.name} to Jus-dr Bank...")
        time.sleep(1)
        choose = int(input("Choose your process :\n 1.Deposit Money\n 2.Withdraw Money\n 3.Print My Informations\n 4.Change TRY\n 5.Exit\n Your choose : "))

        while (choose not in [1,2,3,4,5]):
            choose = int(input("Wrong choose try again : "))

        if (choose == 1):
            self.deposit()
        elif (choose == 2):
            self.withdraw()
        elif (choose == 3):
            self.showMyInfos()
        elif (choose == 4):
            self.changeTRY()
        elif (choose == 5):
            self.exit()


bank_account = Bank("Ahmet")

bank_account.chooseProcess()