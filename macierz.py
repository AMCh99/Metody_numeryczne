macierz = [ [1,2,3],
		 	[4,5,0],
			[7,8,9]]

stopien = len(macierz)
def wyznacznik(macierz):
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

wyznacznik(macierz)


