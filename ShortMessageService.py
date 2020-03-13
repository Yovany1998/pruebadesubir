# -*- coding: utf8 -*-
# Almacena el último id de la nota
import datetime
last_id = 0


class shortMessageService:
    """
    Representa un mensaje.
    Permite almacenar un mensaje. 
    """

    def __init__(self,has_been_viewed,from_number,time_arrived,text_of_sms=""):
        """
        Inicializa un mensaje con has_been_viewed , con el valor de from_number y la fecha
        enviadas por el usuario(separadas por espacio). Automáticamente
        inserta la fecha de creación y un id único.
        """
        self.has_been_viewed = has_been_viewed
        self.from_number = from_number
        self.creation_date = datetime.date.today()
        self.time_arrived = time_arrived
        self.text_of_sms = text_of_sms
        global last_id
        last_id += 1
        self.id = last_id 

    def search(self, filter):
        """
        Determina si la nota actual está contenida en el valor
        del filtro (distingue mayúsculas de minúsculas). 
        Retorna True si es igual o False en caso contrario.
        """
        return filter in self.from_number or filter in self.has_been_viewed
