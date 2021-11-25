Algoritmo Numeros_fibonacci23

	
	Escribir "Inserte en numero fibonacci a resolver "
	Leer N1
	
	a=0
	b=1
	c=1
	
	si N1 <= 0 Entonces
		Escribir "El resultado es 0"
	SiNo
		Para f<-1 Hasta  N1 Hacer
			c <- a + b
			a <- b
			b <- c
		FinPara
		Escribir "El resultado es", a 
	FinSi

FinAlgoritmo
