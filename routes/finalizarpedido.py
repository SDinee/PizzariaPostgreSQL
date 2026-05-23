from flask import flash, redirect, session, request, url_for, render_template, Blueprint
from database.db import get_connection

finalizar_bp = Blueprint("finalizar", __name__)

@finalizar_bp.route("/finalizar_pedido", methods=["POST"])
def finalizar_pedido():
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("""
                INSERT INTO pedidos (usuario_id, tipo_entrega, tipo_pagamento)
                VALUES (%s, %s, %s) RETURNING id
                """, (session["usuario_id"], request.form["tipo_entrega"], request.form["tipo_pagamento"])) 
    pedido_id = cur.fetchone()[0]
    
    for nome, qtd in session.get("pedido", {}).items():
        cur.execute("SELECT id FROM produtos WHERE nome = %s", (nome,))
        produto = cur.fetchone()
        if produto:
            produto_id = produto[0]
            
            cur.execute("""
                        SELECT id, quantidade FROM itens_pedido
                        WHERE pedido_id = %s AND produto_id =%s
                        """, (pedido_id, produto_id))
            item_existente = cur.fetchone()
            
            if item_existente:
                cur.execute("""
                            UPDATE itens_pedido
                            SET quantidade = quantidade + %s
                            WHERE id = %s
                            """, (qtd, item_existente[0],))
            else:
                cur.execute("""
                            INSERT INTO itens_pedido (pedido_id, produto_id, quantidade)
                            VALUES (%s, %s, %s)""",
                            (pedido_id, produto_id, qtd))
    
    conn.commit()
    cur.close()
    conn.close()
    
    session.pop("pedido", None)
    flash("Pedido Finalizado com sucesso!")
    return redirect(url_for("finalizar.nota_fiscal", pedido_id = pedido_id))

@finalizar_bp.route("/nota_fiscal/<int:pedido_id>")
def nota_fiscal(pedido_id):
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("""
                SELECT p.id, u.nome, p.tipo_entrega, p.tipo_pagamento, p.data_pedido
                FROM pedidos p
                JOIN usuarios u ON p.usuario_id = u.id
                WHERE p.id = %s
                """, (pedido_id,))
    pedido = cur.fetchone()
    
    cur.execute("""
                SELECT pr.nome, pr.preco, pr.imagem, pr.disponivel, ip.quantidade
                FROM itens_pedido ip
                JOIN produtos pr ON ip.produto_id = pr.id
                WHERE ip.pedido_id = %s
                """, (pedido_id,))
    itens = cur.fetchall()
    
    cur.close()
    conn.close()
    
    total = sum([float(item[1]) * item[4] for item in itens])
    
    return render_template("nota_fiscal.html", pedido = pedido, itens = itens, total = total)