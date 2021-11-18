#Desarrollar un programa que guarde a todos los integrantes del grupo como objetos
#con los siguientes atributos: Edad, Calificacion de los diferentes materias, promedio, 
#calificacion de la prepa y lugares de residencia. 
#Imprimir o mostrar los siguientes reportes:
#5 alumnos con mayor edad (dias incluidos)
#Promedio de toda la preparatoria 
#Alumnos que viven mas cerca y mas lejos
#Materia con mejor rendimiento.

#crear clase
class Alumno():
     def __init__ (self,edad,nombre,caldif,fp,fi,it,te,ing,md,califpre,dondvive,distancia):
          self.nombre= nombre
          self.edad = edad
          self.caldif = caldif
          self.fp = fp
          self.fi = fi
          self.it = it
          self.te = te
          self.ing = ing
          self.md = md
          self.califpre = califpre
          self.dondvive = dondvive
          self.distancia=distancia

#crear objetos
Reyna Yamile = Alumno(18,"Reyna Yamile", 9, 8, 10, 10, 9, 6, 7, 9, "Emiliano Zapata", 13)
Sharlene Mirozlava = Alumno(18,"Sharlene Mirozalva",9, 8, 10, 7, 9, 6, 7, 8, "Cosio", 27)
Melani Marlen = Alumno (18,"Melani Marlen", 5, 5, 7, 5, 5, 5, 5, 9, "Pabellon de Arteaga", 5)
Diego = Alumno(19,"Diego", 8, 9, 9, 10, 8, 8, 10, 10, "Rincon de Romos", 13) 
Britzy Michel = Alumno(18,"Britzy Michel", 10, 9, 10, 10, 8, 8, 10, 10, "Rincon de Romos", 13) 
Fernando Ulises = Alumno(17, "Fernando Ulises", 8, 8, 7, 9, 10, 8, 10, 9, "Pabellon de Arteaga", 5)
Johana Alejandra = Alumno(18,"Johana Alejandra", 10, 10, 10, 10, 10, 10, 10, 8, "jesus maria", 27)
Alejandro= Alumno(19, "Alejandro", 10, 9, 8, 9, 8, 9, 8, 9, "Ejido Fresnillo", 17)
Donaldo Ramses= Alumno(18, "Donaldo Ramses", 8, 9, 10, 9, 8, 6, 8, 8, "Pabellon de Arteaga", 5)
Austin Kenneth= Alumno(19, "Austin Kenneth", 10, 9, 8, 9, 10, 9, 8, 8, "Pabellon de Arteaga", 5)
Paola Marlen=Alumno(18,"Paola Marlen", 10, 9, 8, 9, 10, 9, 8, 8, "Carboneras", 8)
Isaac Jared=Alumno(19, "Isaac Jared", 10, 9, 10, 9, 10, 10, 10, 9, "Rincon de Romos", 13)
Areli Jatziri=Alumno(19, "Areli Jatziri", 10, 9, 10, 9, 10, 9, 10, 8, "Rincon de Romos", 13)
Elias Alain=Alumno(18, "Elias Alain", 10, 9, 10, 9, 10, 9, 10, 8, "Rincon de Romos", 11)
Alexis David=Alumno(19, "Alexis David", 10, 9, 10, 8, 7, 8, 7, 8, "Rincon de Romos", 13)
#alumnos con mayor edad
print ("los alumnos con mayor edad son ", Diego.nombre,",",Alejandro.nombre,",",Isaac Jared.nombre,",",Areli Jatziri.nombre,",",Alexis David.nombre,"y", Austin Kenneth.nombre )
#alumnos con su promedio
print ("los alumnos y sus calificaciones se presentaran a continuación\n", Reyna Yamile.nombre,"con promedio de",Reyna Yamile.calprep,",\n",Sharlene Mirozlava.nombre,"con promedio de",Sharlene Mirozlava.calprep)
print(Melani Marlen.nombre,"con promedio de",Melani Marlen.calprep,",\n",Diego.nombre,"con promedio de",Diego.calprep,",\n",Britzy Michel.nombre,"con promedio de",Britzy Michel.calprep)
print(fernando.nombre,"con promedio de",fernando.calprep,",\n",alejandra.nombre,"con promedio de",alejandra.calprep,",\n",alejandro.nombre,"con promedio de",alejandro.calprep)
print(donaldo.nombre,"con promedio de",donaldo.calprep,",\n",austin.nombre,"con promedio de",austin.calprep,",\n",paola.nombre,"con promedio de",paola.calprep)
print(Isaac Jared.nombre,"con promedio de",Isaac Jared.calprep,",\n",Areli Jatziri.nombre,"con promedio de",Areli Jatziri.calprep,",\n",Elias Alain.nombre,"con promedio de",Elias Alain.calprep,",\n",Alexis David.nombre,"con promedio de",Alexis David.calprep)
#alumnos que viven mas cerca y mas lejos
print("Los alumnos que viven mas lejos del tec son:\n",Sharlene Mirozlava.nombre,"es de ",Sharlene Mirozlava.dondvive, "con una distancia de", Sharlene Mirozlava.distancia, "y\n", Johana Alejandra.nombre, "es de", Johana Alejandra.dondvive, "con una distancia de", Johana Alejandra.distancia )
print("Los alumnos que viven mas cerca del tec son:\n",Melani Marlen.nombre,"es de ",Melani Marlen.dondvive, "con una distancia de", Melani Marlen.distancia, "y\n", Donaldo Ramses.nombre, "es de", Donaldo Ramses.dondvive, "con una distancia de",Donaldo Ramses.distancia )
#alumnos y su mejor calificacion de materia
print ("los alumnos y sus mejoras se presentaran a continuación\n", Reyna Yamile.nombre,"con la meteria de fundamentos de la programacion",",\n",Sharlene Mirozlava.nombre,"con la meteria de fundamentos de la investigación")
print(Melani Marlen.nombre,"con la materia de fundamentos de la investigacion",",\n",Diego.nombre,"con la materia de fundamentos de mates discretas",",\n",Britzy Michel.nombre,"con la materia de calculo diferencial")
print(Fernando Ulises.nombre,"con la materia de matematicas discretas",",\n",Johana Alejandra.nombre,"con la materia de introduccion a las tics",",\n",Alejandro.nombre,"con la materia de calculo diferencial")
print(Donaldo Ramses.nombre,"con la materia de calculo diferencial",",\n",Austin Kenneth.nombre,"con la materia de ingles ",",\n",Paola Marlen.nombre,"con la materia de calculo diferencial ")
print(Isaac Jared.nombre,"con la materia de calculo diferencial",",\n",Areli Jatziri.nombre,"con la materia de fundamentos de la investigacion",",\n",Elias Alain.nombre,"con la materia de ingles",",\n",Alexis David.nombre,"con la materia de calculo diferencial ")