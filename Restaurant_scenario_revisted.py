# Definimos la clase MenuItem como la clase base para los elementos del menu
class MenuItem:
    def __init__(self, name, price):
        self.name = name  # Nombre del elemento (ej: "frijolada")
        self.price = price  # Precio del elemento (ej: 10000)
    
    # Calcula el precio total segun la cantidad
    def total_price(self, number_of_items):
        return self.price * number_of_items

# Clase para los platos principales
class MainCourse(MenuItem):
    definition = "el plato principal"
    def __init__(self, name = None, price = None, course_list = []):
        super().__init__(name, price)
        self._maincourse_list = course_list  # Lista de platos principales disponibles

    def set_maincourse(self, new_course):
        self._maincourse_list.append(new_course)  # Agrega un nuevo plato principal
        
    def get_maincourse_list(self):
        # Muestra todos los platos principales disponibles
        for i in self._maincourse_list:
            print(f"{self._maincourse_list.index(i)+1}.{i.name} ${i.price}")

# Clase para las bebidas
class Drinks(MenuItem):
    definition = "las bebidas"
    def __init__(self, name = None, price = None, drink_list = []):
        super().__init__(name, price)
        self._drink_list = drink_list  # Lista de bebidas disponibles

    def set_drinks(self, new_drink):
        self._drink_list.append(new_drink)  # Agrega una nueva bebida
        
    def get_drinks_list(self):
        # Muestra todas las bebidas disponibles
        for i in self._drink_list:
            print(f"{self._drink_list.index(i)+1}.{i.name} ${i.price}")

# Clase para los postres
class Dessert(MenuItem):
    definition = "el postre"
    def __init__(self, name = None, price = None, dessert_list = []):
        super().__init__(name, price)
        self._dessert_list = dessert_list  # Lista de postres disponibles

    def set_dessert(self, new_dessert):
        self._dessert_list.append(new_dessert)  # Agrega un nuevo postre
        
    def get_dessert_list(self):
        # Muestra todos los postres disponibles
        for i in self._dessert_list:
            print(f"{self._dessert_list.index(i)+1}.{i.name} ${i.price}")

# Clase abstracta para medios de pago
class MedioPago:
  def __init__(self):
    pass

  def pagar(self, monto):
    raise NotImplementedError("Subclases deben implementar pagar()")

# Clase para pago con tarjeta
class Tarjeta(MedioPago):
    def __init__(self, numero, cvv, password, por_contacto = False):
        super().__init__()
        self.numero = numero  # Numero de la tarjeta
        self.__cvv = str(cvv)  # CVV privado
        self.por_contacto = por_contacto  # Si es pago por contacto
        self.__password : str = password  # Contrasena privada

    def pagar(self, monto):
        if self.por_contacto:
            print(f"Pagando por contacto {monto} con tarjeta {self.numero}")
            print("transaccion completada")
        else:
            n_intentos = 3
            while True:
                if n_intentos > 0:
                    print(f"Descontando {monto} de la tarjeta: {self.numero}")
                    password = input("Ingrese su password: ")
                    cvv = input("Ingrese su cvv: ")
                    if password == self.__password and cvv == self.__cvv:
                        print("Transaccion completada")
                        break
                    else:
                        n_intentos -=  1
                        print(f"Password o CVV incorrectos, le queda {n_intentos} intentos")
                        if n_intentos == 0:
                            break
                
# Clase para pago en efectivo
class Efectivo(MedioPago):
    def __init__(self, monto_entregado):
        super().__init__()
        self.monto_entregado = monto_entregado  # Dinero entregado por el cliente

    def pagar(self, monto):
        if self.monto_entregado >= monto:
            print(f"Pago realizado en efectivo. Cambio: {self.monto_entregado - monto}")
        else:
            print(f"Fondos insuficientes. Faltan {monto - self.monto_entregado} para completar el pago.")

# Clase que representa la orden del cliente
class Order:
    def __init__(self, main_course_list, drinks_list, dessert_list):
        self.main_course : "MainCourse" =  main_course_list  # Objeto con la lista de platos principales
        self.drink : "Drinks" = drinks_list  # Objeto con la lista de bebidas
        self.dessert : "Dessert" =  dessert_list  # Objeto con la lista de postres
        self.order_total_price = 0  # Precio total acumulado
        self.seleccion = []  # Elementos seleccionados por el usuario

    # Permite al usuario elegir un plato principal
    def _choose_main_course(self):
        lista = self.main_course._maincourse_list
        while True:
            self.main_course.get_maincourse_list()
            seleccion_1 = int(input("Que desea? "+ " \n(0 para volver): \n-->"))
            if seleccion_1 == 0:
                break
            try:
                if 1 <= seleccion_1 <= len(lista):
                    self.seleccion.append(lista[seleccion_1 - 1])
                else:
                    print("Ingrese un numero valido de la lista.")
            except ValueError:
                print("Por favor ingrese un numero.")

    # Permite al usuario elegir una bebida
    def _choose_drink(self):
        lista = self.drink._drink_list
        while True:
            self.drink.get_drinks_list()
            seleccion_1 = int(input("Que desea? "+ " \n(0 para volver): \n-->"))
            if seleccion_1 == 0:
                break
            try:
                if 1 <= seleccion_1 <= len(lista):
                    self.seleccion.append(lista[seleccion_1 - 1])
                else:
                    print("Ingrese un numero valido de la lista.")
            except ValueError:
                print("Por favor ingrese un numero.")

    # Permite al usuario elegir un postre
    def _choose_dessert(self):
        lista = self.dessert._dessert_list
        while True:
            self.dessert.get_dessert_list()
            seleccion_1 = int(input("Que desea? "+ " \n(0 para volver): \n-->"))
            if seleccion_1 == 0:
                break
            try:
                if 1 <= seleccion_1 <= len(lista):
                    self.seleccion.append(lista[seleccion_1 - 1])
                else:
                    print("Ingrese un numero valido de la lista.")
            except ValueError:
                print("Por favor ingrese un numero.")

    # Menu principal para que el usuario agregue productos a la orden
    def chosse_order(self):
        while True:
            seleccion_2 = input(
                "Que le gustaria agregar a la orden? \n 1. Plato principal \n 2. Bebida \n 3. Postre"
                " (si desea terminar la orden escriba 0) \n-->"
            )
            if seleccion_2 == "1":
                self._choose_main_course()
            elif seleccion_2 == "2":
                self._choose_drink()
            elif seleccion_2 == "3":
                self._choose_dessert()
            elif seleccion_2 == "0":
                self._get_factura()
                print("\n\n___________pagando___________\n\n".center(30))
                mi_tarjeta.pagar(self.order_total_price)
                break
            else:
                print("Ingrese una opcion valida.")

    # Calcula y muestra la factura final, aplicando descuentos si corresponde
    def _get_factura(self):
        n_bebidas = 0
        n_maincourse = 0
        n_desserts = 0
        print("\n\n___________Factura___________\n\n".center(30))
        for i in self.seleccion:
            if type(i) == Drinks:
                n_bebidas +=1
            elif type(i) == MainCourse:
                n_maincourse += 1
            elif type(i) == Dessert:
                n_desserts += 1
            print(f"{self.seleccion.index(i)+1}: {i.name}")
            self.order_total_price += i.price
        # Aplica descuentos segun la cantidad de productos
        if n_bebidas >= 5 or  n_maincourse >= 5 or n_desserts >= 10:
            print("\n\n___________Descuentos___________\n\n".center(30))
            if n_bebidas >= 5:
                print("descuento cantidad de bebidas = -5%")
                self.order_total_price = (self.order_total_price 
                                        - (self.order_total_price * (5/100))
                                        )
            if n_maincourse >= 5:
                print("descuento cantidad de platos principales = -10%")
                self.order_total_price = (self.order_total_price 
                                        - (self.order_total_price * (10/100))
                                        )
            if n_desserts >= 10:
                print("descuento cantidad de postres = -5%")
                self.order_total_price = (self.order_total_price 
                                        - (self.order_total_price * (5/100))
                                        )
        print(f"\n\nCANTIDAD A PAGAR: {self.order_total_price}")


if __name__ == "__main__":

    main_course_list = [
        MainCourse("frijolada", 10000),
        MainCourse("costillas bbq", 15000),
        MainCourse("pollo asado", 12000),
        MainCourse("tacos", 8000)
    ]
    drinks_list = [
        Drinks("agua", 2000),
        Drinks("limonada", 3000),
        Drinks("cafe", 2500),
        Drinks("cerveza", 5000)
    ]

    dessert_list = [
        Dessert("cupcake", 4000),
        Dessert("helado", 3500),
        Dessert("fruta", 3000),
        Dessert("chocolate", 4500)
    ]

    postres = Dessert(dessert_list = dessert_list)
    bebidas = Drinks(drink_list = drinks_list)
    plato_principal = MainCourse(course_list = main_course_list)
    mi_tarjeta = Tarjeta( 1234356789, 123, "qweasdzxc")
    order = Order(plato_principal, bebidas, postres)
    order.chosse_order()