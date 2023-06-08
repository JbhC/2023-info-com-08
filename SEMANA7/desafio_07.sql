CREATE DATABASE desafio_07;

USE desafio_07;

CREATE TABLE comentario (
    
    id INT PRIMARY KEY, 
    id_articulo int(6),
    id_usuario INT (4),
    contenido VARCHAR(255),
    fecha_hora DATETIME,

);
