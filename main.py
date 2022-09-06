from Fitness.Formulas.conversor import Conversor
from Fitness.Formulas.formules import Formules
from Fitness.Formulas.tables import women_age_range

obje = Conversor()
(obje.pregunta())
obje.convertir_peso(obje.pregunta())

my = Formules()
print(my.pregunta())
print(my.genero(obje.convertir_peso(obje.pregunta())))

women_age_range()
