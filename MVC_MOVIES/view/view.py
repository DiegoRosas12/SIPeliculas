class View:
    def start(self):
        print("----------------------------------")
        print("Bienvenido al sistema de peliculas")
        print("----------------------------------")
        
    def end(self):
        print("\n--------------------------------")
        print("          ¡Vuelve pronto!         ")
        print("----------------------------------")

    def menu(self):
        print("----------------------------------")
        print("          Menú Principal:         ")
        print("----------------------------------") 
        print("Elige una opción")
        print("1. Actores")
        print("2. Directores") 
        print("3. Géneros")
        print("4. Películas")
        print("0. Salir\n") 
 
    def select_opcion(self):
        print("Seleccione una opción: ", end = '') 

    def opcion_invalid(self):
        print("¡Opción invalida vuelva a intentar!") 

    def ask(self, output):
        print(output, end = '')   

    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))

    def error(self, err):
        print(' ¡ERROR! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4)) 
        
    def success(self):    
        print("Los cambios se efectuaron correctamente ")
    
    def id_invalido(self):
        print("Error. el id es invalido") 

    def mostrar_update(self):
        print("Actualiza los campos que sean necesarios")

    """
    ---------------------------------------------------------------------
    Metodos actor
    ---------------------------------------------------------------------
    """
    def menu_actor(self):
        print("----------------------------------") 
        print("           Menú Actores:          ")
        print("----------------------------------") 
        print("1. Agregar actor")
        print("2. Leer actor") 
        print("3. Leer todos los actores")
        print("4. Buscar actor por nombre")
        print("5. Actualizar actor")
        print("6. Borrar actor")  
        print("0. Salir\n")

    def mostrar_un_actor(self, actor):
        print('ID: ', actor[0])
        print('Nombre: ', actor[1])
        print('Apellido Paterno: ', actor[2])
        print('Apellido Materno: ', actor[3])
        print('Fecha de nacimiento: ', actor[4])
        print('Sexo: ', actor[5])
        print('País: ', actor[6])

    def mostrar_todos_actores(self, actores):
        print('\n' + 'ID'.ljust(3) + '|' + 'Nombre(s)'.ljust(10) + '|' + 'A. Paterno'.ljust(10)+ '|'+'A. Materno'.ljust(10) +'|País'.ljust(16)+'|'+'Fecha nacimiento'.ljust(10)+'|' +' Sexo'.ljust(1)+'|')   
        print('-'*76)
        for record in actores:
            print(f'{record[0]:<3}|{record[1]:<10}|{record[2]:<10}|{record[3]:<10}|{record[6]:<15}|   {record[4]}   |{record[5]}|')
        print('-'*76)
    
    def mostrar_actor_header(self, header):
        print(header.center(76,'*'))
        print('-'*76)
    
    def mostrar_actor_midder(self):
        print('-'*76)

    def mostrar_actor_footer(self):
        print('*'*76)


    """
    -----------------------------------------------------------
    Metodos directores
    -----------------------------------------------------------
    """
    
    def menu_director(self):
        print("\n---------------------")
        print("    Menú Directores:  ")
        print("---------------------") 
        print("1. Agregar director")
        print("2. Leer director") 
        print("3. Leer todos los directores")
        print("4. Buscar director por nombre")
        print("5. Actualizar director")
        print("6. Borrar director")  
        print("0. Salir\n")

    def mostrar_un_director(self, director):
        print('ID: ', director[0])
        print('Nombre: ', director[1])
        print('Apellido Paterno: ', director[2])
        print('Apellido Materno: ', director[3])
        print('Fecha de nacimiento: ', director[4])
        print('Sexo: ', director[5])
        print('País: ', director[6])


    def mostrar_todos_directores(self, directores):
        print('\n' + 'ID'.ljust(3) + '|' + 'Nombre(s)'.ljust(10) + '|' + 'A. Paterno'.ljust(10)+ '|'+'A. Materno'.ljust(10) +'|País'.ljust(16)+'|'+'Fecha nacimiento'.ljust(10)+'|' +' Sexo'.ljust(1)+'|')   
        print('-'*76)
        for record in directores:
            print(f'{record[0]:<3}|{record[1]:<10}|{record[2]:<10}|{record[3]:<10}|{record[6]:<15}|   {record[4]}   |{record[5]}|')
        print('-'*76)
    
    def mostrar_director_header(self, header):
        print(header.center(76,'*'))
        print('-'*76)
    
    def mostrar_director_midder(self):
        print('-'*76)

    def mostrar_director_footer(self):
        print('*'*76)

    
    """
    -----------------------------------------------------------
    Metodos género
    -----------------------------------------------------------
    """
    
    def menu_genero(self):
        print("\n---------------------")
        print("    Menú Género:  ")
        print("---------------------") 
        print("1. Agregar género")
        print("2. Leer género") 
        print("3. Leer todos los géneros")
        print("4. Buscar género por nombre")
        print("5. Actualizar género")
        print("6. Borrar género")
        print("0. Salir\n") 

    def mostrar_un_genero(self, genero):
        print('ID: ', genero[0])
        print('Descripción: ', genero[1])

    def mostrar_todos_generos(self, generos):
        print('\n' + 'ID'.ljust(4) + '|' + 'Descripción'.ljust(25))   

        for record in generos:
            print(f'{record[0]:<4}|{record[1]:<25}|')
        print('-'*29)
    
    def mostrar_genero_header(self, header):
        print(header.center(29,'*'))
        print('-'*29)
    
    def mostrar_genero_midder(self):
        print('-'*29)

    def mostrar_genero_footer(self):
        print('*'*29)

    
    """
    -----------------------------------------------------------
    Metodos peliculas
    -----------------------------------------------------------
    """
    
    def menu_pelicula(self):
        print("\n---------------------")
        print("    Menú Películas:  ")
        print("---------------------") 
        print("1. Agregar pelicula")
        print("2. Leer pelicula") 
        print("3. Leer todos las peliculas")
        print("4. Buscar pelicula por titulo")
        print("5. Actualizar pelicula")
        print("6. Borrar pelicula")
        print("0. Salir\n") 

    def mostrar_una_pelicula(self, pelicula):
        print('ID: ', pelicula[0])
        print('Género: ', pelicula[1])
        print('Director: ', pelicula[2])
        print('Titulo: ', pelicula[3])
        print('Sinopsis: ', pelicula[4])
        print('Duración: ', pelicula[5])
        print('Fecha estreno: ', pelicula[6])
        print('Clasificación: ', pelicula[7])
        print('País: ', pelicula[8])

    def mostrar_todas_peliculas(self, peliculas):
        print('\n' + 'ID'.ljust(4) + '|' + 'Género'.ljust(15) + '|' + 'Director'.ljust(15)+ '|'+'Titulo'.ljust(15)+'|'+'Sinopsis'.ljust(20)+'|' +' Duración'.ljust(8)+'|' +' Fecha estreno'.ljust(8)+'|' +' Clasificación'.ljust(4)+'|' +' País'.ljust(15))   

        for record in peliculas:
            print(f'{record[0]:<4}|{record[1]:<15}|{record[2]:<15}|{record[3]:<15}|{record[4]:<20}|{record[5]:<8}|{record[6]:<8}|{record[6]:<4}|{record[6]:<15}')
        print('-'*104)
    
    def mostrar_pelicula_header(self, header):
        print(header.center(104,'*'))
        print('-'*104)
    
    def mostrar_pelicula_midder(self):
        print('-'*104)

    def mostrar_pelicula_footer(self):
        print('*'*104)

    
    """
    -----------------------------------------------------------
    Metodos actores_pelicula (Roles)
    -----------------------------------------------------------
    """
    
    def menu_rol(self):
        print("\n---------------------")
        print("    Menú Roles:  ")
        print("---------------------") 
        print("1. Agregar rol")
        print("2. Leer rol") 
        print("3. Leer todos los rols")
        print("4. Buscar rol por nombre")
        print("5. Actualizar rol")
        print("6. Borrar rol")
        print("0. Salir\n") 

    def mostrar_un_rol(self, rol):
        print('Pelicula: ', rol[0])
        print('Actor: ', rol[1])
        print('Personaje: ', rol[2])
        print('Rol: ', rol[3])

    def mostrar_todos_roles(self, roles):
        print('\n' + 'Pelicula'.ljust(5) + '|' + 'Actor'.ljust(20) + '|' + 'Personaje'.ljust(15)+ '|'+'Rol'.ljust(15))   

        for record in roles:
            print(f'{record[0]:<5}|{record[1]:<20}|{record[2]:<15}|{record[3]:<15}|')
        print('-'*55)
    
    def mostrar_rol_header(self, header):
        print(header.center(55,'*'))
        print('-'*55)
    
    def mostrar_rol_midder(self):
        print('-'*55)

    def mostrar_rol_footer(self):
        print('*'*55)

                
           
