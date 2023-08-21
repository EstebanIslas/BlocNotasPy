import datetime
import hashlib #Cifrado de pwd
import bd.conexion as connection

conn = connection.connect()
cnbd = conn[0]
sql = conn[1]

class User:

    def __init__(self, name, last_name, email, password):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password

    def register(self):
        date = datetime.datetime.now()

        #Cifrado de Password
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8')) #Cifrar enviando el parametro en bytes

        query = "INSERT INTO users VALUES(null, %s, %s, %s, %s, %s)"
        user = (self.name, self.last_name, self.email, cifrado.hexdigest(), date)

        try:
            sql.execute(query, user)
            cnbd.commit() #Conexion a la bd y ejecutar la consulta
            result = [sql.rowcount, self]
        except:
            result = [0, self]

        return result

    def identificar(self):
        
        #Validar en bd
        query = "SELECT * FROM users WHERE email = %s AND password = %s"

        #Cifrado de Password
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8')) #Cifrar enviando el parametro en bytes

        #Data Consult
        user = (self.email, cifrado.hexdigest())

        sql.execute(query, user)
        result = sql.fetchone()

        return result