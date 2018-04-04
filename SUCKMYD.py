from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
<<<<<<< HEAD

    return "Hello World!Investigating!YOYOhihii"

=======
    return "Hello Worldcvbnm,fghjkl!"
>>>>>>> 63e7ec9e70e42ba65b1f07e04b428c188d9c905e

if __name__=="__main__":
        app.run()
