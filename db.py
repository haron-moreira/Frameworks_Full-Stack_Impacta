from conexao import Connection

def insert(nome: str, sobrenome: str, id: int):
    open = Connection()
    conexao = open.open_connection()

    cursor = conexao.cursor()

    query = "INSERT INTO cadastro (nome, sobrenome, id) VALUES (%s, %s, %i)"
    valores = (nome, sobrenome, id)

    try:
    
        cursor.execute(query, valores)

        conexao.commit()

        cursor.close()
        conexao.close()
        return True

    except Exception as err:
        cursor.close()
        conexao.close()
        return False
    

def get(id):
    open = Connection()
    conexao = open.open_connection()

    cursor = conexao.cursor()

    query = "SELECT nome, sobrenome FROM cadastro WHERE id = %i"
    valores = (id)

    try:
    
        cursor.execute(query, valores)

        conexao.commit()

        cursor.close()
        conexao.close()
        result = cursor.fetchone()
        return {"nome": result[0], "sobrenome": result[1]}

    except Exception as err:
        cursor.close()
        conexao.close()
        return {"erro": "não encontrado"}


