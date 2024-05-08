import sqlite3

# Conectar a la base de datos (si no existe, se creará)
conn = sqlite3.connect('puertos.db')

# Crear cursor
cursor = conn.cursor()

# Crear tabla para generales
cursor.execute('''
    CREATE TABLE Generales (
        puerto_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_pu TEXT NOT NULL,
        direccion TEXT NOT NULL,
        telefono TEXT NOT NULL,
        mail TEXT NOT NULL
    )
''')

# Crear tabla para responsables
cursor.execute('''
    CREATE TABLE Responsables (
        responsable_id INTEGER PRIMARY KEY AUTOINCREMENT,
        puerto_id INTEGER NOT NULL,
        nombre_res TEXT NOT NULL,
        apellidos TEXT NOT NULL,
        cargo_res TEXT NOT NULL,
        FOREIGN KEY (puerto_id) REFERENCES Generales(puerto_id)
    )
''')

# Crear tabla para socioeconomicos
cursor.execute('''
    CREATE TABLE Socioeconomicos (
        socioeconomico_id INTEGER PRIMARY KEY AUTOINCREMENT,
        puerto_id INTEGER NOT NULL,
        trab_total INTEGER,
        trab_hombres INTEGER,
        trab_mujeres INTEGER,
        volumen_ventas REAL,
        colaboracion TEXT,
        plan_estrategico_enlace TEXT,
        plan_estrategico_descripcion TEXT,
        plan_transicion_energetica_enlace TEXT,
        plan_transicion_energetica_descripcion TEXT,
        plan_igualdad_enlace TEXT,
        plan_igualdad_descripcion TEXT,
        FOREIGN KEY (puerto_id) REFERENCES Generales(puerto_id)
    )
''')

# Crear tabla para resultado explotacion
cursor.execute('''
    CREATE TABLE ResultadoExplotacion (
        resultado_id INTEGER PRIMARY KEY AUTOINCREMENT,
        puerto_id INTEGER NOT NULL,
        anio_ex INTEGER,
        valor_ex REAL,
        FOREIGN KEY (puerto_id) REFERENCES Socioeconomicos(puerto_id)
    )
''')

# Crear tabla para resultado ejercicio
cursor.execute('''
    CREATE TABLE ResultadoEjercicio (
        resultado_id INTEGER PRIMARY KEY AUTOINCREMENT,
        puerto_id INTEGER NOT NULL,
        anio_ej INTEGER,
        valor_ej REAL,
        FOREIGN KEY (puerto_id) REFERENCES Socioeconomicos(puerto_id)
    )
''')

# Crear tabla para inversiones
cursor.execute('''
    CREATE TABLE Inversiones (
        inversion_id INTEGER PRIMARY KEY AUTOINCREMENT,
        puerto_id INTEGER NOT NULL,
        anio_in INTEGER,
        valor_in REAL,
        FOREIGN KEY (puerto_id) REFERENCES Socioeconomicos(puerto_id)
    )
''')

# Crear tabla para categorias de inversiones
cursor.execute('''
    CREATE TABLE CategoriasInversiones (
        categoria_id INTEGER PRIMARY KEY AUTOINCREMENT,
        inversion_id INTEGER NOT NULL,
        puerto_id INTEGER NOT NULL,
        nombre_cat TEXT,
        valor_cat REAL,
        FOREIGN KEY (inversion_id) REFERENCES Inversiones(inversion_id),
        FOREIGN KEY (puerto_id) REFERENCES Socioeconomicos(puerto_id)
    )
''')

# Crear tabla para tecnicos
cursor.execute('''
    CREATE TABLE Tecnicos (
        create_id INTEGER PRIMARY KEY AUTOINCREMENT,
        puerto_id INTEGER NOT NULL,
        consumo_electrico_total REAL,
        autoconsumo REAL,
        consumo_electrico_clientes REAL,
        venta_energetica_red REAL,
        nivel_proteccion_ambiental INTEGER,
        FOREIGN KEY (puerto_id) REFERENCES Generales(puerto_id)
    )
''')

# Crear tabla para zonas de consumo electrico
cursor.execute('''
    CREATE TABLE ZonasConsumoElectrico (
        zona_id INTEGER PRIMARY KEY AUTOINCREMENT,
        puerto_id INTEGER NOT NULL,
        nombre_zona TEXT,
        valor_zona REAL,
        FOREIGN KEY (puerto_id) REFERENCES Tecnicos(puerto_id)
    )
''')

# Crear tabla para franjas horarias de consumo electrico
cursor.execute('''
    CREATE TABLE FranjasHorariasConsumoElectrico (
        franja_id INTEGER PRIMARY KEY AUTOINCREMENT,
        puerto_id INTEGER NOT NULL,
        franja_inicio TEXT,
        franja_fin TEXT,
        valor_franja REAL,
        FOREIGN KEY (puerto_id) REFERENCES Tecnicos(puerto_id)
    )
''')

# Crear tabla para usos de consumo electrico
cursor.execute('''
    CREATE TABLE UsosConsumoElectrico (
        uso_id INTEGER PRIMARY KEY AUTOINCREMENT,
        puerto_id INTEGER NOT NULL,
        nombre_uso TEXT,
        valor_uso REAL,
        FOREIGN KEY (puerto_id) REFERENCES Tecnicos(puerto_id)
    )
''')

# Crear tabla para diques
cursor.execute('''
    CREATE TABLE Diques (
        dique_id INTEGER PRIMARY KEY AUTOINCREMENT,
        puerto_id INTEGER NOT NULL,
        nombre_dique TEXT,
        amplitud REAL,
        periodo REAL,
        velocidad REAL,
        longitud_onda REAL,
        profundidad REAL,
        escullera BOOLEAN,
        FOREIGN KEY (puerto_id) REFERENCES Tecnicos(puerto_id)
    )
''')

# Guardar cambios
conn.commit()

# Cerrar conexión
conn.close()