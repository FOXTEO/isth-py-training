from app.adaptor import file_routes as file
from app.domain.model import Usuario


user = Usuario()
#Informacion del usuario
user.Apellido = "Aley"
user.Nombre = "Jose"
user.Username = "JAley"

file.create_file("nuevo.txt", user)

print('Iniciando')
