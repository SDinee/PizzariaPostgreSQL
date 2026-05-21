from flask import Blueprint,render_template ,request, request, redirect, url_for, flash, session
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
            session["usuario_id"] = usuario[0]  # Armazena o ID do usuário na sessão
            session["usuario_email"] = usuario[2]  # Armazena o email do usuário na sessão
            
            flash("Login realizado com sucesso!", "success")
            return redirect(url_for("home.home"))
        else:
            flash("Usuário ou senha inválidos!", "error")
            return redirect(url_for("login.login"))
        
    return render_template("login.html")

@login_bp.route("/logout")
def logout():
    session.clear()  # Remove o ID do usuário da sessão
    flash("Você saiu da sua conta.", "info")
    return redirect(url_for("login.login"))