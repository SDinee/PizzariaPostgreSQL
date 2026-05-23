from flask import Blueprint, render_template, session, flash, redirect, url_for, request
from database.db import get_connection

pedido_bp = Blueprint("pedido", __name__)

@pedido_bp.route("/pedido", methods=["GET", "POST"])
def pedido():
    # Verifica login
    if "usuario_id" not in session:
        flash("Você precisa estar logado para acessar os pedidos.", "warning")
        return redirect(url_for("login.login"))

    # Se for POST, adiciona pizza ao pedido
    if request.method == "POST":
        pizza_nome = request.form["pizza_nome"]
        session.setdefault("pedido", []).append(pizza_nome)
        session.modified = True # garante que a sessão será atualizada

    # Carrega itens do pedido (funciona para GET e POST)
    conn = get_connection()
    cur = conn.cursor()
    itens = []
    if "pedido" in session:
        for nome in session["pedido"]:
            cur.execute("SELECT nome, preco, imagem FROM produtos WHERE nome = %s", (nome,))
            pizza = cur.fetchone()
            if pizza:
                itens.append(pizza)
    cur.close()
    conn.close()

    return render_template("pedido.html", itens=itens)
