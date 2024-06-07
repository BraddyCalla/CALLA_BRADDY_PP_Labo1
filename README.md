Se dispone de un archivo con datos acerca de los servicios de un taller de costura, que tiene el
siguiente formato:
id_servicio, descripción (del servicio), tipo (1-MINORISTA, 2-MAYORISTA, 3-EXPORTAR),
precioUnitario, cantidad, totalServicio
Ejemplo: {

"id_servicio": "50",
"descripcion": "ruedo pantalon",
"tipo": "1",
"precioUnitario": "250",
"cantidad": "2",
"totalServicio": "0"
}

Se deberá realizar un programa que permita el análisis de dicho archivo y sea capaz de generar
nuevos archivos de salida de formato similar filtrados por varios criterios:
El programa contará con el siguiente menú:
1) Cargar archivo: Se pedirá el nombre del archivo y se cargarán en una lista los elementos
del mismo.
2) Imprimir lista: Se imprimirá por pantalla la tabla (en forma de columnas) con los datos de los
servicios.
3) Asignar totales: Se deberá hacer uso de una función lambda que asignará a cada servicio el
total calculado (totalServicio) de la siguiente forma: cantidad x precioUnitario.
4) Filtrar por tipo: Se deberá generar un archivo igual al original, pero donde solo aparezcan
servicios del tipo seleccionado.
5) Mostrar servicios: Se deberá mostrar por pantalla un listado de los servicios ordenados por
descripción de manera ascendente.
6) Guardar servicios: Se deberá guardar el listado del punto anterior en un archivo de tipo json.
7) Salir.
Requerimientos del desarrollo. •
nota: el código deberá tener comentarios con la documentación de cada una de las funciones y
respetar las reglas de estilo de la cátedra.
nota bis: separar las funciones en distintas bibliotecas.

Para nota de aprobación, se deberán realizar como mínimo 3 puntos.
Para nota de promoción se deberán realizar como mínimo 4 puntos.