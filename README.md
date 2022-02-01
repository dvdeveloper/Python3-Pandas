# Python 3 Panda - Ejemplos varios
1. DataFrame
   - Crear dataframe de forma manual
   - Listado de indices
   - Filtrar datos de una fila
   - Crear dataframe usando listas
2. CSV, Series y Frame
   - Carga csv a un Dataframe
   - Uso de Head (5 filas)
   - Uso de head (10 filas)
   - Mostrar información del dataframe - info()
   - Mostrar sólo una columna => Series
   - Mostrar 2 columnas => Frames
3. Manipulación de filas
   - Filtrar fila => iloc
   - Filtrar entre filas [X:Y]
   - Obtener las primeras 4 filas [:4]
   - Obtener las últimas 3 filas [-3:]
   - Filtrar por datos en una columna
   - Filtrar por datos > XXX
   - Filtrar datos distintos (!=)
   - Filtrar datos utilizando ó => |
   - Filtrar datos utilizando y => &
   - Filtrar datos utilizando array (in) => isin
4. Reset Index
   - Resetear el indice luego de filtrar dataframe
   - Eliminar columna Index
5. Proyecto Peliculas
   - Crear DataFrame
   - Crear DataFrame utilizando lista
   - Crear CSV formato string
   - Cargar archivo CSV
   - Mostrar información del DataFrame
6. Proyecto Clinica
   - Crear DataFrame clinica
   - filtrar clinica: clinic_north
   - filtrar clinica: clinic_north y clinic_south
   - obtener visitas de marzo para todas las clinicas
   - obtener visitas en Enero
   - Obtener visitas en Marzo y Abril
   - Obtener visitas en Enero,Febrero y Marzo
   - Resetear index del DataFrame
7. Modificación de DataFrame
   - Agregar nueva columna
   - Agregar columna boolean 
   - Agregar nueva columna + aritmetica
   - Agregar nueva columna + utilizando función upper()
   - Renombrar columnas
   - Eliminar columna
8. Función lambda
   - Ejemplo básico de lambda
   - Agregar nueva columna utilizando lambda 
   - Lambda row (fila)
9. Tienda de Zapatos - Lambda
   - Crear DataFrame
   - Agregar columna: Sold in Bulk?
   - Agregar columna: Is taxed?
   - Agregar columna: revenue -> realizar calculo
   - Obtener apellido a través de lambda
   - Agregar columna: last_name
   - Cargar CSV
   - Modificar nombre de columnas
   - Modificar sólo 1 columna, Title: Movie Title
   - Agregar columna: Shoe Source utilizando Lambda
   - Agregar columna: salutation utilizando Lambda
10. Tienda de Jardineria - Lambda
	- Cargar CSV
	- Filtrar ubicación por: Staten Island
	- Agregar columna: in_stock utilizando Lambda
	- Agregar columna: total_value -> Calculando utilizando Price * Quantity
	- Agregar columna: full_description utilizando lamda (valores de 2 columnas)
11. Agregación
	- Obtener mediana
	- Obtener valores únicos (nunique y unique)
	- Obtener máximos y minimos
	- Agrupación: Obtener el rating máximo por genero
	- Resetear el index de la agrupación