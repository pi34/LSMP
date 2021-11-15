def equilibrium (N, Am, AC, AT):

    N = int(input("How Many Bodies Do You Have? "))

    for i in range(N):
        m = int(input("What is the mass of Body", str(i+1) + "?"))
        C = int(input("What is the Specific Heat Capacity of Body", str(i+1) + "?"))
        T = int(input("What is the initial temperature of Body", str(i+1) + "?"))

        Am.append(m)
        AC.append(C)
        AT.append(T)

    numerator = 0
    denominator = 0

    for i in range(N):
        numerator = numerator + (Am[i]*AC[i]*AT[i])
        denominator = denominator + (Am[i]*AC[i])

    return (numerator / denominator)
