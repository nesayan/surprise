from flask import Flask, render_template, request
import os

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

            <p>I lowkey like your techy posts and your wonderfully weird, unique vibe. Which is exactly my kind of awesome!</p>

            <p>Wondering...would you join me for coffee or lunch sometime on the weekend ? Maybe we can geek out and make some great memories together! 😊</p>

            <p><i>P.S. You better be an Exception. Cause I would catch you! </i> 💻😉</p>

            </body>
        """
        )
    elif name:
        message = (
            f"""
                <body style='font-family: Arial, sans-serif; line-height: 1.6; color: #333;'>
                <p>No pranks, I already know who you are!! 😏</p>
                
                <p>Never thought I’d be writing something like this to flirt with you — but hey, who wouldn’t be into someone who codes? 😄</p>

                <p>I lowkey like your techy posts and your wonderfully weird, unique vibe. Which is exactly my kind of awesome!</p>

                <p>Wondering...would you join me for coffee or lunch sometime on the weekend ? Maybe we can geek out and make some great memories together! 😊</p>

                <p><i>P.S. You better be an Exception. Cause I would catch you! </i> 💻😉</p>

                </body>
            """
        )
    return render_template("result.html", message=message, name=name)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)