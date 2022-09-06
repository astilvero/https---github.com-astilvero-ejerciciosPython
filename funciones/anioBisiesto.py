def bisiesto(year):
    if year == 1900:
        return "No es anio bisiesto"
    elif year % 4 == 0:
        return "Es anio bisiesto"
    else:
        return "No es anio bisiesto"

result = bisiesto(2022)
print(result)