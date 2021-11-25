Algoritmo Numeros_fibonacci23

	
	Escribir "Dame un numero"
	Leer N1
	
	a=0
	b=1
	c=1
	
	Para f <- 1 hasta N1 hacer 
		
		c=a+b
		a<-b
		b<-c
		

	FinPara
	
	r= a+b-N1
	
	Escribir "La suma es:", r

FinAlgoritmo
