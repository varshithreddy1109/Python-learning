def greet_user(first_name,last_name):#function
    print("Hi there!!",first_name,last_name)
    print("Welcome abord")

greet_user("shiva","shankar")#calling of the function
greet_user("Revanth","MG")

greet_user("achanta", first_name="revanth")#keyword aruguments:in this case postion is not cared


#emoji converter using function

def emoji(message):
    words = message.split()
    output = ""
    emojis = {
              ":)":"😊",
              ":(":"😔"
              }
    for word in words:
         output+= emojis.get(word,word)
    return output

output = emoji(input("Enter message"))
print("output")