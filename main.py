print("Register")
login = input("Enter login:")
password = input("Enter password:")
f = open("file.txt","w")
f.write(f"{login.lower()}:{password}")
f.close()


print("Log-in")
login = input("Enter login:")
password = input("Enter password:")
authLog = ""
authPass = ""
f = open("file.txt","r")
text = f.read()
f.close()
authLog = text.split(":")[0]
authPass = text.split(":")[1]
if authLog == login.lower() and password == authPass:
  print("Welcome!")
else:
  print("Try again!")