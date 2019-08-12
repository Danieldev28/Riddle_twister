import os
from flask import Flask, render_template , request
# import random

app = Flask(__name__)

@app.route("/", methods= ["POST", "GET"])
def index():
    if request.method== "POST":
        print(request.form)
    return render_template("index.html")


# play_game = True


array = ['hearts', 'spades', 'clubs', 'diamonds']
def my_shuffle(array):
    for item in array:
        shuffled_word = list(item)
        random.shuffle(shuffled_word)
        random_word = ''.join(shuffled_word)
        print(random_word)
    return array
    
# my_shuffle(array)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

