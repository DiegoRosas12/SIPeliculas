from model.model import Model
from view.view import View

m = Model()
print("connecting...")
v = View()
v.menu_genero()
# m.create_genero("Comedia")
g = m.read_genero_nombre("Terror")
v.mostrar_un_genero(g)
generos = m.read_all_generos()
print(generos)
# v.mostrar_todos_generos(generos)
m.close_db()