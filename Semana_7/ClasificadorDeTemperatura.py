Temperatura= float(input("Ingrese la temperatura en grados Celsius: "))
if Temperatura < 0:
  print("Bajo Cero, congelación")
elif Temperatura >= 0 and Temperatura < 15:
  print("Frio")
elif Temperatura >= 15 and Temperatura <=25:
  print("Templada, es una temperatura ideal :D")
elif Temperatura > 25 and Temperatura <= 35:
  print("Calida")
else:
  print("Extremo Calor")
