import bd.conexion as connection

#Variables de Conexion
conn = connection.connect()
cnbd = conn[0]
sql = conn[1]

class Nota:

    def __init__(self, user_id, title, description):
        self.user_id = user_id
        self.title = title
        self.description = description

    
    def save(self):
        query = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        nota = (self.user_id, self.title, self.description)

        sql.execute(query, nota)
        cnbd.commit()

        return [sql.rowcount, self]