def login():
  name = "keira"
  password = "catsRpawsome"
  while True:
   username = input("What is your username?: ")
   userPassword = input("What is your password?: ")
   if name == username and password == userPassword:
    print("You are logged in!")
    print("Welcome to replit, Keira!")
    break
   else:
    print("Oh no! I didn't quite recognise that username and/or password.")
    print("Please try again.")
    print()
    continue
print("Replit Login System") 
print()
login()
exit()
