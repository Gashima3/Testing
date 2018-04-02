from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
<<<<<<< HEAD
    return "Hello World!Investigating!YOYO"
=======
    return "Hello World!Investigating!YOYOhihii"
<<<<<<< HEAD
>>>>>>> 74930af60b65be19c038510cb8e48c101a033639
=======
>>>>>>> b2ef17cf628ddeb8bbba56509624ba3b4c74fa09
>>>>>>> b792b3fc0c27b0a667809a7ed474f4da6504224e

if __name__=="__main__":
        app.run()
