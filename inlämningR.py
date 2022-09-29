

while True:
 allAccounts = {'1234': 500,'1009':1000, '1002': 300}
 allAccounts = {}
 
 def CreatAccount():
    saldo =1100
    kontonummer = int(input('Ange kontonummer>'))
    if kontonummer in allAccounts:
        print('redan taget')
    else:
        allAccounts[kontonummer] = saldo
        
 while True:
  def signInAccount():
    
     kontonummer = int(input('Ange kontonummer>'))
     if kontonummer in allAccounts:
        printSubMeny()
  
        withDraw()
     else:
        print('Account not existing')
        pass
        
  def printHuvudMeny():
    print('\033[32m****HUVUDMENY****')
    print('\033[37m1. Skapa konto')
    print('\033[37m2. Administrera konto')
    print('\033[37m3. Avsluta')
  printHuvudMeny()
 
  val = int(input('\033[33mAnge menyval >'))
  if val == 1:
        
        CreatAccount()
        

  elif val == 2:
       
        signInAccount()
  else:
         pass
  def printSubMeny():
    print('1. Ta ut pengar')
    print('2. Sätt in pengar')
    print('3. Visa saldo')
  def withDraw():
    
     kontonummer = int(input('Ange Kontonummer'))
     belopp = int(input('Ange belopp:'))
     saldo = 1100
     if belopp > saldo:
      print('det gör inta att ta ut pengar')
      Deposite()
     else:
       
      allAccounts[kontonummer] = allAccounts[kontonummer]  - belopp
      print(f"saldo: {allAccounts[kontonummer]}")
        
  def Deposite():
    belopp = int(input('Ange belopp:'))
    kontonummer = int(input('Ange kontonummer:'))
    allAccounts[kontonummer] = allAccounts[kontonummer] + belopp
    for saldo in allAccounts.values():
     print(f"saldo: {saldo}")
 

      

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