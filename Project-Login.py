#Project -Login

username="sachin"
password="password"

username_input= input("username:")
password_input=input("password:")

if username_input==username and password_input==password:
    print("Access Granted")
    print("Welcome")
elif username_input!= username and password_input== password:
    print("Incorrect username")
elif username_input==username and password_input!=password:
    print("Incorrect password")
else:
    print("You might wanna check both")









    
