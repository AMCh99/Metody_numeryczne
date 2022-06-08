macierz = [ [0,2,3,0],
		 	[4,0,0,0],
			[7,8,0,0],
            [6,0,1,0]]

def wyznacznik(macierz):
    stopien = len(macierz)
    wyz = 0
	
    for x in range(stopien):
        w1 = 1
        for y in range(stopien):
            if x + y < stopien:
                m = macierz[y][x+y]
            else:
                m = macierz[y][x+y-stopien]
			
            w1 = w1 * m
        wyz += w1
	
    for x in range(stopien):
        w1 = 1
        for y in range(stopien):
            if x + y < stopien:
                m = macierz[-y][x+y]
            else:
                m = macierz[-y][x+y-stopien]
			
            w1 = w1 * m	
        wyz -= w1
    
    return wyz

print(wyznacznik(macierz))


