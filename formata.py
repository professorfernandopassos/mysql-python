nome = input('Insira o nome do médico: ')
crm = input('Agora, insira o CRM no médico: ')
especializacao = input('Por fim, a especialização do médico: ')

inserirMedico = f"INSERT INTO medico (`crm`,`nome`, `especializacao`) VALUES ('{crm}','{nome}','{especializacao}')"
buscarMedico = f"SELECT * from medico WHERE crm = '{crm}'"

print(inserirMedico)
print(buscarMedico)