import psycopg

try:
    conn = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="20252_pessoal_db_login",
        user="postgres",
        password="1234" 
    )
    print("Conexão bem-sucedida!")
    conn.close()
except Exception as e:
    print("Erro na conexão:", e)