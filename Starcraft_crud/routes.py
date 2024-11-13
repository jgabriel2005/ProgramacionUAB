from flask import request, jsonify
from __init__ import app, mysql
from werkzeug.security import generate_password_hash, check_password_hash

# Registro
@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    nombre_usuario = data['nombre_usuario']
    correo_electronico = data['correo_electronico']
    contrasena = generate_password_hash(data['contrasena'])
    raza = data['raza']
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO usuarios (nombre_usuario, correo_electronico, contrasena, raza) VALUES (%s, %s, %s, %s)", (nombre_usuario, correo_electronico, contrasena, raza))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({"mensaje": "Usuario registrado exitosamente!"})

# Inicio de sesión
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    correo_electronico = data['correo_electronico']
    contrasena = data['contrasena']
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios WHERE correo_electronico = %s", (correo_electronico,))
    usuario = cur.fetchone()
    cur.close()

    if usuario and check_password_hash(usuario[3], contrasena):  # Asumiendo que la contraseña está en la cuarta columna
        return jsonify({"mensaje": "Inicio de sesión exitoso!"})
    else:
        return jsonify({"mensaje": "Correo electrónico o contraseña incorrectos."}), 401

# CRUD para unidades
@app.route('/unidades', methods=['GET'])
def obtener_unidades():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM unidades")
    unidades = cur.fetchall()
    cur.close()
    return jsonify([{
        "id": unidad[0],
        "nombre": unidad[1],
        "tipo": unidad[2],
        "ataque": unidad[3],
        "defensa": unidad[4],
        "salud": unidad[5],
        "velocidad": unidad[6],
        "alcance": unidad[7],
        "tiempo_construccion": unidad[8],
        "costo_minerales": unidad[9],
        "costo_gas": unidad[10]
    } for unidad in unidades])

@app.route('/unidades', methods=['POST'])
def crear_unidad():
    data = request.get_json()
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO unidades (nombre, tipo, ataque, defensa, salud, velocidad, alcance, tiempo_construccion, costo_minerales, costo_gas) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (data['nombre'], data['tipo'], data['ataque'], data['defensa'], data['salud'], data['velocidad'], data['alcance'], data['tiempo_construccion'], data['costo_minerales'], data['costo_gas']))
    mysql.connection.commit()
    cur.close()
    return jsonify({"mensaje": "Unidad creada exitosamente!"})

@app.route('/unidades/<int:id>', methods=['PUT'])
def actualizar_unidad(id):
    data = request.get_json()
    cur = mysql.connection.cursor()
    cur.execute("UPDATE unidades SET nombre=%s, tipo=%s, ataque=%s, defensa=%s, salud=%s, velocidad=%s, alcance=%s, tiempo_construccion=%s, costo_minerales=%s, costo_gas=%s WHERE id=%s",
                (data['nombre'], data['tipo'], data['ataque'], data['defensa'], data['salud'], data['velocidad'], data['alcance'], data['tiempo_construccion'], data['costo_minerales'], data['costo_gas'], id))
    mysql.connection.commit()
    cur.close()
    return jsonify({"mensaje": "Unidad actualizada exitosamente!"})

@app.route('/unidades/<int:id>', methods=['DELETE'])
def eliminar_unidad(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM unidades WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({"mensaje": "Unidad eliminada exitosamente!"})

# Rutas adicionales para edificios, tecnologías, logros, amigos y partidas pueden seguir un patrón similar
