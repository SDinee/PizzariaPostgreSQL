from flask import Blueprint, render_template, request
from database.db import get_connection

cadastro_bp = Blueprint("cadastro", __name__)

@cadastro_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]
        telelfone = request.form["telefone"]
        endereco = request.form["endereco"]
        cpf = request.form["cpf"]
        
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO usuarios (nome, email, senha, telefone, endereco, cpf) VALUES (%s, %s, %s, %s, %s, %s)",
            (nome, email, senha, telelfone, endereco, cpf)
        )
        
        conn.commit()
        cur.close()
        conn.close()
        
        return "Usuário cadastrado com sucesso!"
    return render_template("cadastro.html")