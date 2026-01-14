balance=0.0

def check_balance():
    print(f"your current balance is {balance}")

def deposit(amount):
    global balance
    if amount >=0:
        balance += amount
    else:
        print("cannot deposit")

def withdraw(amount):
    global balance
    if amount < 0:
        print("can not withdraw")
        
    elif amount > balance:
        print("can not withdraw")
        
    else:
        balance -= amount



kyc_documents={}
def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc():
    if len(kyc_documents) == 0:
        print("kyc not done ")
    else:
        for doc in kyc_documents:
            print(f"{doc} : {kyc_documents[doc]}")



print("welcome to atharv bank application my dears ")

while True :
    print("1.check your balance")
    print("2.deposit an amount")
    print("3.withdraw an amount")
    print("4.check kyc")
    print("5.update kyc")
    print("6.quit")
    choice=int(input("enter your choice (1-6)"))

    if choice == 1:
        check_balance()
    elif choice == 2:
        amt=float(input("enter amount to deposit:"))
        deposit(amt)
        print(f"amount deposited {amt}")
    elif choice == 3 :
        amt=float(input("enter amount to deposit"))
        if amt >=0:
           print("can not withdraw")
        elif balance<amt:
            print("insufficient balance")
        else:
            
            print(f"amount withdrawn{amt}")
    elif choice == 4:
        check_kyc()
    elif choice == 5 :
        kyc_docs={}
        n_document= int(input("enter number of documents you wanted to add :"))
        for i in range (n_document):
            key= str(input("enter document type :"))
            value= input ("enter document number:")
            kyc_docs[key]= value
            print(f"kyc updated")
    elif choice == 6:
        break
    else:
        print("ivalid choice!!! re try")
         

print("Thank you for banking with uss")





