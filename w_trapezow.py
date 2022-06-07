def fcja(x):
    x = eval(function)
    return x


def integrate(function, a, b,x1,w):
    if w == 1:
        i = (b - a)/x1
        dx = (b - a) / i
        integr = 0
        x = b
        x = eval(function)
        bx = x
        x = 0
        for x in range(int(i)):
            x = x * dx + a
            x = eval(function)
            print(x)
            integr += x
            print(integr)
    
    
        return (0.5 * x1) * (2 * integr + bx)


    if w == 2:
        i = (b - a)/(2 * x1)
        dx = (b - a) / i
        integr = 0
        x = b
        x = eval(function)
        bx = x
        x = 0
        for x in range(int(i)):
            x = x * dx + a
            x = eval(function)
            print(x)
            integr += x
            print(integr)
        
        return (x1/3) * (fcja(a) + (4 * (2 * integr + bx)))

 
def main(args):
    function = input("Funkcja: ")
    w = int(input("jaki wzor 1-trapezow, 2-parabol: "))
    a = float(input("Początek przedziału: "))
    b = float(input("Koniec przedziału: "))
    #i = int(input("Liczba podprzedziałów: "))
    x1 = float(input("Podaj x1 dl kroku: "))
    print("Całka = {integrate}".format(integrate = integrate(function, a, b, x1, w)))
    return 0
 
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
