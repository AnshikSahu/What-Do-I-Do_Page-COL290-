import mysql.connector

mydb= mysql.connector.connect(
        host= "localhost",
        user="root",
        password="my-secret-password",
        auth_plugin='mysql_native_password',
        database="photons"
        )

