from flask import Blueprint, render_template, request, redirect, url_for, session
from database.db import get_connection

cardapio_bp = Blueprint("cardapio", __name__)

@cardapio_bp.route("/cardapio")
def cardapio():
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT nome, preco, imagem FROM produtos")
    produtos = cur.fetchall()
    cur.close()
    conn.close()
    
    return render_template("cardapio.html", produtos = produtos)
