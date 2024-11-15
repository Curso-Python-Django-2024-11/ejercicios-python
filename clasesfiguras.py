class Figura:

    def area(self):
        pass

    def perimetro(self):
        pass


class Triangulo(Figura):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura / 2
    

class Rectangulo(Figura):

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)
    

class Cuadrado(Rectangulo):

    def __init__(self, lado):
        super().__init__(base=lado, altura=lado)