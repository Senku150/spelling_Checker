import pyttsx3
from flask import Flask
import math
import random
import json
import socket

def read_specific_line(file_path, line_number):
  with open(file_path, "r") as f:
    # Check for valid line number (within file bounds)
    if line_number < 1 or line_number > sum(1 for _ in f):
      return None  # Handle invalid line number

    # Move the file pointer to the beginning of the desired line
    f.seek(0)  # Reset pointer to beginning
    for i in range(line_number - 1):  # Skip lines until target line
      f.readline()  # Discard lines we don't need

    # Read and return the specific line
    return f.readline().strip()  # Read and remove trailing newline
random.seed()
randomNum=random.randint(1,89058)
line_content = read_specific_line("anagram_dictionary.txt", randomNum)

print(line_content)
pyttsx3.speak(line_content)




"""app = Flask(__name__)

hidden = None

tries = 0


#Creating the game
def generate(low, high, ip):
    random.seed()
    global hidden
    global tries

    #Swapping the values if the user entered them in the wrong order
    temp = 0
    if(low > high):
        temp = low
        low = high
        high = temp

    
    tries = round(math.log(high-low+1,2)) #The equation that calculates the minimum tries is not mine
    hidden = random.randint(low, high)#Chosing the random number
    
    app.run(debug=False, host=ip, port=5000)




@app.route("/", methods=["GET"])
def index():
    #Sending the hidden number and number of tries to any user that connects to the server
    return json.dumps({"hidden" : hidden, "tries" : tries})
    





if __name__ == "__main__":
    ip = socket.gethostbyname(socket.gethostname())
    low = int(input("Enter the lowest number: "))
    high = int(input("Enter the highest number: "))
    print(f"[**] Use {ip} as the ip for clients [**] \n Ignore everything under this message\n")
    generate(low, high, ip)"""