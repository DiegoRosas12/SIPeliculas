class View:
    def start(self):
        print("--------------------------------")
        print("Bienvenido al sistema de peliculas")
        print("--------------------------------")
        
    def end(self):
        print("\n-----------------")
        print("¡Vuelve pronto!")
        print("-----------------")

    def menu(self):
        print("---------------------")
        print("    Menú Principal:  ")
        print("---------------------") 
        
        print("1. Actores")
        print("2. Directores") 
        print("3. Generos")
        print("4. Peliculas")
        print("\n0. Salir") 
 
    def select_opcion(self):
        print("Seleccione una opción: ", end = '') 

    def opcion_invalid(self):
        print("¡Opción invalida vuelva a intentar!") 

    def ask(self, output):
        print(output, end = '')    
        
    def success(self):    
        print("Los cambios se efectuaron correctamente ")

    def error(self):
        print("Error: no se realizo correctamente")
    
    def id_invalido(self):
        print("Error. el id es invalido") 

    def mostrar_update(self):
        print("Actualiza los campos que sean necesarios")

    """
    Metodos actor
    """
    def menu_actor(self):
        print("---------------------")
        print("    Menú Actores:  ")
        print("---------------------") 
        
        print("1. Agregar actor")
        print("2. Leer actor") 
        print("3. Leer todos los actores")
        print("4. Buscar actor por nombre")
        print("5. Actualizar actor")
        print("6. Borrar actor")  
        print("\n0. Salir")

    def actor_menu(self, actor):
        print('ID: ', actor[0])
        print('Nombre: ', actor[1])
        print('Apellido Paterno: ', actor[2])
        print('Apellido Materno: ', actor[3])
        print('Fecha de nacimiento: ', actor[4])
        print('Sexo: ', actor[5])
        print('País: ', actor[5])

    def mostrar_un_actor(self, actor):
        print(f'{record[0]:<5}|{record[1]:<20}|{record[2]:<15}|{record[3]:<15}|{record[4]:<8}|{record[5]:<1}|{record[6]:<15}')


    def mostrar_actores(self, actors):
        print('\n' + 'ID'.ljust(5) + '|' + 'Nombre(s)'.ljust(20) + '|' + 'Apellido Paterno'.ljust(15)+ '|'+'Apellido Materno'.ljust(15)+'|'+'Fecha nacimiento'.ljust(8)+'|' +' Sexo'.ljust(1)+'|' +' País'.ljust(15))   

        for record in actores:
            print(f'{record[0]:<5}|{record[1]:<20}|{record[2]:<15}|{record[3]:<15}|{record[4]:<8}|{record[5]:<1}|{record[6]:<15}')
        print('-'*79)

    def mostrar_actor_footer(self):
        print('*'*79)


    """
    Metodos directores
    """
    
    def director_menu(self):
        print("\n---------------------")
        print("    Menú Directores:  ")
        print("---------------------") 
        
        print("1. Agregar director")
        print("2. Leer director") 
        print("3. Leer todos los directors")
        print("4. Leer rangos de precio de los directors")
        print("5. Actualizar director")
        print("6. Borrar director")
        print("0. Salir") 

    def mostrar_directors(self, directors):
        print('\n' + 'barcode'.ljust(5) + '|' + 'Nombre(s)'.ljust(20) + '|' + 'Marca'.ljust(20)+ '|'+'Detalles'.ljust(35)+'|'+' Precio'.ljust(20))   

        for record in directors:
            print(f'{record[0]:<6}|{record[1]:<35}|{record[2]:<35}|{record[3]:<35}|{record[4]:<35}')

    """
    Metodos producto
    """
    
    def mostrar_pedido(self, var):
        print("\n---------------------")
        print("     Pedido:  ")
        print("---------------------")   
        print("ID: ", var[0])
        print("Estado orden:", self.obtener_pedido(var[1])) 
        print("Fecha: ",var[2])
        print("ID Cliente:", var[3])
        print("Nombre del actor:", var[4])
        print("Dirección de envio:", var[5])
        print("Correo:", var[6])
        print("Teléfono:",var[7])

    def obtener_pedido(self, status):
        string = ''

        if status == 0:
            string = "Pendiente"
        elif status == 1:
            string = "Enviado"
        elif status == 2:
            string = "Retrasado"  
        elif status == 3:
            string = "Entregado" 
        else:
            string ="Desconocido"

        return string               
           

    def pedidos_menu(self):
        print("\n---------------------")
        print("    Menú Pedidos:  ")
        print("---------------------") 
        
        print("1. Empezar Compra")
        print("2. Leer Pedido")
        print("3. Leer todos los pedidos")
        print("4. Leer pedidos entre fechas")
        print("5. Actualizar pedido")
        print("6. Agregar el producto del pedido")
        print("7. Modificar productos del pedido")
        print("8. Borrar productos del pedido")
        print("9. Borrar pedido")
        print("0. Salir")      

    def mostrar_pedidosProductos(self, productos):
        print('\n' + 'ID venta'.ljust(5) + '|' + 'Nombre'.ljust(20) + '|' + 'Marca'.ljust(20)+ '|'+'Precio'.ljust(35)+'|'+' Cantidad'.ljust(20)+ '|'+' Total'.ljust(20))   

        for record in productos:
            print(f'{record[0]:<11}|{record[1]:<25}|{record[2]:<10}|{record[3]:<15}|{record[4]:<15}|{record[5]:<15}')

    def mostrar_pedidos(self, pedidos):
        print('\n' + 'ID pedido'.ljust(5) + '|' + 'Status'.ljust(20) + '|' + 'Fecha y Hora'.ljust(20)+ '|'+'ID Cliente'.ljust(35)+'|'+'ID Dirección'.ljust(20))  
        print('='*120) 

        for record in pedidos:
            print(f'{record[0]:<6}|{self.obtener_pedido(record[1]):<25}|{str(record[2]):<25}|{record[3]:<25}|{record[4]:<25}')