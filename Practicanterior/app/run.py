from app.adaptor import file_routes as file
from app.domain.model import Usuario


user = Usuario()
#Informacion del usuario, con un diccionario
info = {"Username":"JAley", "Nombre":"Jose", "Apellido":"Aley"}
user.load(info)


print(file.create_file("nuevo.txt", user))

print('Iniciando')
