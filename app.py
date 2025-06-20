from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    message = None
    name = request.form.get("name")
    if name and name.lower().strip() == "prerna":
        message = (
            f"""
            <body style='font-family: Arial, sans-serif; line-height: 1.6; color: #333;'>
            <p>Hey {name},</p>
            
            <p>I never thought I’d be writing something like this to flirt with you — but hey, who wouldn’t be into someone who codes? 😄</p>

            <p>I already love your techy posts and your wonderfully weird, unique vibe. I would gladly bookmark your profile 😂</p>

            <p>Honestly, your weirdness is exactly my kind of awesome! 🤓</p>

            <p>So wondering...would you like to join me for coffee or lunch sometime on the weekend ? Maybe we can geek out and make some great memories together! 😊</p>

            <p><i>P.S. Are you an Exception? Cause I’d catch you every single day! </i> 💻😉</p>

            </body>
        """
        )
    elif name:
        message = (
            "Wait- stranger, you aint the one I am expecting. <br>"
            "No pranks, I know who you are!! Try again 😏"
        )
    return render_template("result.html", message=message, name=name)

if __name__ == "__main__":
    app.run(debug=True)