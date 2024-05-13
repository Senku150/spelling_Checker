from flask import Flask
import random
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



app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
  random.seed()
  randomNum=random.randint(1,89058)
  line_content = read_specific_line("anagram_dictionary.txt", randomNum)
  return line_content

if __name__ == "__main__":
    ip = socket.gethostbyname(socket.gethostname())
    app.run(debug=False, host=ip, port=5000)



