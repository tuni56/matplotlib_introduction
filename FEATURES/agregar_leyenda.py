import pylab as pl
import numpy as np
# Crear una figura de 8x6 puntos de tamaño, 80 puntos por pulgada
pl.figure(figsize=(8, 6), dpi=80)
# Crear una nueva subgráfica en una rejilla de 1x1
pl.subplot(1, 1, 1)
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
# En uno de los parámetros puedo especificar el color y el grosor de l
a línea para la gráfica en este caso elijo Rojo "Red"
# y Grosor 2, el parámetro LineStyle define el tipo de Linea. En este
caso voy a elegir -. para que se diferencie con la
# segunda gráfica. Agrego el Parámetro Label para luego mostrar en la leyenda
pl.plot(X, C, color="Red", linewidth=2.0, linestyle="-.", label="Función Coseno")
# Voy a cambiar de la segunda gráfica el color a Amarillo, Yellow y elGrosor de la Línea a 4, tipor de línea -.
#Agrego el parámetro label para luego mostrar la leyenda
pl.plot(X, S, color="Yellow", linewidth=4.0, linestyle="-", label="Función Seno")
#Configuro los Spines de la siguiente manera
ax = pl.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
# Puedo poner límites para el Eje x. En el punto anterior la gráfica no tenía límites en este caso va a ir de -4 a 4
pl.xlim(-4.0, 4.0)
# Ticks en x - Con xticks puedo cambiar la graduación del eje
pl.xticks(np.linspace(-4, 4, 9, endpoint=True))
# Puedo poner límites para el Eje y. En el punto anterior la gráfica no tenía límites en este caso va a ir de -1 a 1
pl.ylim(-1.0, 1.0)
# Ticks en y Con yticks puedo cambiar la graduación del eje
pl.yticks(np.linspace(-1, 1, 5, endpoint=True))
pl.legend(loc='upper left')
# Muestro el Resultado por Pantalla
pl.show()
