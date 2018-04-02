from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
<<<<<<< HEAD
    return "Hello World!Investigating!YOYO"
=======
    return "Hello World!Investigating!YOYOhihii"
>>>>>>> 74930af60b65be19c038510cb8e48c101a033639

if __name__=="__main__":
        app.run()
