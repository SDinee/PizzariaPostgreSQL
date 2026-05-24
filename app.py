from flask import Flask
from routes.home import home_bp
from routes.cardapio import cardapio_bp
from routes.pedido import pedido_bp
from routes.cadastro import cadastro_bp
from routes.login import login_bp
from routes.finalizarpedido import finalizar_bp

app = Flask(__name__)

app.secret_key = "umasecretekeyqualquercuidadocomestasenha"

app.register_blueprint(home_bp)
app.register_blueprint(cardapio_bp)
app.register_blueprint(pedido_bp)
app.register_blueprint(finalizar_bp)
app.register_blueprint(cadastro_bp)
app.register_blueprint(login_bp)

if __name__ == "__main__":
    app.run()
