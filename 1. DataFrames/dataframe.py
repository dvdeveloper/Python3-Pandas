#importar librería panda. Una buena practica es utilizar un alias pd (as)
import pandas as pd

#crear dataframe de forma manual
df1 = pd.DataFrame({
    'nombre': ['Diego','Jaime','Martin'],
    'direccion': ['Santiago','Las Condes','Estación Central'],
    'edad': [31,30,38]
})

#imprimir dataframe. Primera columna es el indice (key único)
print(df1)

#listar todos los indices del dataframe
df1.index

#ver el dato de una fila en particular
df1.loc[2]

#crear dataframe utilizando lista
df2 = pd.DataFrame([
    ['Diego','Santiago',31],
    ['Jaime','Las Condes',30],
    ['Martin','Estación Central',38]
],
columns=['nombre','direccion','edad'])

#imprimir dataframe de lista
print(df2)