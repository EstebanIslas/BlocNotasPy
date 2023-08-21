import mysql.connector
import datetime
import hashlib #Cifrado de pwd

#Conexion a la bd
cnbd = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="notes_python",
    port=3306
)

sql = cnbd.cursor(buffered=True) #Generar consultas

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
        return self.name