from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Xanandra131313@localhost/mi_flask_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<Usuario {self.nombre}>'

# Crear tablas
with app.app_context():
    db.create_all()

# Rutas
@app.route('/')
def inicio():
    return '¡Bienvenido a tu app Flask con PostgreSQL!'

@app.route('/add_user/<nombre>/<email>')
def add_user(nombre, email):
    usuario = Usuario(nombre=nombre, email=email)
    db.session.add(usuario)
    db.session.commit()
    return f'Usuario {nombre} agregado con éxito.'

@app.route('/usuarios')
def usuarios():
    usuarios = Usuario.query.all()
    return '<br>'.join([f'{u.id} - {u.nombre} - {u.email}' for u in usuarios])

# Ejecutar servidor
if __name__ == '__main__':
    app.run(debug=True)
