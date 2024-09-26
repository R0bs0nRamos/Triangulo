
from flask import Flask, render_template, request 

app = Flask(__name__)

def classificar_triangulo(lado1, lado2, lado3):

    """
    Clasifica un triángulo según las medidas de sus lados.

 Argumentos:
 lado1 (flotante): Medida del primer lado.
 lado2 (flotante): Medida del segundo lado.
 side3 (flotante): Medida del tercer lado.

 Devoluciones:
 str: Tipo de triángulo (equilátero, isósceles, escaleno o inválido).
    """

    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        return "Medidas no válidas. Todos los lados deben ser mayores que cero."

    if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
        return "No es un triângulo válido."

    if lado1 == lado2 == lado3:
        return "Equilátero. Todos los tres lados y ángulos son iguales. Ángulos = 60°, 60°, 60°."
    
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles. Dos lados iguales y uno diferente. Ángulos = 70°, 70°, 40°."
    
    else:
        return "Escaleno. Todos los lados y ángulos son diferentes. Ángulos = 50°, 60°, 70°."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lado1 = float(request.form['lado1'])
        lado2 = float(request.form['lado2'])
        lado3 = float(request.form['lado3'])
        resultado = classificar_triangulo(lado1, lado2, lado3)
        return render_template('resultado.html', resultado=resultado)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)