from model.model import Model

m = Model()
m.create_actor('John', 'Whick', 'Torres', '01/01/79', 'M', 'E.U.A.')
m.read_actor(1)
m.read_actor_name('John')
m.close_db()