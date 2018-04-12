from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
<<<<<<< HEAD
<<<<<<< HEAD
    return "Hello World!say whatttttt"
=======
    return "Hello World!Investigating!YOYO"
>>>>>>> a8e2b7c2e00b138ae3abfbaec6d56fe25196e168
=======
    return "Hello World!Investigating!YOYO"
>>>>>>> a8e2b7c2e00b138ae3abfbaec6d56fe25196e168

if __name__=="__main__":
        app.run()
