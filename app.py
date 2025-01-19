from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mi_base_de_datos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Modelos de base de datos
class Banco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    tipo_convenio = db.Column(db.String(20), nullable=False)

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    banco_id = db.Column(db.Integer, db.ForeignKey("banco.id"), nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    tin = db.Column(db.Float, nullable=False)
    endeudamiento_max = db.Column(db.Float, nullable=False)

class RequisitoFinanciero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey("producto.id"), nullable=False)
    ingresos_minimos = db.Column(db.Float, nullable=False)
    aportacion_minima = db.Column(db.Float, nullable=False)

class RequisitoLaboral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey("producto.id"), nullable=False)
    antiguedad_minima = db.Column(db.Integer, nullable=False)
    tipo_contrato = db.Column(db.String(50), nullable=False)

class Vinculacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey("producto.id"), nullable=False)
    seguros = db.Column(db.String(100))
    domiciliacion_nomina = db.Column(db.Boolean, nullable=False)

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefono = db.Column(db.String(20))

class Solicitud(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("cliente.id"), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey("producto.id"), nullable=False)
    fecha_solicitud = db.Column(db.Date, nullable=False)
    estado = db.Column(db.String(20), nullable=False)

# Rutas de la aplicación
@app.route("/")
def home():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    return f"¡Gracias por enviar el formulario, {name}!"

@app.route("/user/<username>")
def user_profile(username):
    return f"¡Hola, {username}!"

@app.route("/about")
def about():
    return "Esta es la página 'Sobre Nosotros'."

@app.route("/contact")
def contact():
    return "¡Contáctanos en contacto@example.com!"

# Crear la base de datos
@app.route("/create_db")
def create_db():
    db.create_all()
    return "Base de datos y tablas creadas correctamente."

# Añadir un banco
@app.route("/add_banco/<nombre>/<tipo_convenio>")
def add_banco(nombre, tipo_convenio):
    banco = Banco(nombre=nombre, tipo_convenio=tipo_convenio)
    db.session.add(banco)
    db.session.commit()
    return f"Banco {nombre} añadido con convenio: {tipo_convenio}."

if __name__ == "__main__":
    app.run(debug=True)
