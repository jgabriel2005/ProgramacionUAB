CREATE DATABASE IF NOT EXISTS starcraftdb;
USE starcraftdb;

CREATE TABLE IF NOT EXISTS usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre_usuario VARCHAR(255) NOT NULL,
  correo_electronico VARCHAR(255) NOT NULL UNIQUE,
  contrasena VARCHAR(255) NOT NULL,
  raza VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS unidades (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  tipo VARCHAR(50) NOT NULL,
  ataque INT NOT NULL,
  defensa INT NOT NULL,
  salud INT NOT NULL,
  velocidad FLOAT NOT NULL,
  alcance FLOAT NOT NULL,
  tiempo_construccion INT NOT NULL,
  costo_minerales INT NOT NULL,
  costo_gas INT NOT NULL
);

CREATE TABLE IF NOT EXISTS edificios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  tipo VARCHAR(50) NOT NULL,
  salud INT NOT NULL,
  tiempo_construccion INT NOT NULL,
  costo_minerales INT NOT NULL,
  costo_gas INT NOT NULL,
  unidades_producidas TEXT
);

CREATE TABLE IF NOT EXISTS tecnologias (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  descripcion TEXT,
  tiempo_investigacion INT NOT NULL,
  costo_minerales INT NOT NULL,
  costo_gas INT NOT NULL
);

CREATE TABLE IF NOT EXISTS recursos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usuario_id INT NOT NULL,
  minerales INT NOT NULL,
  gas INT NOT NULL,
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE IF NOT EXISTS logros (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usuario_id INT NOT NULL,
  logro VARCHAR(255) NOT NULL,
  fecha_logro DATE,
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE IF NOT EXISTS amigos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  usuario_id INT NOT NULL,
  amigo_id INT NOT NULL,
  FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
  FOREIGN KEY (amigo_id) REFERENCES usuarios(id)
);

CREATE TABLE IF NOT EXISTS partidas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  jugador1_id INT NOT NULL,
  jugador2_id INT NOT NULL,
  ganador_id INT,
  fecha_partida DATE,
  duracion INT,
  FOREIGN KEY (jugador1_id) REFERENCES usuarios(id),
  FOREIGN KEY (jugador2_id) REFERENCES usuarios(id),
  FOREIGN KEY (ganador_id) REFERENCES usuarios(id)
);
