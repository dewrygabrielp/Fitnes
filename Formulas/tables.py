def women_age_range():
    try:
        age = int(input("Ingrese su edad: "))
    except ValueError:
        print("Esta opción solo acepta valores enteros")
    if age < 20:
        print("Estás en potestad de comer cuanto quieras sino tienes enfermedades como diabetes. ")
    elif age > 79:
        print("Debes comer según los cuicados e indicaciones de tu Doctor. ")
    elif  age in range(20, 39):
        print("Si su porcentaje se situa entre 21 y el 33% tendrá sobrepeso si su procentaje está\n"
              "entre 33 y 39% será obeso si el porcentaje supera el 39% de grasa corporal.")
    elif age in range(40, 59):
        print("Será baja en grasa con un porcentaje inferior al 23%;  saludable [ara in porcentaje de\n"
              "23-35%; sobrepeso con un 35-40% y la obesidad con cifras superiores al 40%.")
    elif age in range(60, 79):
        print("Está bajo en grasa para los índices inferiores al 24% saludable para 24-36%, sobrepeso\n"
              "para el 36-42% y obesidad para porcentajes superiores al 42%\n"
              "de grasa corporal")

women_age_range()