-- Crear las tablas
CREATE TABLE maquinas_artes_marciales (
    id_maquina INT AUTO_INCREMENT PRIMARY KEY,
    dificultad INT NOT NULL,
    total_golpes INT NOT NULL,
    precision DECIMAL(5, 2) NOT NULL
);

CREATE TABLE sesiones_entrenamiento (
    id_sesion INT AUTO_INCREMENT PRIMARY KEY,
    id_maquina INT,
    fecha DATE NOT NULL,
    golpes_exitosos INT NOT NULL,
    golpes_totales INT NOT NULL,
    fuerza_promedio DECIMAL(5, 2) NOT NULL,
    FOREIGN KEY (id_maquina) REFERENCES maquinas_artes_marciales(id_maquina)
);

-- Insertar datos en maquinas_artes_marciales
INSERT INTO maquinas_artes_marciales (dificultad, total_golpes, precision)
VALUES (1, 0, 0.00), (2, 100, 75.50), (3, 150, 80.00), (4, 200, 85.00), (5, 250, 90.00);

-- Insertar datos en sesiones_entrenamiento
INSERT INTO sesiones_entrenamiento (id_maquina, fecha, golpes_exitosos, golpes_totales, fuerza_promedio)
VALUES (1, '2024-10-01', 8, 10, 60.00), (2, '2024-10-02', 9, 12, 65.50), (3, '2024-10-03', 10, 12, 70.00),
       (4, '2024-10-04', 7, 10, 75.00), (5, '2024-10-05', 6, 9, 80.00);

-- Ejemplo de consultas SELECT
SELECT * FROM maquinas_artes_marciales;

SELECT * FROM sesiones_entrenamiento
WHERE id_maquina = 3;

SELECT AVG(precision) AS promedio_precision
FROM maquinas_artes_marciales;

SELECT * FROM maquinas_artes_marciales
ORDER BY dificultad DESC
LIMIT 1;

SELECT * FROM sesiones_entrenamiento
ORDER BY fuerza_promedio DESC
LIMIT 1;
