#Thank you BongoBondhuSheikhMujiburRahman for helping me in this journey !
#Must Subscribe On YouTube @BongoBondhuSheikhMujiburRahmanr 

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '@BongoBondhuSheikhMujiburRahman'

if __name__ == "__main__":
    app.run()
