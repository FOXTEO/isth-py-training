"""Service methods for file endpoints"""
from app.common.Constants import Constants as constantes
import os

class fileRepository:

    def get_file(self, id):
        return NotImplementedError

    def post_file(self,nombre,data):
        #Se crea la direccion en donde va a estar el archivo nuevo C:/DEV/NUEVO.TXT
        direccion = constantes.FILE_UPLOAD_PATH + "/"+ nombre
        archivo = os.makedirs(direccion)
        #se carga la informacion del usuario en forma de diccionario
        info = data.provide()
        return info
