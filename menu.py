# -*- coding: utf8 -*-
import sys
import platform
import os
from my_inbox import My_inbox


class Menu:
    """
    Despliega un menú que responde a las elecciones del usuario.
    """

    def __init__(self):
        self.my_inbox = My_inbox()
        self.options = {"1": self.add_new_arriva,
                        "2": self.message_count,
                        "3": self.get_message,
                        "4": self.get_unread_indexe,
                        "7": self.exit
                         }

    def display_menu(self):
        """ Despliega el menú principal. """
        self.clear_screen()
        print("""
                        Mensajes
                
                1. Insertar un nuevo mensaje 
                2. Cantidad total de mensajes sms en buzon
                3. Buscar mensaje  
                4. Listar todos los SMS sin leer 
                5. Eliminar mensaje
                6. Vaciar papelera
                7. Salir
                """)

    def clear_screen(self):
        """
        Verifica mediante la librería platform el sistema operativo
        del usuario y limpia la pantalla dependiendo del SO utilizado.
        """
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Darwin" or platform.system() == "Linux":
            os.system("clear")
        else:
            print("Plataforma no soportada")
    
    def press_enter(self):
        """ Realiza una pausa y solicita presionar una tecla """
        input("\nPresiona Enter para continuar")


    def run(self):
        """ Método de entrada para la aplicación """
        while True:
            self.display_menu()
            choise = input("Ingrese una opción: ")
            action = self.options.get(choise)

            if action:
                action()
            else:
                print("¡{0} no es una opción válida!".format(choise))


    def show_mensa(self, shortMessageServices=None):
        """ Despliega una nota """
        if not shortMessageServices:
            shortMessageServices = self.my_inbox.shortMessageServices

        for mensaje in shortMessageServices:
            print("Id: {0}\nEstado: '{1}'\nNumero: {2}\nFecha: {3}\nContenido: {4}"
                  .format(mensaje.id,mensaje.has_been_viewed, mensaje.from_number, mensaje.time_arrived, mensaje.text_of_sms))

    def get_message(self):
        """ Busca un mensaje mediante el numero de telefono """
        filter = input("Ingresa numero: ")
        mensaje = self.my_inbox.search(filter)
        self.show_mensa(mensaje)
        self.press_enter()  

    def add_new_arriva(self):
        has_been_viewed = input("Ingrese el estado del mensaje")
        from_number = input("Ingrese el numero: ")
        time_arrived = input("Ingrese la hora: ")
        text_of_sms = input("Ingrese el contenido del mensaje: ")
        self.my_inbox.new_inbox(has_been_viewed,from_number, time_arrived, text_of_sms)
        print("¡Nuevo mensaje agregado!")


    def message_count(self):
        """Cuenta y muestra la cantidad de mensajes que hay en la bandeja"""
        print("Tiene {0} mensajes".format(len(self.my_inbox.shortMessageServices)))        
        self.press_enter()  

        
    def get_unread_indexe(self):
        """ Muestra todos los mensajes  """
        
        print(self.my_inbox.shortMessageServices)
        print("Tiene {0} mensajes".format(len(self.my_inbox.shortMessageServices)))
        self.press_enter()  

        return False


    def exit(self):
        """ Cierra la aplicación """
        print("Gracias por usar la mensajeria")
        sys.exit(0)


if __name__ == "__main__":
    menu = Menu()
    menu.run()

