import math
def main():
    #escribe tu código abajo de esta línea

    Altura = int(input('Altura de la casa: '))
    angulo = int(input('Angulo en grados: '))
    radianes = angulo*3.14/180
    Largo = round(Altura/math.sin(radianes))
    print("Largo de la escalera: "+str(Largo))
if __name__ == '__main__':
    main()
