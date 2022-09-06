class Formules():

    def __init__(self):
        self.sexo= False


    def genero( peso_kg, sexo):
        altura_cm = float(input("Digite su altura en centimetros: "))
        age = int(input("Digite su edad:  "))
        if sexo:
            calories_tbm = 66 + (13.7 * float(peso_kg)) + (5 * float(altura_cm)) - (6.75 * age)
        elif sexo == False:
            calories_tbm = 655 + (9.6 * float(peso_kg)) + (1.8 * float(altura_cm)) - (4.7 * age)
        else:
            print("Ha ocurrido un error: seleccionaste dos veces un valor fuera de tus opciones ")
        return calories_tbm.__round__()


    def pregunta(self):
        # self.kg = False

        while  True:
            try:
                sexo = input("Cual es tu genero?  Enter 'm' or 'f'  y confirme su respuesta:  ")
            except ValueError:
                print("valores de cadenas o strings ")
            else:
                if  sexo == 'm':

                    hombre = True



                elif  sexo == 'f':


                    hombre = False


                else:
                    hombre = None
                    print("Intente con m or f. ")
            break

        return hombre

