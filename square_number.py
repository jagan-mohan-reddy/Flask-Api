from flask import Flask

app = Flask(__name__)

@app.route("/square/<int:num>")
def square(num):
    return str(num**2)


if __name__ == '__main__':
    app.run(debug=True)

#Run this py file in one terminal using python3 /path/square_number.py
#On another terminal run below line
#curl http://127.0.0.1:5000/square/8
