from model.model import Model
from view.view import View

m = Model()
print("connecting...")
v = View()
m.create_actor("Johnny","Deep"," ", '83/04/05', 'M', 'Estados Unidos')
m.create_director("José", "González", "Iñarritu", "75/02/03", 'M', 'México')
m.create_genero("Acción")
d = m.read_all_directores()
a = m.read_all_actores()
v.mostrar_todos_directores(d)
v.mostrar_todos_actores(a)
m.create_pelicula(1,1,"Atlantis","Una aventura abajo del mar", 90, '2003/02/02', 'A', 'E.U.A')
p = m.read_all_peliculas()
v.mostrar_todas_peliculas(p)
m.close_db()