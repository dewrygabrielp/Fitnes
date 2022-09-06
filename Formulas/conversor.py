class Conversor():

    def __init__(self):
        self.kg = False
        self.libra = 0
        self.kilogramo = 0

    def convertir_peso(self, kg):
        if kg:
            self.kilogramos = float(input("Digite el peso en Kilogramos: "))
            self.libras = self.kilogramos * 2.20462262
            print("Usted tiene: {} libras: ".format(self.libras))

        elif kg == False:
            self.libras = float(input("Digite el peso en Libras: "))
            kilogramos: float = self.libras / 2.2046
            print("Usted tiene: {} kilogramos: ".format(kilogramos))


        else:
            print("Ha ocurrido un error: seleccionaste dos veces un valor fuera de tus opciones ")

        return kilogramos

    def pregunta(self):
        # self.kg = False

        while  True:
            try:
                med = input("Que desea convertir? Enter 'kg' or 'lb'  y confirme su respuesta:  ")
            except ValueError:
                print("Intente con kg or lb. ")
            else:
                if med == 'kg':

                    kg = True
                    return kg


                elif med == 'lb':


                    kg = False
                    return  kg

                else:
                    kg = None
                    print("Intente con kg or lb. ")
            break

obje = Conversor()

(obje.pregunta())
obje.convertir_peso(obje.pregunta())
