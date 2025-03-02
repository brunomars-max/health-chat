from flask import Flask
from flask import render_template
from flask_socketio import SocketIO, send
from bot import ai_response
#create our server

app=Flask(__name__)
socket=SocketIO(app)
@app.route("/chatPage")
def chatPage():
    return render_template("index.html")

@app.route("/")
def home():
    return render_template("home.html")

@socket.on("connect")
def connect():
    print("someone is trying to connect")

@socket.on("message")
def message(ClientMessage):
    print("i have received",ClientMessage)
    response = ai_response(ClientMessage)    
    send(response)

@socket.on("disconnect")
def disconnect():
    print("someone left")




socket.run(app)