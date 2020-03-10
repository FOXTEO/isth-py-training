# Empty
from app.application import file_service


def get_file(nombre):
    result = file_service.get_file(nombre)


#Esto es un post para enviar la informacion del archivo, 
def create_file(nombre, contenido):
    result = file_service.post_file(nombre, contenido)
