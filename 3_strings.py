### Strings###

# Declaración de strings usando comillas simples y dobles

variable1 = 'Pedro'
variable2 = "Riquelme"

print(variable1)
print(variable2)

# Concatenar strings con un espacio en blanco

print(variable1 + " " + variable2)

# Crear un salto de línea

variable3 = "Esto es un string\ncon salto de línea"
print(variable3)

# Insertar tabulación

variable4 = "\tEsto es un string con una tabulación"
print(variable4)

# Insertar tabulación

variable5 = "\tEsto es un string con salto de línea"
print(variable5)

# Formateo de strings

nombre, surname, age = "Pedro", "Riquelme", 50

# Formateo usando ,format()

print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age)) 

# Formateo usando 1

print("Mi nombre es %5 %5 y mi edad es %5" % (name,surname,age)) 

# Cocatear varios string

print ("Mi nombre es" + name + "" + surname + "y mi edad es" + str (age))

#Formulario usando f-strings (moderno)

print (f"Mi nombre es {name} {surname} y mi edad es {age}")