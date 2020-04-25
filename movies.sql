CREATE DATABASE  IF NOT exists cine_db;
use cine_bd;

CREATE TABLE IF NOT EXISTS actores(
	id_actor INT NOT NULL AUTO INCREMENT,
  nombre VARCHAR(50) NOT NULL,
	apellido_paterno VARCHAR(30) NOT NULL,
	apellido_materno VARCHAR(30),
	fecha_nacimiento DATE,
  sexo SET('H', 'M') NOT NULL,
	pais VARCHAR(30),
	PRIMARY KEY(actor_id)
)ENGINE = InnoDB;
-- -----------------------------------------------------
-- Directores
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS directores(
  id_director INT NOT NULL AUTO INCREMENT,
  nombre VARCHAR(45) NOT NULL,
  apellido_paterno VARCHAR(30) NOT NULL,
	apellido_materno VARCHAR(30),
  fecha_nacimiento DATE,
  sexo SET('H', 'M') NOT NULL,
	pais VARCHAR(30),
  PRIMARY KEY (id_director)
  )ENGINE = InnoDB;
-- -----------------------------------------------------
-- Generos
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS generos (
  id_genero INT NOT NULL AUTO INCREMENT,
  descripcion VARCHAR(45) NOT NULL,
  PRIMARY KEY (gender_id)
  )ENGINE = InnoDB;
-- -----------------------------------------------------
-- Peliculas
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS peliculas (
  id_pelicula INT NOT NULL AUTO INCREMENT,
  id_genero	INT NOT NULL,
  id_director INT NOT NULL,
  titulo VARCHAR(45) NULL,
  sinopsis VARCHAR(45) NULL,
  premiere DATETIME NULL,
  duracion VARCHAR(45) NULL,
  CONSTRAINT fk_id_genero_peliculas FOREIGN KEY(id_genero)
    REFERENCES generos(id_genero),
    ON UPDATE CASCADE
  CONSTRAINT fk_id_director_peliculas FOREIGN KEY(id_director)
    REFERENCES directores(id_director),
    ON UPDATE CASCADE
  PRIMARY KEY (id_pelicula)
 )ENGINE = InnoDB;


  CREATE TABLE IF NOT EXISTS actores_peliculas(   
  id_pelicula INT NOT NULL,      
  id_actor INT NOT NULL,   
  personaje VARCHAR(20) NOT NULL,
  rol VARCHAR(20) NOT NULL,
  CONSTRAINT fk_id_pelicula_actores_peliculas FOREIGN KEY(id_pelicula)
    REFERENCES peliculas(id_pelicula),
    ON DELETE CASCADE
    ON UPDATE CASCADE
  CONSTRAINT fk_id_actor_actores_peliculas FOREIGN KEY(id_actor)
    REFERENCES actores(id_actor),  
    ON DELETE CASCADE
    ON UPDATE CASCADE
  PRIMARY KEY (id_pelicula, id_actor),   
  )ENGINE = InnoDB;
