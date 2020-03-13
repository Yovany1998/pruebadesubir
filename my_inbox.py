# -*- coding: utf8 -*-
from ShortMessageService import shortMessageService


class My_inbox:
    """
    Representa una colección de mensajes que pueden ser buscados.
    """

    def __init__(self):
        """ Inicializa el buzon """
        self.shortMessageServices= list()

    def new_inbox(self,has_been_viewed,from_number, time_arrived, text_of_sms=""):
        """ Un nuevo mensaje """
        self.shortMessageServices.append(shortMessageService(has_been_viewed,from_number, time_arrived, text_of_sms))

    def get_message(self, shortmessageservice_id):
        """
        Busca una nota con el id enviado.
        Esta función es privada (empieza con _).
        https://docs.python.org/2/tutorial/classes.html
        """
        for shortmessageservice in self.shortMessageServices:
            if str(shortmessageservice.id) == str(shortmessageservice_id):
                return shortmessageservice

        return shortMessageService

    def contar_mensajes(self):
        """Cuenta y muestra la cantidad de mensajes que hay en la bandeja"""
        print("Tiene {0} mensajes".format(len(self.shortMessageServices)))        

    def listar_mensajes(self):
        """ Muestra todos los mensajes  """
        print(self.shortMessageServices)
        print(len(self.shortMessageServices))

        return False




    def search(self, filter):
        """
        Busca todas las notas que satisfacen el filtro enviado.
        """
        return [shortmessageservice for shortmessageservice in self.shortMessageServices if shortmessageservice.search(filter)]
