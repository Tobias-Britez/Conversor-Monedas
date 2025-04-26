def ARSCONVERT():
    if Moneda1 == 1 and Moneda2 == 2:
        print ("Has elegido el cambio de ARS a USD...")
        ARS = float(input("Ingrese la cantidad de ARS que desea convertir... "))
        ValorUSD = 1200
        ARSTOTAL = ARS/ValorUSD
        print ("La cantidad de ",ARS," pesos, equivale a ",ARSTOTAL,"USD")
    elif Moneda1 == 1 and Moneda2 == 3:
        print ("Has elegido el cambio de ARS a EUR")
        ARS = float(input("Ingrese la cantidad de ARS que desea convertir... "))
        ValorEUR = 1327
        ARSTOTAL = ARS/ValorEUR
        print ("La cantidad de ",ARS," pesos, equivale a ",ARSTOTAL,"EUR")
    elif Moneda1 == 1 and Moneda2 == 4:
        print ("Has elegido el cambio de ARS a BRL")
        ARS = float(input("Ingrese la cantidad de ARS que desea convertir... "))
        ValorBRL = 204
        ARSTOTAL = ARS/ValorBRL
        print ("La cantidad de ",ARS," pesos, equivale a ",ARSTOTAL,"USD")
def USDCONVERT():
    if Moneda1 == 2 and Moneda2 == 1:
        USD = float(input("Ingrese la cantidad de USD que desea convertir... "))
        ValorARS = 0,86
        USDTOTAL = USD/ValorARS
        print ("La cantidad de ",USD," USD, equivale a ",ValorARS,"ARS")
    elif Moneda1 == 2 and Moneda2 == 3:
        USD = float(input("Ingrese la cantidad de USD que desea convertir... "))
        ValorEUR = 1,14
        USDTOTAL = USD/ValorEUR
        print ("La cantidad de ",USD," USD, equivale a ",ValorEUR,"EUROS")
    elif Moneda1 == 2 and Moneda2 == 4:
        USD = float(input("Ingrese la cantidad de USD que desea convertir... "))
        ValorBRL = 0,18
        USDTOTAL = USD/ValorBRL
        print ("La cantidad de ",USD," USD, equivale a ",ValorARS,"BRL")
print ("Bienvenido al conversor de monedas L O L")
Moneda1 = int(input("¿Que monedas quieres convertir? [1] ARS, [2] USD, [3] EUR [4] BRL: "))
Moneda2 = int(input("¿A que moneda quieres convertir? [1] ARS, [2] USD, [3] EUR [4] BRL: "))
if Moneda1 == Moneda2:
    print ("No puedes convertir en la misma moneda")
elif Moneda1 == 1:
    ARSCONVERT()
elif Moneda2 == 2:
    USDCONVERT()
