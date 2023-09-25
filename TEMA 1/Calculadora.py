class Calculadora:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
        
    # Métodos Setter para x e y
    def set_x(self, x):
        self._x = x
    
    def set_y(self, y):
        self._y = y
        
    # Métodos Getter para x e y
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
        
    # Métodos para las operaciones básicas
    def suma(self):
        return self._x + self._y
    
    def resta(self):
        return self._x - self._y
    
    def multiplicacion(self):
        return self._x * self._y
    
    def division(self):
        if self._y == 0:
            return "Error: División por cero"
        return self._x / self._y


if __name__ == "__main__":
    # Ejemplo de uso
    calc = Calculadora(10, 5)  # Se crea un objeto calculadora con x=10 y y=5
    
    print("x:", calc.get_x())  # Se imprime el valor de x
    print("y:", calc.get_y())  # Se imprime el valor de y

    print("x:", calc._x)  # Se imprime el valor de x
    print("y:", calc._y)  # Se imprime el valor de y
    
    print("Suma:", calc.suma())  # Se imprime el resultado de la suma
    print("Resta:", calc.resta())  # Se imprime el resultado de la resta
    print("Multiplicación:", calc.multiplicacion())  # Se imprime el resultado de la multiplicación
    print("División:", calc.division())  # Se imprime el resultado de la división
    
    # Cambiar valores de x e y usando los métodos Setter
    calc.set_x(20)  # Se cambia el valor de x a 20
    calc.set_y(0)  # Se cambia el valor de y a 0
    
    print("\nValores Actualizados")
    print("x:", calc.get_x())  # Se imprime el nuevo valor de x
    print("y:", calc.get_y())  # Se imprime el nuevo valor de y
    print("División con nuevos valores:", calc.division())  # Se intenta realizar una división por cero