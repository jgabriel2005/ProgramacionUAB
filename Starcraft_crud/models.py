from __init__ import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(255), nullable=False)
    correo_electronico = db.Column(db.String(255), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)
    raza = db.Column(db.String(50), nullable=False)

class Unidad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    ataque = db.Column(db.Integer, nullable=False)
    defensa = db.Column(db.Integer, nullable=False)
    salud = db.Column(db.Integer, nullable=False)
    velocidad = db.Column(db.Float, nullable=False)
    alcance = db.Column(db.Float, nullable=False)
    tiempo_construccion = db.Column(db.Integer, nullable=False)
    costo_minerales = db.Column(db.Integer, nullable=False)
    costo_gas = db.Column(db.Integer, nullable=False)

class Edificio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    salud = db.Column(db.Integer, nullable=False)
    tiempo_construccion = db.Column(db.Integer, nullable=False)
    costo_minerales = db.Column(db.Integer, nullable=False)
    costo_gas = db.Column(db.Integer, nullable=False)
    unidades_producidas = db.Column(db.String, nullable=True)

class Tecnologia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.String, nullable=True)
    tiempo_investigacion = db.Column(db.Integer, nullable=False)
    costo_minerales = db.Column(db.Integer, nullable=False)
    costo_gas = db.Column(db.Integer, nullable=False)

class Recurso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    minerales = db.Column(db.Integer, nullable=False)
    gas = db.Column(db.Integer, nullable=False)

class Logro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    logro = db.Column(db.String(255), nullable=False)
    fecha_logro = db.Column(db.Date, nullable=False)

class Amigo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    amigo_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

class Partida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jugador1_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    jugador2_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    ganador_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    fecha_partida = db.Column(db.Date, nullable=False)
    duracion = db.Column(db.Integer, nullable=False)
