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
    
    def compute_perimeter(self):
        #print(self.edges)
        for i in range(len(self.edges)):
            self.edges[i].compute_length()
            self.perimeter += self.edges[i].length
        return self.perimeter

    def compute_area(self):
        self.compute_perimeter()
        semiperimetro = self.perimeter/2
        self.area = (semiperimetro*(semiperimetro-self.edges[0].length)
                    *(semiperimetro-self.edges[1].length)
                    *(semiperimetro-self.edges[2].length))**(1/2)
        return self.area

    def compute_inner_angles(self):
        # a**2 = b**2 + c**2 - 2bc cos a -> cos a = (a**2 - b**2 - c**2)/(-2bc)
        angulos = []
        for i in range(len(self.edges)):
            self.edges[i].compute_length() 
        for i in range(len(self.edges)):
            a = self.edges[i].length
            b = self.edges[i-1].length
            c = self.edges[i-2].length
            cos_i = ((a**2 - b**2 - c**2) / (-2 * b * c))
            angulo = round(degrees(acos(cos_i)))
            angulos.append(angulo)
        return angulos

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
```
2. **The restaurant revisted**
 - Add setters and getters to all subclasses for menu item
 - Override calculate_total_price() according to the order composition (e.g if the order includes a main course apply some disccount on beverages)
 - Add the class Payment() following the class example.
