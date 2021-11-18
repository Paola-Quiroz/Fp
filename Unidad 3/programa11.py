#Pedir calificaciones y que muestre si aprobo
N  =  5
Nombre  =  input ( "Ingresar nombre:" );
print ( "Ingresar calificaciones:" );
Ca  =  int ( input ( "Matematicas:" ));
Cb  =  int ( input ( "Programacion:" ));
Cc  =  int ( input ( "Inglés:" ));
Cd  =  int ( entrada ( "TICS:" ));
Ce  =  int ( input ( "Calculo:" ));

Cal  = ( Ca + Cb + Cc + Cd + Ce );
Prom  = ( Cal / N );

si  Prom  >  7 :
	print ( Nombre , Prom , "Aprobo" ):
elif  Prom  <  7 :
	print ( Nombre , Prom , "Reprobo" );