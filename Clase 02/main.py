nombre:str = "Daniel"
edad:int = (input("¿Cuál es tu edad? "))
anno_de_nacimiento:int = 2026 - 2
print(anno_de_nacimiento)
mayor_de_edad = edad >= 18
print(mayor_de_edad)

no_soy_yo = not(nombre == "Daniel" and edad == 22)
soy_yo = nombre == "Daniel" and edad == 22
quizas_soy_yo = nombre == "Daniel" or edad == 21

print(soy_yo)
print(no_soy_yo)
print(quizas_soy_yo)

x:int = 10
x += 5
print(x)