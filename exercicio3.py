import math
x1= float(input("O valor de x1 é:"))
x2= float(input("O valor de x2 é:"))
y1= float(input("O valor de y2 é:"))
y2= float(input("O valor de y2 é:"))
distancia= math.sqrt((x1-x2) ** 2 + (y2 - y1) ** 2)
print("A distância entre os pontos é:", distancia )