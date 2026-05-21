from flask import Blueprint,render_template ,request 
from database.db import get_connection

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM usuarios WHERE email=%s AND senha=%s", (email, senha))
        
        usuario = cur.fetchone()
        cur.close()
        conn.close()
        
        if usuario:
            return "Login Realizado com sucesso!"
        else:
            return "Usuário ou senha inválidos!"
    return render_template("login.html")