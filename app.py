import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    image_url = None

    if request.method == "POST":
        outcome = random.choice(["Heads", "Tails"])
        result = f"It's {outcome}!"
        # Python seekhni paray gi sahi se

     <<<<<<< HEAD
        if outcome == "Heads":
            image_url = "/static/heads-gold.jpg"
=======
        if outcome == "Heads":
            image_url = "/static/heads.jpg"
>>>>>>> dev
    return render_template("index.html", result=result, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)