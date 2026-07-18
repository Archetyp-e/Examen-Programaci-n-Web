from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal con menú
@app.route('/')
def index():
    return render_template('index.html')

# Ejercicio 1: cálculo de compras
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio_unitario = 9000
        total_sin_descuento = cantidad * precio_unitario

        # Lógica de descuentos
        if 18 <= edad <= 30:
            descuento = 0.15 * total_sin_descuento
        elif edad > 30:
            descuento = 0.25 * total_sin_descuento
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento - descuento

        return render_template(
            'ejercicio1.html',
            nombre=nombre,
            total_sin_descuento=total_sin_descuento,
            descuento=descuento,
            total_con_descuento=total_con_descuento
        )
    return render_template('ejercicio1.html')

# Ejercicio 2: login
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario'].lower()
        contrasena = request.form['contrasena']

        if usuario == "juan" and contrasena == "admin":
            mensaje = f"Bienvenido Administrador {usuario}"
        elif usuario == "pepe" and contrasena == "user":
            mensaje = f"Bienvenido Usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template('ejercicio2.html', mensaje=mensaje)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)

