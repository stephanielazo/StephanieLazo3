from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':

        ejercicio = request.form.get('ejercicio')

        if ejercicio == '1':
            return redirect(url_for('ejercicio1'))

        elif ejercicio == '2':
            return redirect(url_for('ejercicio2'))

    return render_template('home.html')

@app.route('/Ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        try:

            nota1 = int(request.form['nota1'])
            nota2 = int(request.form['nota2'])
            nota3 = int(request.form['nota3'])
            asistencia = int(request.form['asistencia'])

            if not (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70):
                return "Las notas deben estar entre 10 y 70."
            if not (0 <= asistencia <= 100):
                return "La asistencia debe estar entre 0 y 100."


            promedio = (nota1 + nota2 + nota3) / 3

            estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"

            return render_template('Ejercicio1.html', promedio=promedio, estado=estado)

        except ValueError:
            return "Por favor ingrese valores válidos."

    return render_template('Ejercicio1.html')

@app.route('/Ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':

        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [(nombre1, len(nombre1)), (nombre2, len(nombre2)), (nombre3, len(nombre3))]
        nombre_mayor = max(nombres, key=lambda x: x[1])

        return render_template('Ejercicio2.html', nombre_mayor=nombre_mayor, nombre1=nombre1, nombre2=nombre2,
                               nombre3=nombre3)

    return render_template('Ejercicio2.html', nombre1='', nombre2='', nombre3='')

if __name__ == '__main__':
    app.run(debug=True)