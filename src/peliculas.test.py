from peliculas import *
if __name__== '__main__':
    ruta = Path('data\peliculas.csv')
    pelicula= lee_peliculas(ruta)
    #TEST 1
    #print(pelicula)
    
    #TEST 2
    print('La pelicula con más ganancias es:',pelicula_mas_ganancias(pelicula, 'Acción'))

    #TEST 3
    print(media_presupuesto_por_genero(pelicula))

    #TEST 4
    print(peliculas_por_actor(pelicula, 2010, 2018))

    #TEST 5
    print(actores_mas_frecuentes(pelicula, 3, 2000, 2020))

