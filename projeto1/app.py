from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/QUEMSOMOS")
def quemsomos():
    return render_template("quemsomos.html")

@app.route("/CONTATOS")
def contatos():
    return render_template("contatos.html")

if __name__ == "__main__":
    app.run(debug=True)