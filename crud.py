from database import conectar
from sqlite3 import Error


def criar_tabela_tarefas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            concluida INTEGER DEFAULT 0  
            )
    """)
    conn.commit()
    conn.close()



def criar_tarefa(titulo, descricao, concluida=0):
    conn = conectar()
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO tarefas(titulo, descricao, concluida) VALUES (?,?,?)", 
                       (titulo, descricao, concluida))
        conn.commit()
        return True
    except Error as e:
        print(e)
        return None
    finally:
        conn.close()

