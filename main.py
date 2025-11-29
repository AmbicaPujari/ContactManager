contacts=[]
print("contacts manager created!")
def addContact(name ,num,email):
    contacts.append({
    'name':name ,
    'number':num ,
    'email':email
    })
    contacts.sort(key=lambda x: x["name"])
def delContacts(name):
    for a in contacts:
        if a['name']==name:
            contacts.remove(a)
            return True
    return False

while True:
    cmd=input("Add:add , Delete:del , Display:all , Exit:exit \n Mode:").lower()
    match cmd:
        case 'add':
            name=input("Name:") 
            num=input("Mobile No:") 
            email=input("email:")
            addContact(name , num , email)
            print("added!")
        case 'del':
            name=input("Name:")
            if delContacts(name):
                print("deleted!")
            else:
                print("Not Found")
        case 'all':
            print(contacts)
        case 'exit':
            print("Exited!")
            break
        case _:
            print("Invalid!")
