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
            sql = 'INSERT INTO actores(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, pais) VALUES(%s,%s,%s,%s,%s,%s)'
            values = (nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, pais)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)   

    def read_actor(self, id):
        try:
            sql = 'SELECT * FROM actores WHERE id_actor = %s'
            values = (id,)
            self.cursor.execute(sql, values)
            actor = self.cursor.fetchone()

            return actor
        except connector.Error as err:
            return (err)

    def read_actor_name(self, name):
        try:
            sql = 'SELECT * FROM actores WHERE nombre LIKE %s'
            values = (name,)
            self.cursor.execute(sql, values)
            actor = self.cursor.fetchone()

            return actor
        except connector.Error as err:
            return (err)


    def read_all_actores(self):
        try:
            sql = 'SELECT * FROM actores'
            self.cursor.execute(sql)
            actor = self.cursor.fetchall()

            return actor
        except connector.Error as err:
            return (err)  

    def update_actor(self, id, nombre = '', apellido_paterno = '', apellido_materno = '', fecha_nacimiento = '', sexo = '', pais= ''):
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
            sql = 'UPDATE actores SET ' + ','.join(fields) +' WHERE id_actor =%s'

            self.cursor.execute(sql,val)
            self.cnx.commit()

            return True


        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def delete_actor(self, id):
        try:
            sql = 'DELETE  FROM actores WHERE id_actor = %s'
            values = (id,)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            count = self.cursor.rowcount
            return count
            
        except connector.Error as err:
            self.cnx.rollback()
            return (err)

    ######################     metodos de directores          ###################
    ##########################################################################
    def create_director(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, pais):
        try:
            sql = 'INSERT INTO directores(nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, pais) VALUES(%s,%s,%s,%s,%s,%s)'
            values = (nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, pais)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)   

    def read_director(self, id):
        try:
            sql = 'SELECT * FROM directores WHERE id_director = %s'
            values = (id,)
            self.cursor.execute(sql, values)
            director = self.cursor.fetchone()

            return director
        except connector.Error as err:
            return (err)  

    def read_director_name(self, id):
        try:
            sql = 'SELECT * FROM directores WHERE nombre LIKE %s'
            values = (id,)
            self.cursor.execute(sql, values)
            director = self.cursor.fetchone()

            return director
        except connector.Error as err:
            return (err) 

    def read_all_directores(self):
        try:
            sql = 'SELECT * FROM directores'
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
            sql = 'UPDATE directores SET ' + ','.join(fields) +' WHERE id_director =%s'

            self.cursor.execute(sql,val)
            self.cnx.commit()

            return True


        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def delete_director(self, id):
        try:
            sql = 'DELETE  FROM directores WHERE id_director = %s'
            values = (id,)

            self.cursor.execute(sql, values)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count

        except connector.Error as err:
            self.cnx.rollback()
            return (err)
    
    ######################     metodos de generos          ###################
    ##########################################################################

    def create_genero(self, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo, pais):
        try:
            sql = 'INSERT INTO generos(descripcion) VALUES(%s)'
            values = (descripcion)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)   

    def read_genero(self, id):
        try:
            sql = 'SELECT * FROM generos WHERE id_genero = %s'
            values = (id,)
            self.cursor.execute(sql, values)
            genero = self.cursor.fetchone()

            return genero
        except connector.Error as err:
            return (err)  

    def read_all_generos(self):
        try:
            sql = 'SELECT * FROM generos'
            self.cursor.execute(sql)
            genero = self.cursor.fetchall()

            return genero
        except connector.Error as err:
            return (err)  

    def update_genero(self, id, descripcion = ''):
        fields = []
        val = []

        if descripcion !='':
            val.append(nombre)
            fields.append('nombre = %s')

        val.append(id)
        val = tuple(val)         
        try:
            sql = 'UPDATE generos SET ' + ','.join(fields) +' WHERE id_genero =%s'

            self.cursor.execute(sql,val)
            self.cnx.commit()

            return True


        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def delete_genero(self, id):
        try:
            sql = 'DELETE  FROM generos WHERE id_genero = %s'
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
    def create_pelicula(self, id_genero, id_director, titulo, sinopsis, premiere, duracion):
        try:
            sql = 'INSERT INTO peliculas(id_genero, id_director, titulo, sinopsis, premiere, duracion) VALUES(%s,%s,%s,%s,%s,%s)'
            values = (id_genero, id_director, titulo, sinopsis, premiere, duracion)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)   

    def read_pelicula(self, id):
        try:
            sql = 'SELECT * FROM peliculas WHERE id_pelicula = %s'
            values = (id,)
            self.cursor.execute(sql, values)
            pelicula = self.cursor.fetchone()

            return pelicula
        except connector.Error as err:
            return (err)  

    def read_all_peliculas(self):
        try:
            sql = 'SELECT * FROM peliculas'
            self.cursor.execute(sql)
            pelicula = self.cursor.fetchall()

            return pelicula
        except connector.Error as err:
            return (err)  

    def update_pelicula(self, id, id_genero = '', id_director = '', titulo = '', sinopsis = '', premiere = '', duracion = ''):
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
        if premiere != '':
            val.append(premiere)
            fields.append('premiere = %s') 
        if duracion != '':
            val.append(duracion)
            fields.append('duracion = %s') 

        val.append(id)
        val = tuple(val)         
        try:
            sql = 'UPDATE peliculas SET ' + ','.join(fields) +' WHERE id_pelicula =%s'

            self.cursor.execute(sql,val)
            self.cnx.commit()

            return True


        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def delete_pelicula(self, id):
        try:
            sql = 'DELETE  FROM peliculas WHERE id_pelicula = %s'
            values = (id,)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            count = self.cursor.rowcount
            return count
            
        except connector.Error as err:
            self.cnx.rollback()
            return (err)

    ######################   metodos de actores_pelicula     #################
    ##########################################################################
    def create_actor_pelicula(self, id_pelicula, id_actor, personaje, rol):
        try:
            sql = 'INSERT INTO actores_peliculas(id_pelicula, id_actor, personaje, rol) VALUES(%s,%s,%s,%s)'
            values = (id_pelicula, id_actor, personaje, rol)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            return True
        except connector.Error as err:
            self.cnx.rollback()
            return(err)   

    def read_actor_pelicula(self, id_pelicula, id_actor):
        try:
            sql = 'SELECT p.titulo, a.nombre, a.apellido_paterno, a.apellido_materno, ap.personaje, ap.rol FROM actores_peliculas ac, peliculas p, actores a WHERE p.id_pelicula = ap.id_pelicula AND a.id_actor = ap.id_actor AND ap.id_pelicula = %s AND ap.id_actor = %s'
            values = (id_pelicula, id_actor)
            self.cursor.execute(sql, values)
            actor_pelicula = self.cursor.fetchone()

            return actor_pelicula
        except connector.Error as err:
            return (err)  

    def read_all_actores_peliculas(self):
        try:
            sql = 'SELECT * FROM actores_peliculas'
            self.cursor.execute(sql)
            actores_peliculas = self.cursor.fetchall()

            return actores_peliculas
        except connector.Error as err:
            return (err)  

    def update_actor_pelicula(self, id_pelicula, id_actor, id_genero = '', id_director = '', titulo = '', sinopsis = '', premiere = '', duracion = ''):
        fields = []
        val = []

        if personaje !='':
            val.append(personaje)
            fields.append('personaje = %s')
        if rol !='':
            val.append(rol)
            fields.append('rol = %s')
        

        val.append(id)
        val = tuple(val)         
        try:
            sql = 'UPDATE actores_peliculas SET ' + ','.join(fields) +' WHERE id_pelicula =%s and id_actor = %s'

            self.cursor.execute(sql,val)
            self.cnx.commit()

            return True


        except connector.Error as err:
            self.cnx.rollback()
            return(err)

    def delete_actor_pelicula(self, id_pelicula, id_actor):
        try:
            sql = 'DELETE  FROM actores_peliculas WHERE id_pelicula = %s AND id_actor = %s'
            values = (id_pelicula, id_actor)

            self.cursor.execute(sql, values)
            self.cnx.commit()

            count = self.cursor.rowcount
            return count
            
        except connector.Error as err:
            self.cnx.rollback()
            return (err)         
    

