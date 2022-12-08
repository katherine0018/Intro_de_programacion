# Intro_de_programacion
Clase de programacion en UNIBE

# Introducción

En este repositorio se va a hacer el ejercicio de "Refinando código" de la actividad PP5 - Calidad y archivos.
Las metas de este es limpiar el código utilizando herramientas como pylint y autopep8., y subirlo a un repositiorio de GitHub.

# Refactorización

El primer paso ha sido producir la funcionalidad que convierte el documento externo a una lista utilizando herramientas como with open() y se guardó en una variable que después es retornada al cliente. Después de esto se logró la segunda funcionalidad que toma como parametro la variable de la primera funcionalidad, y después sumo todos los valores de la lista. La tercera funcionalidad es la primordial que llama a ambas funcionalidades anteriores e imprime el resultado.

# Limpieza
Se uso pylint para lograr una puntuación de mi trabajo y los errores que se deberían componer. La mayor parte de dichos errores eran añadir docstrings a las funcionalidades y añadir datos como el encoding al abrir el documento. Al terminar con esto, utilice autopep8 para formatear el trabajo de aquel modo, y después copié el resultado.

# Gestión de errores
*Control de errores*

En la ejecución de código, los errores que más salieron fueron al utilizar 'with open()' para abrir el documento con los costos que después ha sido arreglado al modificar el formato de la funcionalidad y ciertos errores de indentación. Además de esto, otro error que encontre fue en la creación de la función principal 'main()' en la que no imprimía la respuesta correcta, este fue arreglado al hacer que la segunda función 'total()' coja como parámetro la primera función 'costs_list()'.

*Pruebas unitarias*

Cada una de estas pruebas fueron realizada con la herramienta pytest. Las primera prueba usada ha sido para verificar que la lista de costos sea adecuada. La segunda prueba ha sido para confirmar que el precio total sea conveniente. La última prueba se uso para cofnirmar que la funcionalidad primordial no devuelva ningún otro dato excepto el resultado de ambas funcionalidades anteriores.

Link al repositorio: https://github.com/katherine0018/Intro_de_programacion.git

<img width="1256" alt="Captura de Pantalla 2022-12-08 a la(s) 7 20 53 p  m" src="https://user-images.githubusercontent.com/116019483/206587544-c29ab146-93fe-48c8-a317-370c2a8144b0.png">
