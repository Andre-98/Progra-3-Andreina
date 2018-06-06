date = input ("Ingrese una fecha: ")
if date%100 == 0:
    print "La fecha que usted ingreso pertenece al siglo " + str (date/100)
else:
    print "La fecha que usted ingreso pertenece al siglo " + str ((date/100)+1)
