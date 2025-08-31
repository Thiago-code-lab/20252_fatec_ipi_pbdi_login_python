import psycopg

class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

def existe(usuario):
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="20252_pessoal_db_login",  # ← MANTENHA ESTE (ou use o correto)
        user="postgres",
        password="1234"
    ) as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                'SELECT * FROM tb_usuario WHERE login=%s AND senha=%s',
                (usuario.login, usuario.senha)
            )
            result = cursor.fetchone()
            return result is not None

def inserir_usuario(login, senha):
    try:
        with psycopg.connect(
            host="localhost",
            port=5432,
            dbname="20252_pessoal_db_login",  # ← ALTEREI PARA O MESMO DA FUNÇÃO EXISTE()
            user="postgres",
            password="1234"  # ← ALTEREI PARA A MESMA SENHA DA FUNÇÃO EXISTE()
        ) as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO tb_usuario (login, senha) VALUES (%s, %s)',
                    (login, senha)
                )
                conexao.commit()
                print("Usuário inserido com sucesso!")
    except Exception as e:
        print("Erro ao inserir usuário:", e)

def menu():
    texto = "0-Fechar Sistema\n1-Login\n2-Logoff\n3-Inserir Usuário\n"
    usuario = None
    op = int(input(texto))
    while op != 0:
        if op == 1:
            login = input("Digite seu login\n")
            senha = input("Digite sua senha\n")
            usuario = Usuario(login, senha)
            print("Usuário OK!!!" if existe(usuario) else "Usuário NOK!!!")
        elif op == 2:
            usuario = None
            print("Logoff realizado com sucesso")
        elif op == 3:
            login = input("Digite o novo login\n")
            senha = input("Digite a nova senha\n")
            inserir_usuario(login, senha)
        else:
            print("Opção inválida!")
        op = int(input(texto))
    print("Até mais")

menu()