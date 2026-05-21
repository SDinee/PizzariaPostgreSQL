from flask import Blueprint, render_template

pedido_bp = Blueprint("pedido", __name__)

@pedido_bp.route("/pedido")
def pedido():
    return render_template("pedido.html")