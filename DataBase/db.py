import psycopg2

def ObterConexao():
        return psycopg2.connect(
        dbname="NomeBanco",
        user="postgres",
        password="SUA_SENHA",
        host="localhost",
        port="5432"
    )