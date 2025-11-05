import csv
from typing import NamedTuple, List
from datetime import date, datetime
from pathlib import Path

Pelicula = NamedTuple(
    "Pelicula",
    [("fecha_estreno", date), 
    ("titulo", str), 
    ("director", str), 
    ("generos",List[str]),
    ("duracion", int),
    ("presupuesto", int), 
    ("recaudacion", int), 
    ("reparto", List[str])
    ]
)

def lee_peliculas(ruta:str)->list[Pelicula]:
    peliculas=[]
    with open (ruta, encoding='utf-8') as f:
        lector=csv.reader(f, delimiter=';')
        next(lector)
        for linea in lector:
            fecha_estreno, titulo, director, generos, duracion, presupuesto, recaudacion, reparto = linea
            pelicula=Pelicula(
                fecha_estreno=datetime.strptime(fecha_estreno, "%d/%m/%Y").date(),
                titulo=titulo,
                director=director,
                generos=generos.split(',') if generos else [],
                duracion=duracion,
                presupuesto=int(presupuesto),
                recaudacion=int(recaudacion),
                reparto=reparto.split(',') if reparto else [] 
                )
            peliculas.append(pelicula)
        return peliculas
if __name__== '__main__':
    ruta = Path('data\peliculas.csv')
    pelicula= lee_peliculas(ruta)

def pelicula_mas_ganancias(peliculas:List[Pelicula], genero:str=None)->tuple[str, int]:
    pelicula_ganancias=str
    ganancias_max=0
    for pelicula in peliculas:
        if genero in pelicula.generos or genero==None:
            ganancias = pelicula.recaudacion-pelicula.presupuesto
            if ganancias>ganancias_max:
                ganancias_max=ganancias
                pelicula_ganancias=pelicula.titulo
    return (pelicula_ganancias, ganancias_max)

def media_presupuesto_por_genero(peliculas:list[Pelicula])->dict[str, float]:
    generos_presupuesto={}
    for pelicula in peliculas:
        for genero in pelicula.generos:
            if genero not in generos_presupuesto:
                generos_presupuesto[genero]= []
            generos_presupuesto[genero].append(pelicula.presupuesto)

    for genero, presupuestos in generos_presupuesto.items():
        generos_presupuesto[genero] = sum(presupuestos)/ len(presupuestos)
    return generos_presupuesto

def peliculas_por_actor(peliculas:list[Pelicula], año_inicial:int=None, año_final:int=None)->dict[str, int]:
    actor_peliculas={}
    for pelicula in peliculas:
        if año_inicial<=pelicula.fecha_estreno.year>=año_final or (año_inicial==None and año_final>=pelicula.fecha_estreno.year) or (año_final==None and año_inicial<=pelicula.fecha_estreno.year) or (año_inicial==None and año_final==None):
            for actor in pelicula.reparto:
                if actor not in actor_peliculas:
                    actor_peliculas[actor]=1
                else:
                    actor_peliculas[actor]+=1
    return actor_peliculas

def actores_mas_frecuentes(peliculas:list[Pelicula], n:int, año_inicial:int=None, año_final:int=None)->list[str]:
    actores_frecuentes=peliculas_por_actor(peliculas, año_final, año_inicial)
    actores_ordenados=sorted(actores_frecuentes.items(), key=lambda x: (-x[1], x[0]))
    resultado=[actor for actor, _ in actores_ordenados[:n]]
    return resultado
