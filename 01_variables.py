# Variables: Siempre en minusculas y en caso de nombres compuestos separo con _

my_string_variable = "My String variable" # Guion bajo si, guion medio NO!
print(my_string_variable)

my_bool_variable = False
print(my_bool_variable)

my_int_variable = 5
print(my_int_variable)

# Con funcion STR() convierto el valor int a string (lo mismo con INT() SORTED() FLOAT() ENTRE OTRAS)
my_int_to_str_variable = str(my_int_variable)
print (my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Concatenar
print(my_string_variable, my_int_variable, my_bool_variable) 
print("Este es el valor de: ", my_bool_variable) # Concateno con texte pre-establecido
# Funciones del sistema

# LEN () : Cuenta el largo de caracteres
print(len(my_int_to_str_variable)) 
print(len(my_string_variable)) 

# Variables en una sola linea
name, surname, alias, age = "Gonzalo", "Avedano", "Zerone", 32
print("Me llamo:", name, surname, "Mi edad es: ",age, "Y mi alias es: ", alias)

# Solicitar al usuario el ingreso de datos y almacenarlos en variables (NO ES LO USUAL)
first_name = input('Cual es tu nombre: ')
age = input('Cuantos años tienes? ')

print(first_name)
print(age)

# Forzamos el tipo, QUE NO TIENE SENTIDO PORQUE MODIFICAMOS EL VALOR
address: str = " Mi direccion"
address: 32
print(type(address))