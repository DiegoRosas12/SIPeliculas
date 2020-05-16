from mysql import connector

# TODO: Cambiar todos los select para leer los nombres en lugar de los ids
class Model:

    ##################     configuracion de la base          ###################
    ############################################################################

    def __init__(self,config_db_file = 'config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()
    
    def read_config_db(self):
        d ={}

        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close() 

    ######################     metodos de actores          ###################
    ##########################################################################
    def create_actor(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, pais):
        try:
            if apellido_materno != '':
                sql = 'INSERT INTO actores(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, pais) VALUES(%s,%s,%s,%s,%s,%s);'
                values = (nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, pais)
            else:
                sql = 'INSERT INTO actores(nombre, apellido_paterno, fecha_nacimiento, sexo, pais) VALUES(%s,%s,%s,%s,%s);'
                values = (nombre, apellido_paterno, fecha_nacimiento, sexo, pais)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)   

    def read_actor(self, id):
        try:
            sql = 'SELECT * FROM actores WHERE id_actor = %s;'
            values = (id,)
            self.cursor.execute(sql, values)
            actor = self.cursor.fetchone()

            return actor
        except connector.Error as err:
            print(err)
            return (err)

    def read_actores_nombre(self, nombre):
        try:
            sql = 'SELECT * FROM actores WHERE nombre LIKE %s;'
            values = (nombre,)
            self.cursor.execute(sql, values)
            actores = self.cursor.fetchall()

            return actores
        except connector.Error as err:
            print(err)
            return (err)


    def read_all_actores(self):
        try:
            sql = 'SELECT * FROM actores;'
            self.cursor.execute(sql)
            actores = self.cursor.fetchall()

            return actores
        except connector.Error as err:
            print(err)
            return (err)  

    def update_actor(self, id, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, pais):
        fields = []
        val = []

        if nombre !='':
            val.append(nombre)
            fields.append('nombre = %s')
        if apellido_paterno !='':
            val.append(apellido_paterno)
            fields.append('apellido_paterno = %s')
        if apellido_materno != '':
            val.append(apellido_materno)
            fields.append('apellido_materno = %s')
        if fecha_nacimiento != '':
            val.append(fecha_nacimiento)
            fields.append('fecha_nacimiento = %s')
        if sexo != '':
            val.append(sexo)
            fields.append('sexo = %s') 
        if pais != '':
            val.append(pais)
            fields.append('pais = %s') 

        val.append(id)
        val = tuple(val)         
        try:
            sql = 'UPDATE actores SET ' + ','.join(fields) +' WHERE id_actor = %s;'

            self.cursor.execute(sql,val)
            self.cnx.commit()

            return True


        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)

    def delete_actor(self, id):
        try:
            sql = 'DELETE  FROM actores WHERE id_actor = %s;'
            values = (id,)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            count = self.cursor.rowcount
            return count
            
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return (err)

    ######################     metodos de directores          ###################
    ##########################################################################
    def create_director(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, pais):
        try:
            sql = 'INSERT INTO directores(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, pais) VALUES(%s,%s,%s,%s,%s,%s);'
            values = (nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, pais,)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return(err)   

    def read_director(self, id):
        try:
            sql = 'SELECT * FROM directores WHERE id_director = %s;'
            values = (id,)
            self.cursor.execute(sql, values)
            director = self.cursor.fetchone()

            return director
        except connector.Error as err:
            return (err)  

    def read_directores_nombre(self, nombre):
        try:
            sql = 'SELECT * FROM actores WHERE nombre LIKE %s;'
            values = (nombre,)
            self.cursor.execute(sql, values)
            directores = self.cursor.fetchall()

            return directores
        except connector.Error as err:
            print(err)
            return (err)

    def read_all_directores(self):
        try:
            sql = 'SELECT * FROM directores;'
            self.cursor.execute(sql)
            director = self.cursor.fetchall()

            return director
        except connector.Error as err:
            return (err)


    def update_director(self, id, nombre = '', apellido_paterno = '', apellido_materno = '', fecha_nacimiento = '', sexo = '', pais= ''):
        fields = []
        val = []

        if nombre !='':
            val.append(nombre)
            fields.append('nombre = %s')
        if apellido_paterno !='':
            val.append(apellido_paterno)
            fields.append('apellido_paterno = %s')
        if apellido_materno != '':
            val.append(apellido_materno)
            fields.append('apellido_materno = %s')
        if fecha_nacimiento != '':
            val.append(fecha_nacimiento)
            fields.append('fecha_nacimiento = %s')
        if sexo != '':
            val.append(sexo)
            fields.append('sexo = %s') 
        if pais != '':
            val.append(pais)
            fields.append('pais = %s') 

        val.append(id)
        val = tuple(val)         
        try:
            sql = 'UPDATE directores SET ' + ','.join(fields) +' WHERE id_director =%s;'

            self.cursor.execute(sql,val)
            self.cnx.commit()

            return True


        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def delete_director(self, id):
        try:
            sql = 'DELETE  FROM directores WHERE id_director = %s;'
            values = (id,)
            print(sql,values)
            self.cursor.execute(sql, values)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count

        except connector.Error as err:
            self.cnx.rollback()
            return (err)
    
    ######################     metodos de generos          ###################
    ##########################################################################

    def create_genero(self, descripcion):
        try:
            sql = 'INSERT INTO generos(descripcion) VALUES(%s);'
            values = (descripcion,)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)   

    def read_genero(self, id):
        try:
            sql = 'SELECT * FROM generos WHERE id_genero = %s;'
            values = (id,)
            self.cursor.execute(sql, values)
            genero = self.cursor.fetchone()

            return genero
        except connector.Error as err:
            return (err)
    
    def read_genero_nombre(self, nombre):
        try:
            sql = 'SELECT * FROM generos WHERE descripcion LIKE %s;'
            values = (nombre,)
            self.cursor.execute(sql, values)
            genero = self.cursor.fetchone()

            return genero
        except connector.Error as err:
            print(err)
            return (err)

    def read_all_generos(self):
        try:
            sql = 'SELECT * FROM generos;'
            self.cursor.execute(sql)
            generos = self.cursor.fetchall()

            return generos
        except connector.Error as err:
            return (err)  

    def update_genero(self, id, descripcion = ''):
        fields = []
        val = []

        if descripcion !='':
            val.append(descripcion)
            fields.append('descripcion = %s')

        val.append(id)
        val = tuple(val)         
        try:
            sql = 'UPDATE generos SET ' + ','.join(fields) +' WHERE id_genero = %s;'

            self.cursor.execute(sql,val)
            self.cnx.commit()

            return True


        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def delete_genero(self, id):
        try:
            sql = 'DELETE  FROM generos WHERE id_genero = %s;'
            values = (id,)

            self.cursor.execute(sql, values)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count

        except connector.Error as err:
            self.cnx.rollback()
            return (err)
    ######################     metodos de peliculas        ###################
    ##########################################################################
    def create_pelicula(self, id_genero, id_director, titulo, sinopsis, duracion, premiere, clasificacion, pais):
        try:
            sql = 'INSERT INTO peliculas(id_genero, id_director, titulo, sinopsis, duracion, premiere, clasificacion, pais) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);'
            values = (id_genero, id_director, titulo, sinopsis, duracion, premiere, clasificacion, pais)
            print(sql,values)
            self.cursor.execute(sql, values)
            self.cnx.commit()

            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)   

    def read_pelicula(self, id):
        try:
            sql = 'SELECT * FROM peliculas WHERE id_pelicula = %s;'
            values = (id,)
            self.cursor.execute(sql, values)
            pelicula = self.cursor.fetchone()

            return pelicula
        except connector.Error as err:
            return (err)
    
    def read_peliculas_titulo(self, nombre):
        try:
            sql = 'SELECT * FROM peliculas WHERE titulo LIKE %s;'
            values = (nombre,)
            self.cursor.execute(sql, values)
            peliculas = self.cursor.fetchone()

            return peliculas
        except connector.Error as err:
            print(err)
            return (err)

    def read_all_peliculas(self):
        try:
            sql = 'SELECT p.id_pelicula, g.descripcion, d.apellido_paterno, p.titulo, p.sinopsis, p.duracion, p.premiere, p.clasificacion, p.pais FROM peliculas p, generos g, directores d WHERE p.id_genero = g.id_genero AND p.id_director = d.id_director;'
            self.cursor.execute(sql)
            peliculas = self.cursor.fetchall()

            return peliculas
        except connector.Error as err:
            return (err)  

    def update_pelicula(self, id, id_genero = '', id_director = '', titulo = '', sinopsis = '', duracion = '', premiere = '', clasificacion = '', pais = ''):
        fields = []
        val = []

        if id_genero !='':
            val.append(id_genero)
            fields.append('id_genero = %s')
        if id_director !='':
            val.append(id_director)
            fields.append('id_director = %s')
        if titulo != '':
            val.append(titulo)
            fields.append('titulo = %s')
        if sinopsis != '':
            val.append(sinopsis)
            fields.append('sinopsis = %s')
        if duracion != '':
            val.append(duracion)
            fields.append('duracion = %s') 
        if premiere != '':
            val.append(premiere)
            fields.append('premiere = %s') 
        if clasificacion != '':
            val.append(clasificacion)
            fields.append('clasificacion = %s') 
        if pais != '':
            val.append(pais)
            fields.append('pais = %s') 

        val.append(id)
        val = tuple(val)         
        try:
            sql = 'UPDATE peliculas SET ' + ','.join(fields) +' WHERE id_pelicula =%s;'

            self.cursor.execute(sql,val)
            self.cnx.commit()

            return True


        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def delete_pelicula(self, id):
        try:
            sql = 'DELETE  FROM peliculas WHERE id_pelicula = %s;'
            values = (id,)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            count = self.cursor.rowcount
            return count
            
        except connector.Error as err:
            self.cnx.rollback()
            return (err)

    ######################   metodos de actores_pelicula (roles)     #################
    ##########################################################################
    def create_rol(self, id_pelicula, id_actor, personaje, rol):
        try:
            sql = 'INSERT INTO roles(id_pelicula, id_actor, personaje, rol) VALUES(%s,%s,%s,%s);'
            values = (id_pelicula, id_actor, personaje, rol)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)   

    def read_un_rol(self, id_pelicula, id_actor):
        try:
            sql = 'SELECT p.id_pelicula, p.titulo, a.id_actor, a.nombre, r.personaje, r.rol FROM roles r, peliculas p, actores a WHERE p.id_pelicula = r.id_pelicula AND a.id_actor = r.id_actor AND r.id_pelicula = %s AND r.id_actor = %s;'
            values = (id_pelicula, id_actor)
            self.cursor.execute(sql, values)
            rol = self.cursor.fetchone()

            return rol
        except connector.Error as err:
            return (err)
    
    def read_roles_nombre(self, nombre):
        try:
            sql = 'SELECT * FROM roles WHERE rol LIKE %s;'
            values = (nombre,)
            self.cursor.execute(sql, values)
            roles = self.cursor.fetchone()

            return roles
        except connector.Error as err:
            print(err)
            return (err)

    def read_all_roles(self):
        try:
            sql = 'SELECT p.id_pelicula, p.titulo, a.id_actor, a.nombre, r.personaje, r.rol FROM roles r, peliculas p, actores a WHERE p.id_pelicula = r.id_pelicula AND a.id_actor = r.id_actor'
            self.cursor.execute(sql)
            roles = self.cursor.fetchall()

            return roles
        except connector.Error as err:
            return (err)  

    def update_rol(self, id_pelicula, id_actor, personaje = '', rol = ''):
        fields = []
        val = []

        if personaje !='':
            val.append(personaje)
            fields.append('personaje = %s')
        if rol !='':
            val.append(rol)
            fields.append('rol = %s')
        

        val.append(id_pelicula)
        val.append(id_actor)
        val = tuple(val)         
        try:
            sql = 'UPDATE roles SET ' + ','.join(fields) +' WHERE id_pelicula =%s and id_actor = %s;'
            self.cursor.execute(sql,val)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def delete_rol(self, id_pelicula, id_actor):
        try:
            sql = 'DELETE  FROM roles WHERE id_pelicula = %s AND id_actor = %s;'
            values = (id_pelicula, id_actor)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            count = self.cursor.rowcount
            return count
            
        except connector.Error as err:
            self.cnx.rollback()
            return (err)         
    

