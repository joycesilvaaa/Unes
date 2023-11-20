from flask import Flask, render_template, request, flash, url_for, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'devweb'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'unes'

mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/QUEMSOMOS")
def quemsomos():
    return render_template("quemsomos.html")

@app.route("/CONTATOS", methods=['GET', 'POST'])
def contatos():
    if request.method == 'POST':
        email = request.form['email']
        assunto = request.form['assunto']
        conteudo = request.form['conteudo']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MENSAGENS(email_user, assunto, conteudo) VALUES (%s, %s, %s)", (email, assunto, conteudo))
        mysql.connection.commit()
        cur.close()
        flash('Sua mensagem foi envia para nossa base de dados!')
        return redirect (url_for('user'))
    return render_template("contatos.html")

@app.route('/MENSAGENS')
def user():
    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM mensagens")

    msg = cur.fetchall()

    cur.close()

    return render_template("msg.html", msg = msg)

if __name__ == "__main__":
    app.run(debug=True)