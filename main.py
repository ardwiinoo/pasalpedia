from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/auth/register")
def register():
    return render_template("/views/auth/register/index.html")


app.run(debug=True)