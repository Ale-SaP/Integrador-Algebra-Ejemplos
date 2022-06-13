def mcm( numero ):
    if numero < 2:
        return numero

    elif (numero >= 2): 
        if (numero % 2 == 0):
            return mcm( numero//2 )

        elif (numero % 3 == 0):
            return mcm( numero//3 )

        else:
            for x in range(4, numero + 1 ):
                if (numero % x == 0):
                    return mcm(numero // x)