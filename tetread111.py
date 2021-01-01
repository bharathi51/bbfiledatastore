from filedatastore_BB import datastore_get
while True:
    print('select 1.create \n 2.read \n3.delete ')
    s=int(input())
    if s==1:
        k=input("enter key")
        val=input("enter value")
        print(datastore_get(1, client ="Access_store" , key = k, value = val, filepath = "E:\out1/"))
    elif s==2:
        k=input("enter key")
        print(datastore_get(2, client = "Access_store" , key = k))
    elif s==3:
        k=input("enter key")        
        print(datastore_get(3, client = "Access_store" , key = k))
        
