import mysql.connector

#Conexion a la bd

def connect():

    cnbd = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="notes_python",
        port=3306
    )

    sql = cnbd.cursor(buffered=True) #Generar consultas

    return [cnbd, sql]
