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
                self.menu_director()
            elif o == '3':
                self.menu_genero()
            elif o == '4':
                #self.menu_pelicula()
                pass
            elif o == '0':
                self.view.end()
                return
            else:
                self.view.opcion_invalid()
    
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
            
    """
    ************************
    * Director controllers *
    ************************
    """
    def menu_director(self):
        while True:
            self.view.menu_director()
            self.view.select_opcion()
            o = input()
            if o == '1':
                self.create_director()
            elif o == '2':
                self.read_director()
            elif o == '3':
                self.read_all_directores()
            elif o == '4':
                self.read_directores_nombre()
            elif o == '5':
                self.update_director()
            elif o == '6':
                self.delete_director()
            elif o == '0':
                return
            else:
                self.view.opcion_invalid()

    def ask_director(self):
        self.view.ask('Nombre(s): ')
        d_name = input()
        self.view.ask('Apellido paterno: ')
        d_apellido1 = input()
        self.view.ask('Apellido materno: ')
        d_apellido2 = input()
        self.view.ask('Fecha de nacimiento (AAAA-MM-DD): ')
        d_birth = input()
        self.view.ask('Sexo (H, M): ')
        d_sexo = input()
        self.view.ask('País: ')
        d_pais = input()
        return [d_name, d_apellido1, d_apellido2, d_birth, d_sexo, d_pais]
    
    def create_director(self):
        d_name, d_apellido1, d_apellido2, d_birth, d_sexo, d_pais = self.ask_director()
        out = self.model.create_director(d_name, d_apellido1, d_apellido2, d_birth, d_sexo, d_pais)
        if out == True:
            self.view.ok(d_name+' '+d_apellido1, 'agregó')
        else:
            self.view.error('No se pudo agregar al director.')
        return
    
    def read_director(self):
        self.view.ask('ID del director: ')
        d_id = input()
        director = self.model.read_director(d_id)
        if type(director) == tuple:
            self.view.mostrar_director_header(' Datos del director '+d_id+' ')
            self.view.mostrar_un_director(director)
            self.view.mostrar_director_midder()
            self.view.mostrar_director_footer()
        else:
            if director == None:
                self.view.error('El director NO existe.')
            else:
                self.view.error('Problema para leer director.')
        return

    def read_all_directores(self):
        directores = self.model.read_all_directores()
        if type(directores) == list:
            self.view.mostrar_todos_directores(directores)
        else:
            self.view.error('Error al leer todos los directores.')
        return
    
    def read_directores_nombre(self):
        self.view.ask('Nombre(s) del director: ')
        d_nombre = input()
        directores = self.model.read_directores_nombre(d_nombre)
        if type(directores) == list:
            self.view.mostrar_director_header(' Directores cuyo nombre es '+d_nombre+' ')
            for director in directores:
                self.view.mostrar_un_director(director)
                self.view.mostrar_director_midder()
            self.view.mostrar_director_footer()
        else:
            self.view.error('Error al leer lista de directores.')
        return
    
    def update_director(self):
        self.view.ask('ID de director a modificar: ')
        d_id = input()
        director = self.model.read_director(d_id)
        if type(director) == tuple:
            self.view.mostrar_director_header(' Datos del director '+d_id+' ')
            self.view.mostrar_un_director(director)
            self.view.mostrar_director_midder()
            self.view.mostrar_director_footer()
        else:
            if director == None:
                self.view.error('El director NO existe.')
            else:
                self.view.error('Problema para leer director.')
            return
        self.view.msg('Ingresa los valores a modificar (vacío para dejarlo igual):')
        d_name, d_apellido1, d_apellido2, d_birth, d_sexo, d_pais = self.ask_director()
        out = self.model.update_director(d_id, d_name, d_apellido1, d_apellido2, d_birth, d_sexo, d_pais)
        if out == True:
            self.view.ok(d_id, 'actualizó')
        else:
            self.view.error('No se pudo actualizar el director.')
        return
    
    def delete_director(self):
        self.view.ask('ID de director a borrar: ')
        d_id = input()
        self.view.ask('¿Seguro que desea borrar a este director? (S = Sí) ')
        confirm = input()
        if confirm.lower() == 's':
            count = self.model.delete_director(d_id)
            if count != 0:
                self.view.ok(d_id, 'borró')
            else:
                if count == 0:
                    self.view.error('El director NO existe.')
                else:
                    self.view.error('Error al borrar director.')
        else:
            self.view.msg('El director no se borrará. Cancelando operación...')
        return
    
    """
    **********************
    * Genero controllers *
    **********************
    """
    def menu_genero(self):
        while True:
            self.view.menu_genero()
            self.view.select_opcion()
            o = input()
            if o == '1':
                self.create_genero()
            elif o == '2':
                self.read_genero()
            elif o == '3':
                self.read_all_generos()
            elif o == '4':
                self.read_genero_nombre()
            elif o == '5':
                self.update_genero()
            elif o == '6':
                self.delete_genero()
            elif o == '0':
                return
            else:
                self.view.opcion_invalid()

    def ask_genero(self):
        self.view.ask('Descripción/Categoría: ')
        g_descripcion = input()
        return g_descripcion
    
    def create_genero(self):
        g_descripcion = self.ask_genero()
        out = self.model.create_genero(g_descripcion)
        if out == True:
            self.view.ok(g_descripcion, 'agregó')
        else:
            self.view.error('No se pudo agregar este género.')
        return
    
    def read_genero(self):
        self.view.ask('ID del género: ')
        g_id = input()
        genero = self.model.read_genero(g_id)
        if type(genero) == tuple:
            self.view.mostrar_genero_header(' Datos del género '+g_id+' ')
            self.view.mostrar_un_genero(genero)
            self.view.mostrar_genero_midder()
            self.view.mostrar_genero_footer()
        else:
            if genero == None:
                self.view.error('Este género NO existe.')
            else:
                self.view.error('Problema para leer género.')
        return

    def read_all_generos(self):
        generos = self.model.read_all_generos()
        if type(generos) == list:
            self.view.mostrar_todos_generos(generos)
        else:
            self.view.error('Error al leer todos los géneros.')
        return
    
    def read_genero_nombre(self):
        self.view.ask('Descripción del género: ')
        g_descripcion = input()
        genero = self.model.read_genero_nombre(g_descripcion)
        if type(genero) == tuple:
            self.view.mostrar_genero_header(' Género '+g_descripcion+' registrado ')
            self.view.mostrar_un_genero(genero)
            self.view.mostrar_genero_midder()
            self.view.mostrar_genero_footer()
        else:
            if genero == None:
                self.view.error('Este género NO existe.')
            else:
                self.view.error('Problema para leer género.')
        return
    
    def update_genero(self):
        self.view.ask('ID del género: ')
        g_id = input()
        genero = self.model.read_genero(g_id)
        if type(genero) == tuple:
            self.view.mostrar_genero_header(' Datos del género '+g_id+' ')
            self.view.mostrar_un_genero(genero)
            self.view.mostrar_genero_midder()
            self.view.mostrar_genero_footer()
        else:
            if genero == None:
                self.view.error('Este género NO existe.')
            else:
                self.view.error('Problema para leer género.')
            return
        self.view.msg('Ingresa la nueva descripción (vacío para dejarla igual):')
        g_descripcion = self.ask_genero()
        out = self.model.update_genero(g_id, g_descripcion)
        if out == True:
            self.view.ok(g_id, 'actualizó')
        elif out == False:
            self.view.msg('Descripción vacía. No se realizarán cambios.')
        else:
            self.view.error('No se pudo actualizar el género.')
        return
    
    def delete_genero(self):
        self.view.ask('ID del género a borrar: ')
        g_id = input()
        self.view.ask('¿Seguro que desea borrar este género? (S = Sí) ')
        confirm = input()
        if confirm.lower() == 's':
            count = self.model.delete_genero(g_id)
            if count != 0:
                self.view.ok(g_id, 'borró')
            else:
                if count == 0:
                    self.view.error('El género NO existe.')
                else:
                    self.view.error('Error al borrar género.')
        else:
            self.view.msg('El género no se borrará. Cancelando operación...')
        return