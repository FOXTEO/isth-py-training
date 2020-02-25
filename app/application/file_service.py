# Empty
"""Methods for altering the file tables"""
from app.infrastructure import file_repository
from app.domain import model as user


def get_file(nombre):
    """Get a file"""
    archivo = file_repository.get_file(nombre)
    return file_repository.get_file(nombre)


def post_file(nombre, user):
    """Create an new file"""
    if(len(user.username) < 6):
        user.username= user.nombre+user.apellido
    user.username.capitalize()
    return file_repository.post_file(nombre, user)
