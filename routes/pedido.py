from flask import Blueprint, render_template, session, flash, redirect, url_for

pedido_bp = Blueprint("pedido", __name__)

@pedido_bp.route("/pedido")
def pedido():
    if "usuario_id" not in session:
        flash("Você precisa estar logado para acessar os pedidos.", "warning")
        return redirect(url_for("login.login"))
    return render_template("pedido.html")