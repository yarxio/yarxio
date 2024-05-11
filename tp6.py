import datetime
import random


#1. Escriba una función redondear() que permita redondear un número
#decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
#entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
#anterior (3). 

'''def redondear():
    numero=float(input('escribe un numero decimal: '))
    print(round(numero))

redondear()'''

#2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un
#módulo que esté fuera de ese paquete, cree una función de suma de
#decimales que redondee el resultado haciendo uso de la función
#redondear() del paquete recién creado.

'''no entiendo esta actividad'''


#3) Usando el módulo datetime, escribe un programa que muestre la fecha
#y hora actuales del sistema.


'''def fecha_hora():
    hora=datetime.datetime.now()
    print(hora)

fecha_hora()

def fecha_hora2():
    x=datetime.datetime.now()
    x2=x.hour
    x3=x.day
    print(x2,x3)

fecha_hora2()'''

#4. Escriba un programa que devuelva un número par al azar entre 2 y 10
#(pista: para comprobar si se pueden generar todos los números, pruebe
#ejecutar el programa dentro de un ciclo infinito).

'''def numeros_random():
    while True:
        numero=random.randint(2,10)
        if numero%2==0:
            print(numero)

numeros_random()'''

# Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
# para la adivinación o para buscar consejo. Su mecanismo es muy simple:
# ante una pregunta del usuario, la bola responde con una de 8 posibles
# respuestas:
# - Es seguro que sí
# - Las chances son buenas
# - Puedes contar con ello
# - Pregúntame de nuevo más tarde
# - Concéntrate y pregunta de nuevo
# - No veo con claridad, intenta de nuevo
# - Mi respuesta es no
# - Mis fuentes me dicen que no
# Escriba una función en Python para simular la bola mágica.

'''def pregunta():
    
   while True:
    pregunta=str(input('cual es tu pregunta: '))
    
    respuestas=('no estoy seguro','es probable que si','es probable que no','puede ser','tal vez','porsupuesto que si','solo tu puedes averiguarlo','claro que no')

    resultado=random.randint(0,7)

    if pregunta=='salir':
      break

    print('la respuesta a',pregunta,'es:',respuestas[resultado])
    #6. Encuentre el tiempo de ejecución de los programas de los ejercicios
    # anteriores (pista: use el módulo time)

    print(datetime.datetime.resolution)

pregunta()'''


# 7. (Opcional) Sorteo: Escriba un programa que simule un sorteo donde
# toman uno o más papeles al azar de un pozo para elegir los ganadores.

'''def sorteo():
    contador=0
    ganadores=['jose','luna','leo','yusei','atlas','yugi','joey','tea','duck','tristan','noa','kaiba','mokuba','chaz','alexis','bastion','crow','yuya']
    while contador<=5:
        numero=random.randint(0,13)
        print('el ganador es',ganadores[numero])
        contador=contador+1
        ganadores.remove(ganadores[numero])
sorteo()
'''

# 8. (Opcional) Escriba una función que pida al usuario ingresar su fecha de
# nacimiento y sea capaz de devolver la cantidad de días desde su
# nacimiento hasta hoy.

def nacimiento():
    nacer=input('año de nacimiento: ')
    