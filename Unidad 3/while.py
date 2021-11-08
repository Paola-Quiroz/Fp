a = True

while a:
    cal = int(input('Escribe una calificacion: '))

    if cal >= 7:
        print('Has Aprobado')
        # Esto causa que el ciclo termine
        a = False
    else:
     print('Has Reprobado :(')
     a= False