import mysql.connector

cnx = mysql.connector.connect(host='localhost', database='exemplos', user='root', password='123')
cursor = cnx.cursor()

query = "select * from medico"

cursor.execute(query)

for linha in cursor:
    print(linha)

print(cursor)
print(type(cursor))

# inserirMedico = "INSERT INTO medico (`crm`,`nome`, `especializacao`) VALUES ('334343','Alberto','Pneumologista')"

# cursor.execute(inserirMedico)

# cnx.commit()

cursor.close()
cnx.close()