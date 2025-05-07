import random

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"  
longitud = int(input('Dime la longitud de tu contraseña: '))
contraseña = ""
for i in range(longitud):
    contraseña += random.choice(caracteres)
print(contraseña)

#