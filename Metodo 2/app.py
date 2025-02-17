# El presente proyecto data de un modelo para alertar sobre la 
# proximidad por fechas implementado de proyectos que necesiten 
# de distintas formas de alertar o visualizar la progreción del tiempo

# Todos los derechos reservados.
# Copyright © 2023 Deivid Edwuar Bautista Ocampo - Jhonatan David Florez Useche


# Importar los distintos modulos que utilizaremos en este metodo número 2
from flask import Flask, render_template
from datetime import date, timedelta

app = Flask(__name__)

# Lista arbitraria de procesos con fechas de inicio y fecha límite
procesos = [
    {"nombre": "Proceso 1", "fecha_inicio": date(2023, 9, 1), "fecha_limite": date(2023, 9, 10)},
    {"nombre": "Proceso 2", "fecha_inicio": date(2023, 8, 25), "fecha_limite": date(2023, 9, 15)},
    {"nombre": "Proceso 3", "fecha_inicio": date(2023, 9, 3), "fecha_limite": date(2023, 9, 5)},
    {"nombre": "Proceso 4", "fecha_inicio": date(2023, 8, 28), "fecha_limite": date(2023, 10, 25)},
]

umbral_maximo_dias = 30

for proceso in procesos:
    diferencia = proceso["fecha_limite"] - proceso["fecha_inicio"]
    
    progreso = 1.0 - min(diferencia.days / umbral_maximo_dias, 1.0)

    if progreso <= 0:
        progreso = 0.03
    # Redondear el valor de progreso a un número entero
    proceso["diferencia_dias"] = diferencia.days
    proceso["progreso"] = round(progreso * 100)


# Ruta para mostrar la lista de procesos
@app.route('/')
def lista_de_procesos():
    # Obtener la fecha actual
    hoy = date.today()

    return render_template('index.html', procesos=procesos, hoy=hoy)

if __name__ == '__main__':
    app.run(debug=True, port=3040)
