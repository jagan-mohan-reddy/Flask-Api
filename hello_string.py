from flask import Flask, jsonify, request

app = Flask(__name__)

#@app.route("/hello/<string:name>")

def hello(name):
    return "Hello "+name

if __name__ == '__main__':
    app.run(debug=True)


#run this file on one termianal using python3 /path/hello_string.py
#On another terminal type below line for output
#curl http://127.0.0.1:5000/hello/jagan
