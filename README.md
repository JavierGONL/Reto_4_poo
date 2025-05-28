## Reto 4: 
1. Include the class exercise in the repo.
```python
from math import acos, degrees

# Clase que representa un punto en un plano cartesiano
class Point:
    def __init__(self, x, y):
        self.x = x  # Coordenada x
        self.y = y  # Coordenada y

    # Método para crear un nuevo punto a partir de coordenadas dadas
    def another_point(self, new_x, new_y):
        return Point(new_x, new_y)


# Clase que representa una línea en un plano cartesiano
class Line:
    def __init__(self, inicio: "Point" = Point(0, 0), final: "Point" = Point(0, 0)):
        self.inicio = inicio  
        self.final = final  
        self.length = "you have to compute this first"  
        self.slope = "you have to compute this first"  
        self.range = "you have to compute this first" 

    # Método para calcular la longitud de la línea
    def compute_length(self):
        self.length : float = ((self.final.x - self.inicio.x)**2 
                        + (self.final.y - self.inicio.y)**2)**(1/2)
        return self.length

    # Método para calcular la pendiente de la línea
    def compute_slope(self):
        self.slope = ((self.final.y - self.inicio.y)
                    /(self.final.x - self.inicio.x)
                    )
        return self.slope

    # Método para calcular el rango de puntos de la línea
    def range_of_the_line(self):
        self.range = []
        if type(self.slope) != str: #Verifica que la pendiente haya sido calculada
            for i in range(self.inicio.x, self.final.x):
                self.range.append(Point(i, (self.slope) * i)) 
            return self.range
        else:
            return print("you have to compute slope first")

    # Método para verificar si la línea cruza el eje x
    def horizontal_cross(self):
        for i in range(len(self.range), len(self.range) - 1):
            if self.range[i].x < 0 and self.range[i + 1].x > 0:
                return print(f"Cross the x-axis between {self.range[i]} and {self.range[i+1]}")
        return print(f"don't Cross the x-axis")

    # Método para verificar si la línea cruza el eje y
    def vertical_cross(self):
        for i in range(len(self.range), len(self.range) - 1):
            if self.range[i].y < 0 and self.range[i + 1].y > 0:
                return print(f"Cross the y-axis between {self.range[i]} and {self.range[i+1]}")
        return print(f"don't Cross the y-axis")
    
class Shape():
    def __init__(self, edges: list = []):
        self.edges = edges
        self.inner_angles = []

    def compute_area():
        pass

    def compute_perimeter():
        pass

    def compute_inner_angles():
        pass

class Rectangle(Shape):
    def __init__(self, edges = []):
        self.edges = edges
        for i in range(len(edges)-1):
            self.edges[i].compute_length()
            if (edges[i+1].inicio.x > edges[i].inicio.x 
                 and edges[i+1].inicio.y > edges[i].inicio.y
                ):
                point_bottom_left = i
            if edges[i].inicio.y == edges[i].final.y:
                self.width : float = edges[i].length
            if edges[i].inicio.x == edges[i].final.x:
                self.height : float = edges[i].length
        self.point_bottom_left : "Point" = point_bottom_left
        self.inner_angles = []

        # puntos de las esquinas
        self.point_bottom_right: "Point"
        self.point_upper_left: "Point"
        self.point_upper_right: "Point"

    # Método para inicializar las esquinas del rectángulo
    def init_bottom_left(self):
        self.point_bottom_right = self.point_bottom_left.another_point(
            self.point_bottom_left.x + self.width, self.point_bottom_left.y
        )
        self.point_upper_left = self.point_bottom_left.another_point(
            self.point_bottom_left.x, self.point_bottom_left.y + self.height
        )
        self.point_upper_right = self.point_bottom_left.another_point(
            self.point_bottom_left.x + self.width, self.point_bottom_left.y + self.height
        )
        return [self.point_bottom_left, 
                self.point_bottom_right, 
                self.point_upper_left, 
                self.point_upper_right
                ]

    # Método para calcular el centro del rectángulo
    def compute_center(self):
        return Point(
            self.point_bottom_left.x + self.width / 2,
            self.point_bottom_left.y + self.height / 2,
        )

    # Método para calcular el área del rectángulo
    def compute_area(self):
        return self.width * self.height

    # Método para calcular el perímetro del rectángulo
    def compute_perimeter(self):
        return 2 * self.width + 2 * self.height

    def compute_inner_angles(self):
        self.inner_angles = [90, 90, 90, 90]

    # Método para verificar si dos rectángulos interfieren
    def compute_interference_between_2_rectangles(self, square_2: "Rectangle"):
        centro_1 = self.center
        centro_2 = square_2.center
        distancia = ((centro_2.x - centro_1.x)**2 
                    +(centro_2.y - centro_1.y)**2)**0.5
        cateto_opuesto = centro_2.y - centro_1.y
        coseno = cateto_opuesto / distancia
        hipotenusa_square_1 = abs(coseno * (self.width / 2))
        hipotenusa_square_2 = abs((coseno * (square_2.width / 2)))
        if distancia <= hipotenusa_square_1 + hipotenusa_square_2:
            print(f"interfieren")
        else:
            print(f"no interfieren")

    # Método para verificar si un rectángulo interfiere con un punto
    def compute_interferece_between_rectangle_and_point(self, point: "Point"):
        centro_1 = self.center
        centro_2 = point
        distancia = ((centro_2.x - centro_1.x)**2
                    +(centro_2.y - centro_1.y)**2)**0.5
        cateto_opuesto = centro_2.y - centro_1.y
        coseno = cateto_opuesto / distancia
        hipotenusa_square_1 = abs(coseno * (self.width / 2))
        if distancia <= hipotenusa_square_1:
            print(f"interfieren")
        else:
            print(f"no interfieren")

    def compute_interference_between_rectangle_and_line(self, line: "Line"):
        centro_1 = self.center
        line = line.range_of_the_line()
        interfieren: bool = False
        for i in range(len(line)):
            distancia = (((line[i].x - centro_1.x))**2 
                        +(line[i].y - centro_1.y)**2)**0.5
            cateto_opuesto = line[i].y - centro_1.y
            coseno = cateto_opuesto / distancia
            if coseno == 0:
                hipotenusa_square_1 = self.width / 2
            else:
                hipotenusa_square_1 = abs(cateto_opuesto / coseno)
            if distancia <= hipotenusa_square_1:
                interfieren = True
                break
        return interfieren

class Triangle(Shape): 
    # definido por los lados, entonces la formula de heron siempre es confiable
    def __init__(self, edges : list = []):
        super().__init__()
        self.edges = edges
        self.perimeter = 0
        self.area = 0
        self.angulos = []
    
    def compute_perimeter(self):
        if self.perimeter == 0:
            for i in range(len(self.edges)):
                self.edges[i].compute_length()
                self.perimeter += self.edges[i].length
            self.perimeter

    def compute_area(self):
        if self.perimeter == 0:
            self.compute_perimeter()
        semiperimetro = self.perimeter/2
        self.area = round((semiperimetro*(semiperimetro-self.edges[0].length)
                    *(semiperimetro-self.edges[1].length)
                    *(semiperimetro-self.edges[2].length))**(1/2),1)

    def compute_inner_angles(self):
        # Calcula los ángulos internos de un triángulo usando la ley de cosenos.
        # Primero, aseguramos que cada lado tenga su longitud calculada.
        angulos = []
        for i in range(len(self.edges)):
            self.edges[i].compute_length() 
        # Para cada vértice, calculamos el ángulo opuesto usando la fórmula del coseno.
        for i in range(len(self.edges)):
            a = self.edges[i].length  # Lado opuesto al ángulo que queremos calcular
            b = self.edges[i-1].length  # Lado adyacente 1
            c = self.edges[i-2].length  # Lado adyacente 2
            # Calculamos el coseno del ángulo usando la ley de cosenos
            cos_i = ((a**2 - b**2 - c**2) / (-2 * b * c))
            # Convertimos el coseno a grados y redondeamos
            angulo = round(degrees(acos(cos_i)))
            angulos.append(angulo)
        self.angulos = angulos


class Isosceles(Triangle):

    definition : str = "Triangulo con 2 lados y angulos iguales"
    def __init__(self, edges = []):
        super().__init__(edges)
    
class Equilateral(Triangle):
    definition : str = "Triangulo con 3 lados y angulos iguales"
    def __init__(self, edges = []):
        super().__init__(edges)

class Scalene(Triangle):
    definition : str = "Triangulo con lados y angulos diferentes"
    def __init__(self, edges = []):
        super().__init__(edges)

class TriRectangle(Triangle):
    definition : str = "Triangulo con un angulo recto"
    def __init__(self, edges = []):
        super().__init__(edges)


if __name__ == "__main__":
    # para un trirectangle
    p_1 = Point(0,0)
    p_2 = Point(1,0)
    p_3 = Point(0,1)
    l_1 = Line(p_1,p_2)
    l_2 = Line(p_2,p_3)
    l_3 = Line(p_3,p_1)
    triangulo_rectangulo = TriRectangle(edges = [l_1, l_2, l_3])
    triangulo_rectangulo.compute_inner_angles()
    triangulo_rectangulo.compute_area()
    triangulo_rectangulo.compute_perimeter()
    print(f" angulos :{triangulo_rectangulo.angulos} \n" 
          + f"area: {triangulo_rectangulo.area} \n"
          + f"perimetro: {triangulo_rectangulo.perimeter}"
          )
```
2. **The restaurant revisted**
 - Add setters and getters to all subclasses for menu item
 - Override calculate_total_price() according to the order composition (e.g if the order includes a main course apply some disccount on beverages)
 - Add the class Payment() following the class example.

   ```python
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
   ```
