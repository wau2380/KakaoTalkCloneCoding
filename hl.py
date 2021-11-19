id = input()
password = input()

if id == "admin":
    if password == "password":
        print("success")
    else:
        print("fail")