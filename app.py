from flask import Flask, render_template

app = Flask(__name__)

reasons = ["Material sempre atualizado", "Tablets em sala de aula", "Professores renomados",
           "Universidade bem avaliada", "Ótima localização"]



@app.route('/home')
def home():
    return render_template('Home.html')


@app.route("/quemsomos")
def quemsomos():
    return render_template("QuemSomos.html", qty_reasons=len(reasons), reasons=reasons)


@app.route("/contato")
def contato():
    return render_template("contato.html")


if __name__ == "__main__":
    app.run(debug=True)
