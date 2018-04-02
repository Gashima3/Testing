from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
<<<<<<< HEAD
    return "Hello World!Investigating!YOYO"
=======
    return "Hello World!Investigating!YOYOhihii"
>>>>>>> b2ef17cf628ddeb8bbba56509624ba3b4c74fa09

if __name__=="__main__":
        app.run()
