import mysql.connector

cnx = mysql.connector.connect(host='localhost', database='exemplos', user='root', password='123')
cursor = cnx.cursor()

nome = input('Insira o nome do médico: ')
crm = input('Agora, insira o CRM no médico: ')
especializacao = input('Por fim, a especialização do médico: ')

inserirMedico = f"INSERT INTO medico (`crm`,`nome`, `especializacao`) VALUES ('{crm}','{nome}','{especializacao}')"

cursor.execute(inserirMedico)

cnx.commit()

buscarMedico = f"SELECT * from medico WHERE crm = '{crm}'"

cursor.execute(buscarMedico)

for medico in cursor:
    print(f"O médico {medico[2]} {medico[1]} com CRM número {medico[0]} foi inserido com sucesso no sistema")


cursor.close()
cnx.close()