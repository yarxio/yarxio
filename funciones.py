#definir una funcion propia

'''def saludar(): #crear la funcion
    print('hola')
    pass #para continuar

saludar() # utiliza la funcion ya echa

def funcion():
    nombre='amir' #solo existe dentro de la funcion
    print('hola')
saludar()
print (nombre) #busca bariable fuera de la funcion
'''
# no utilizar variantes globales en entornos de funciones y viseversa

# def sumar2num(numero1,numero2):
#     print(numero1+numero2)

# sumar2num(1,2) #escribir parametros   #el orden si importa
# sumar2num(14,29)


#1. Escriba una función que muestre todos los números primos entre 1 y un número n que
#es ingresado por parámetro.


#es_primo(numero):
#   if numero<=1:
#       return False
    
#   for i in range(2,numero):
#       if numero%i==0:
#             return False
    
#     return True


'''def primo_n(n):
     for i in range(n,n+1):
         if es_primo(i):
             print(i)

primo_n(100)'''


'''Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si
la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se
considerará válida si contiene el símbolo "@".'''

# def es_correo(correo):
#     if correo.find('@')!=-1:
#         return True
#     return False

#correo=str(input("ingrese un correo"))


# def Es_correo(Correo):
#     if '@' in correo:
#         print('es valida')


def primo(numero):
    if numero<=1: # el 1 en programacion no es primo
        return False
    
    for i in range(1,numero):
        if numero%i==0:
            return False
    
    return True  # esto es para verificar si es primo

def lista_primos(limiteI,limiteS):
    lista=[]
    for i in range(limiteI,limiteS+1):
        if primo(i):
            lista.append(i)
        
    return lista


print(lista_primos(1,10))