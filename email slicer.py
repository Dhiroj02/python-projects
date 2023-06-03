def xxx():
    print("welcome to the email slicer")
    print("")

    email_input  = input("input your email address: ")
    (username,domain)= email_input.split("@")
    (domain,extention)= email_input.split(".")
    
    print("Username:" , username)
    print("Domain: " , domain)
    print("Extension: " , extention) 
while True:
    xxx()
