def CreatAccount():
    saldo =1100
    kontonummer = int(input('Ange kontonummer>'))
    if kontonummer in allAccounts:
        print('redan taget')
    else:
        allAccounts[kontonummer] = saldo

def signInAccount():
     kontonummer = int(input('Ange kontonummer>'))
     if kontonummer in allAccounts:
         while True:
            printSubMeny()
            sel = input("Ange val:")
            if sel == "1":
               withDraw(kontonummer)
            elif sel =="2":
               Deposite(kontonummer)
            elif sel =="3":
               print(allAccounts[kontonummer])    
            elif sel == "4":
               return    
     else:
        print('Account not existing')
        pass

def printSubMeny():
   print('\033[34m1. Ta ut pengar')
   print('\033[34m2. Sätt in pengar')
   print('\033[34m3. Visa saldo')
   print('\033[34m4. Tillbaka')

def withDraw(kontonummer):
   
   belopp = int(input('\033[33mAnge belopp:'))
   if belopp > allAccounts[kontonummer]:
      print('det gör inta att ta ut pengar')
      
   else:
      
      allAccounts[kontonummer] = allAccounts[kontonummer]  - belopp
      print(f"saldo: {allAccounts[kontonummer]}")
         
def Deposite(kontonummer):
      belopp = int(input('\033[34mAnge belopp:'))
      allAccounts[kontonummer] = allAccounts[kontonummer] + belopp
      for saldo in allAccounts.values():
         print(f"saldo: {saldo}")


def printHuvudMeny():
    print('\033[32m****HUVUDMENY****')
    print('\033[37m1. Skapa konto')
    print('\033[37m2. Administrera konto')
    print('\033[37m3. Avsluta')

allAccounts = {'1234': 500,'1009':1000, '1002': 300}
allAccounts = {}

   
while True:
   printHuvudMeny()
   val = (input('\033[33mAnge menyval >'))
   if val == '1':
         CreatAccount()
   elif val == '2':
         signInAccount()
   elif val == '3':
      break
   else:
         pass


      

#print(\033[32m) for colours
# black =30
# red =31
# green 32
# yellow = 33
# blue= 34
# magenta = 35
# cyan =36
# white = 37
# reset = 39