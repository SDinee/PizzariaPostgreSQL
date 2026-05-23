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
        if "pedido" not in session:
            session["pedido"] = {}

        if pizza_nome in session["pedido"]:
            session["pedido"][pizza_nome] += 1
        else:
            session["pedido"][pizza_nome] = 1
        session.modified = True # garante que a sessão será atualizada

    # Carrega itens do pedido (funciona para GET e POST)
    conn = get_connection()
    cur = conn.cursor()
    itens = []
    if "pedido" in session:
        for nome, qtd in session["pedido"].items():
            cur.execute("SELECT preco, imagem, disponivel FROM produtos WHERE nome = %s", (nome,))
            pizza = cur.fetchone()
            if pizza:
                # pizza = (preco, imagem, disponivel)
                itens.append((nome, pizza[0], pizza[1], pizza[2], qtd))

    cur.close()
    conn.close()
    
    total = sum([float(preco) * qtd for _, preco, _, _, qtd in itens])

    return render_template("pedido.html", itens = itens, total = total)

@pedido_bp.route("/remover/<nome>", methods=["POST"])
def remover_item(nome):
    if "pedido" in session:
        if nome in session["pedido"]:
            if session["pedido"][nome] > 1:
                session["pedido"][nome] -= 1
            else:
                del session["pedido"][nome]
            session.modified = True
    return redirect(url_for("pedido.pedido"))
