	Inicio = input ("Muy buen dia;")
	Calcular = print ("Calcular Area de:;")
    Cuadrado = print ("1 = Cuadrado;") 
	Circulo = print ("2 = Circulo;")
	Rectangulo = print ("3 = Rectangulo;") 
	Rectangulo = print ("4 = Triangulo;")
	F = print (input ("¿Cual figura quieres calcular?;"))
	
	Segun F Hacer
		1:
			Figura1 = print ("Area del cuadrado;")
			cu = print(input ("Ingresa el lado;"))
			res1 <- cu * cu
			print ("El area es: ", res1;)
		2:
			Figura2 = print ("Area del circulo;")
			r = print(input ("Ingresa el radio;"))
			res2 <- PI * r^2
			print ("El area es: ", res2;)
		3:
			Figura3 = print ("Area del rectangulo;")
			b1 = print(input ("Ingresa la base;"))
			h1 = print(input ("Ingresa la altura;"))
			res3 <- b1 * h1
			print ("El area es: ", res3;)		
		4:
			Figura4 = print ("Area del triangulo;")
			b = print(input ("Ingresa la base;"))
			h = print(input ("Ingresa la altura;")
			res4 <- (b * h) / 2
			print ("El area es: ", res4;)
		De Otro Modo:
			print ("Tu dato es erroneo, intentalo nuevamente;")
	Fin Segun
	
	
	    print ("Que tengas un exelente dia <3;")