Algoritmo CalcularArea_Cuadrado_circulo_Rectangulo_Triangulo 
	Escribir "Muy buen dia"
	Escribir "Calcular Area de: "
	Escribir "1 = Cuadrado " 
	Escribir "2 = Circulo " 
	Escribir "3 = Rectangulo " 
	Escribir "4 = Triangulo " 
	Escribir "¿Cual figura quieres calcular?"
	Leer F
	
	Segun F Hacer
		1:
			Escribir "Area del cuadrado"
			Escribir "Ingresa el lado"
			Leer cu
			res1 <- cu * cu
			Escribir "El area es: ", res1
		2:
			Escribir "Area del circulo"
			Escribir "Ingresa el radio"
			Leer r
			res2 <- PI * r^2
			Escribir "El area es: ", res2
		3:
			Escribir "Area del rectangulo"
			Escribir "Ingresa la base"
			leer b1
			Escribir "Ingresa la altura"
			Leer h1
			res3 <- b1 * h1
			Escribir "El area es: ", res3			
		4:
			Escribir "Area del triangulo"
			Escribir "Ingresa la base"
			Leer b1
			Escribir "Ingresa la altura"
			Leer h
			res4 <- (b * h) / 2
			Escribir "El area es: ", res4
		De Otro Modo:
			Escribir "Tu dato es erroneo, intentalo nuevamente"
	Fin Segun
	
	
	Escribir "Que tengas un exelente dia <3"
	
FinAlgoritmo
