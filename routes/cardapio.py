from flask import Blueprint, render_template

cardapio_bp = Blueprint("cardapio", __name__)

@cardapio_bp.route("/cardapio")
def cardapio():
    return render_template("cardapio.html")
