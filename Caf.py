nm=str(input("Ingresa tu nomubre "))
mate=str(input("Ingresa la materia "))
calf=float(input( "Escriba su calificacion "))
print("estimad@ ", nm) 
if calf>=95:
    print(" Su calificacion es EXELENTE")
elif calf>=85 and calf<95:
    print(" Su calificacion es NOTABLE")
elif calf>=75 and calf<85:
    print(" Su calificacion es BUENA")
elif calf>=70 and calf<75:
    print(" Su calificacion es SUFICIENTE")
else:
    print (" Su calificacion es N A")
print(" de la materia ", mate)