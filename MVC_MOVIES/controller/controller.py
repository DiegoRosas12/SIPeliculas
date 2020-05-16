from model.model import Model
from view.view import View
from datetime import date

class Controller:
    """
    *******************************
    * A controller for a movie DB *
    *******************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.menu()

    """
    **********************
    * General controller *
    **********************
    """
    def menu(self):
        while True:
            self.view.menu()
            self.view.select_opcion()
            o = input()
            if o == '1':
                self.menu_actor()
            elif o == '2':
                #self.menu_director()
                pass
            elif o == '3':
                #self.menu_genero()
                pass
            elif o == '4':
                #self.menu_pelicula()
                pass
            elif o == '0':
                self.view.end()
                break
            else:
                self.view.opcion_invalid()
        return
    
    """
    *********************
    * Actor controllers *
    *********************
    """
    def menu_actor(self):
        while True:
            self.view.menu_actor()
            self.view.select_opcion()
            o = input()
            if o == '1':
                self.create_actor()
            elif o == '2':
                self.read_actor()
            elif o == '3':
                self.read_all_actores()
            elif o == '4':
                self.read_actores_nombre()
            elif o == '5':
                self.update_actor()
            elif o == '6':
                self.delete_actor()
            elif o == '0':
                return
            else:
                self.view.opcion_invalid()
        return
    
    def ask_actor(self):
        self.view.ask('Nombre(s): ')
        a_name = input()
        self.view.ask('Apellido paterno: ')
        a_apellido1 = input()
        self.view.ask('Apellido materno: ')
        a_apellido2 = input()
        self.view.ask('Fecha de nacimiento (AAAA-MM-DD): ')
        a_birth = input()
        self.view.ask('Sexo (H, M): ')
        a_sexo = input()
        self.view.ask('País: ')
        a_pais = input()
        return [a_name, a_apellido1, a_apellido2, a_birth, a_sexo, a_pais]
    
    def create_actor(self):
        a_name, a_apellido1, a_apellido2, a_birth, a_sexo, a_pais = self.ask_actor()
        out = self.model.create_actor(a_name, a_apellido1, a_apellido2, a_birth, a_sexo, a_pais)
        if out == True:
            self.view.ok(a_name+' '+a_apellido1, 'agregó')
        else:
            self.view.error('No se pudo agregar al actor.')
        return
    
    def read_actor(self):
        self.view.ask('ID del actor: ')
        a_id = input()
        actor = self.model.read_actor(a_id)
        if type(actor) == tuple:
            self.view.mostrar_actor_header(' Datos del actor '+a_id+' ')
            self.view.mostrar_un_actor(actor)
            self.view.mostrar_actor_midder()
            self.view.mostrar_actor_footer()
        else:
            if actor == None:
                self.view.error('El actor NO existe.')
            else:
                self.view.error('Problema para leer actor.')
        return

    def read_all_actores(self):
        actores = self.model.read_all_actores()
        if type(actores) == list:
            self.view.mostrar_todos_actores(actores)
        else:
            self.view.error('Error al leer todos los actores.')
        return
    
    def read_actores_nombre(self):
        self.view.ask('Nombre(s) del actor: ')
        a_nombre = input()
        actores = self.model.read_actores_nombre(a_nombre)
        if type(actores) == list:
            self.view.mostrar_actor_header(' Actores cuyo nombre es '+a_nombre+' ')
            for actor in actores:
                self.view.mostrar_un_actor(actor)
                self.view.mostrar_actor_midder()
            self.view.mostrar_actor_footer()
        else:
            self.view.error('Error al leer lista de actores.')
        return
    
    def update_actor(self):
        self.view.ask('ID de actor a modificar: ')
        a_id = input()
        actor = self.model.read_actor(a_id)
        if type(actor) == tuple:
            self.view.mostrar_actor_header(' Datos del actor '+a_id+' ')
            self.view.mostrar_un_actor(actor)
            self.view.mostrar_actor_midder()
            self.view.mostrar_actor_footer()
        else:
            if actor == None:
                self.view.error('El actor NO existe.')
            else:
                self.view.error('Problema para leer actor.')
            return
        self.view.msg('Ingresa los valores a modificar (vacío para dejarlo igual):')
        a_name, a_apellido1, a_apellido2, a_birth, a_sexo, a_pais = self.ask_actor()
        out = self.model.update_actor(a_id, a_name, a_apellido1, a_apellido2, a_birth, a_sexo, a_pais)
        if out == True:
            self.view.ok(a_id, 'actualizó')
        else:
            self.view.error('No se pudo actualizar el actor.')
        return
    
    def delete_actor(self):
        self.view.ask('ID de actor a borrar: ')
        a_id = input()
        self.view.ask('¿Seguro que desea borrar a este actor? (S = Sí) ')
        confirm = input()
        if confirm.lower() == 's':
            count = self.model.delete_actor(a_id)
            if count != 0:
                self.view.ok(a_id, 'borró')
            else:
                if count == 0:
                    self.view.error('El actor NO existe.')
                else:
                    self.view.error('Error al borrar actor.')
        else:
            self.view.msg('El actor no se borrará. Cancelando operación...')
        return