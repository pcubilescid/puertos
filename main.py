from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_port', methods=['GET', 'POST'])
def add_port():
    if request.method == 'POST':
        if request.form.get('confirmacion') == 'Aceptar':
            # Obtener datos del formulario
            nombre = request.form['nombre']
            direccion = request.form['direccion']
            telefono = request.form['telefono']
            email = request.form['email']
            num_trabajadores_total = request.form['num_trabajadores_total']
            num_trabajadores_hombres = request.form['num_trabajadores_hombres']
            num_trabajadores_mujeres = request.form['num_trabajadores_mujeres']
            volumen_ventas = request.form['volumen_ventas']
            colaboracion = request.form['colaboracion']
            plan_estrategico_enlace = request.form['plan_estrategico_enlace']
            plan_estrategico_descripcion = request.form['plan_estrategico_descripcion']
            plan_transicion_energetica_enlace = request.form['plan_transicion_energetica_enlace']
            plan_transicion_energetica_descripcion = request.form['plan_transicion_energetica_descripcion']
            plan_igualdad_enlace = request.form['plan_igualdad_enlace']
            plan_igualdad_descripcion = request.form['plan_igualdad_descripcion']

            # Conexión a la base de datos
            conn = sqlite3.connect('puertos.db')
            cursor = conn.cursor()

            try:
                # Insertar datos en la tabla 'Generales'
                cursor.execute('''
                    INSERT INTO Generales (nombre_pu, direccion, telefono, mail)
                    VALUES (?, ?, ?, ?)
                ''', (nombre, direccion, telefono, email))

                # Obtener el ID del último puerto insertado
                puerto_id = cursor.lastrowid

                # Obtener los responsables del formulario
                responsables = []
                for i in range(1, 11):  # Máximo de 10 responsables
                    responsable_nombre = request.form.get(f'nombre_responsable_{i}')
                    responsable_apellidos = request.form.get(f'apellidos_responsable_{i}')
                    responsable_cargo = request.form.get(f'cargo_responsable_{i}')
                    if responsable_nombre and responsable_apellidos and responsable_cargo:  # Si se proporciona nombre y cargo
                        responsables.append((responsable_nombre, responsable_apellidos,  responsable_cargo))

                # Insertar responsables en la base de datos
                for responsable in responsables:
                    cursor.execute('''
                        INSERT INTO responsables (puerto_id, nombre_res, apellidos, cargo_res)
                        VALUES (?, ?, ?, ?)
                    ''', (puerto_id, responsable[0], responsable[1], responsable[2]))

                # Insertar datos en la tabla 'Socioeconomicos'
                cursor.execute('''
                    INSERT INTO Socioeconomicos (puerto_id, trab_total, trab_hombres, trab_mujeres, volumen_ventas, colaboracion, plan_estrategico_enlace, plan_estrategico_descripcion, plan_transicion_energetica_enlace, plan_transicion_energetica_descripcion, plan_igualdad_enlace, plan_igualdad_descripcion)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (puerto_id, num_trabajadores_total, num_trabajadores_hombres, num_trabajadores_mujeres, volumen_ventas,
                      colaboracion, plan_estrategico_enlace, plan_estrategico_descripcion,
                      plan_transicion_energetica_enlace, plan_transicion_energetica_descripcion, plan_igualdad_enlace,
                      plan_igualdad_descripcion))

                # Obtener los resultados de explotacion del formulario
                explotaciones = []
                for i in range(1, 11):  # Máximo de 10 responsables
                    anio_explotacion = request.form.get(f'anio_explotacion_{i}')
                    valor_explotacion = request.form.get(f'valor_explotacion_{i}')
                    if anio_explotacion and valor_explotacion:  # Si se proporciona nombre y cargo
                        explotaciones.append((anio_explotacion, valor_explotacion))

                for explotacion in explotaciones:
                    cursor.execute('''
                        INSERT INTO ResultadoExplotacion (puerto_id, anio_ex, valor_ex)
                        VALUES (?, ?, ?)
                    ''', (puerto_id, explotacion[0], explotacion[1]))

                # Obtener los resultados de ejercicio del formulario
                ejercicios = []
                for i in range(1, 11):  # Máximo de 10 responsables
                    anio_ejercicio = request.form.get(f'anio_ejercicio_{i}')
                    valor_ejercicio = request.form.get(f'valor_ejercicio_{i}')
                    if anio_ejercicio and valor_ejercicio:  # Si se proporciona nombre y cargo
                        ejercicios.append((anio_ejercicio, valor_ejercicio))

                for ejercicio in ejercicios:
                    cursor.execute('''
                                INSERT INTO ResultadoEjercicio (puerto_id, anio_ej, valor_ej)
                                VALUES (?, ?, ?)
                            ''', (puerto_id, ejercicio[0], ejercicio[1]))

                # Obtener los resultados de inversiones del formulario
                inversiones = []
                categorias = []
                for i in range(1, 11):  # Máximo de 10 responsables
                    anio_inversion = request.form.get(f'anio_inversion_{i}')
                    valor_inversion = request.form.get(f'valor_inversion_{i}')
                    # Obtener los resultados de categorias de inversiones del formulario
                    for j in range(1, 11):  # Máximo de 10 responsables
                        nombre_categoria = request.form.get(f'nombre_categoria_{i}_{j}')
                        valor_categoria = request.form.get(f'valor_categoria_{i}_{j}')
                        if nombre_categoria and valor_categoria:  # Si se proporciona nombre y cargo
                            categorias.append((nombre_categoria, valor_categoria))
                    if anio_inversion and valor_inversion:  # Si se proporciona nombre y cargo
                        inversiones.append((anio_inversion, valor_inversion))


                for inversion in inversiones:
                    cursor.execute('''
                                        INSERT INTO Inversiones (puerto_id, anio_in, valor_in)
                                        VALUES (?, ?, ?)
                                    ''', (puerto_id, inversion[0], inversion[1]))
                    inversion_id = cursor.lastrowid

                    for categoria in categorias:
                        cursor.execute('''
                                            INSERT INTO CategoriasInversiones (inversion_id, puerto_id, nombre_cat, valor_cat)
                                            VALUES (?, ?, ?, ?)
                                        ''', (inversion_id, puerto_id, categoria[0], categoria[1]))

                # Insertar datos en la tabla 'Tecnicos'
                consumo_electrico_total = request.form['consumo_electrico_total']
                consumo_electrico_autoconsumo = request.form['consumo_electrico_autoconsumo']
                consumo_electrico_clientes = request.form['consumo_electrico_clientes']
                venta_energetica_red = request.form['venta_energetica_red']
                nivel_proteccion_ambiental = request.form['nivel_proteccion_ambiental']
                cursor.execute('''
                    INSERT INTO Tecnicos (puerto_id, consumo_electrico_total, autoconsumo, consumo_electrico_clientes, venta_energetica_red, nivel_proteccion_ambiental)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (puerto_id, consumo_electrico_total, consumo_electrico_autoconsumo, consumo_electrico_clientes,
                      venta_energetica_red, nivel_proteccion_ambiental))


                # Obtener los resultados de zonas consumo electrico  del formulario
                zonas = []
                for i in range(1, 11):  # Máximo de 10 responsables
                    zona_nombre = request.form.get(f'zona_nombre_{i}')
                    zona_consumo = request.form.get(f'zona_consumo_{i}')
                    if zona_nombre and zona_consumo:  # Si se proporciona nombre y cargo
                        zonas.append((zona_nombre, zona_consumo))

                for zona in zonas:
                    cursor.execute('''
                                    INSERT INTO ZonasConsumoElectrico (puerto_id, nombre_zona, valor_zona)
                                    VALUES (?, ?, ?)
                                ''', (puerto_id, zona[0], zona[1]))

                # Obtener los resultados de franjas horarias de consumo electrico  del formulario
                franjas = []
                for i in range(1, 11):  # Máximo de 10 responsables
                    franja_inicio = request.form.get(f'franja_inicio_{i}')
                    franja_fin = request.form.get(f'franja_fin_{i}')
                    franja_consumo = request.form.get(f'franja_consumo_{i}')
                    if franja_inicio and franja_fin and franja_consumo:  # Si se proporciona nombre y cargo
                        franjas.append((franja_inicio, franja_fin, franja_consumo))

                for franja in franjas:
                    cursor.execute('''
                                INSERT INTO FranjasHorariasConsumoElectrico (puerto_id, franja_inicio, franja_fin, valor_franja)
                                VALUES (?, ?, ?, ?)
                            ''', (puerto_id, franja[0], franja[1], franja[2]))

                # Obtener los resultados de usos de consumo electrico  del formulario
                usos = []
                for i in range(1, 11):  # Máximo de 10 responsables
                    uso_nombre = request.form.get(f'uso_nombre_{i}')
                    uso_consumo = request.form.get(f'uso_consumo_{i}')

                    if uso_nombre and uso_consumo:  # Si se proporciona nombre y cargo
                        usos.append((uso_nombre, uso_consumo))

                for uso in usos:
                    cursor.execute('''
                                        INSERT INTO UsosConsumoElectrico (puerto_id, nombre_uso, valor_uso)
                                        VALUES (?, ?, ?)
                                    ''', (puerto_id, uso[0], uso[1]))

                # Obtener los resultados de diques  del formulario
                diques = []
                for i in range(1, 11):  # Máximo de 10 responsables
                    nombre_dique = request.form.get(f'dique_nombre_{i}')
                    amplitud = request.form.get(f'dique_amplitud_{i}')
                    periodo = request.form.get(f'dique_periodo_{i}')
                    velocidad = request.form.get(f'dique_velocidad_{i}')
                    longitud_onda = request.form.get(f'dique_longitud_{i}')
                    profundidad = request.form.get(f'dique_profundidad_{i}')
                    escullera = request.form.get(f'dique_escullera_{i}')

                    if nombre_dique and amplitud and periodo and velocidad and longitud_onda and profundidad and escullera:  # Si se proporciona nombre y cargo
                        diques.append((nombre_dique, amplitud, periodo, velocidad, longitud_onda, profundidad, escullera))

                for dique in diques:
                    cursor.execute('''
                        INSERT INTO Diques (puerto_id, nombre_dique, amplitud, periodo, velocidad, longitud_onda, profundidad, escullera)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (puerto_id, dique[0], dique[1], dique[2], dique[3], dique[4], dique[5], dique[6]))

                conn.commit()
                conn.close()

                return redirect(url_for('index'))

            except Error as e:
                print("Error al insertar datos:", e)
                conn.rollback()
                conn.close()
                return "Error al insertar datos en la base de datos"
        else:
            return render_template('create.html')
    return render_template('create.html')

@app.route('/consult_port', methods=['GET', 'POST'])
def consult_port():
    conn = sqlite3.connect('puertos.db')
    cursor = conn.cursor()

    # Consulta para obtener todos los puertos y solo los campos necesarios
    cursor.execute("SELECT puerto_id, nombre_pu, direccion, telefono, mail FROM Generales")
    puertos = cursor.fetchall()

    if request.method == 'POST':
        nombre = request.form['nombre']
        # Consulta para filtrar por nombre
        cursor.execute("SELECT puerto_id, nombre_pu, direccion, telefono, mail FROM Generales WHERE nombre_pu LIKE ?",
                       ('%' + nombre + '%',))
        puertos = cursor.fetchall()

    conn.close()
    return render_template('read.html', puertos=puertos)

@app.route('/modify_port/<puerto_id>', methods=['GET', 'POST'])
def modify_port(puerto_id):
    if request.method == 'POST':
        if request.form.get('confirmacion') == 'Aceptar':
            # Obtener datos del formulario
            nombre_pu = request.form['nombre_pu']
            direccion = request.form['direccion']
            telefono = request.form['telefono']
            mail = request.form['mail']
            num_trabajadores_total = request.form['num_trabajadores_total']
            num_trabajadores_hombres = request.form['num_trabajadores_hombres']
            num_trabajadores_mujeres = request.form['num_trabajadores_mujeres']
            volumen_ventas = request.form['volumen_ventas']
            colaboracion = request.form['colaboracion']
            plan_estrategico_enlace = request.form['plan_estrategico_enlace']
            plan_estrategico_descripcion = request.form['plan_estrategico_descripcion']
            plan_transicion_energetica_enlace = request.form['plan_transicion_energetica_enlace']
            plan_transicion_energetica_descripcion = request.form['plan_transicion_energetica_descripcion']
            plan_igualdad_enlace = request.form['plan_igualdad_enlace']
            plan_igualdad_descripcion = request.form['plan_igualdad_descripcion']
            # Insertar datos en la tabla 'Tecnicos'
            consumo_electrico_total = request.form['consumo_electrico_total']
            consumo_electrico_autoconsumo = request.form['consumo_electrico_autoconsumo']
            consumo_electrico_clientes = request.form['consumo_electrico_clientes']
            venta_energetica_red = request.form['venta_energetica_red']
            nivel_proteccion_ambiental = request.form['nivel_proteccion_ambiental']


            # Obtener los responsables del formulario
            responsables = []
            for i in range(1, 11):
                responsable_id = request.form.get(f'id_responsable_{i}')
                responsable_nombre = request.form.get(f'nombre_responsable_{i}')
                responsable_apellidos = request.form.get(f'apellidos_responsable_{i}')
                responsable_cargo = request.form.get(f'cargo_responsable_{i}')
                if responsable_nombre and responsable_cargo and responsable_apellidos:
                    responsables.append((responsable_id, responsable_nombre, responsable_apellidos, responsable_cargo))

            explotaciones = []
            for i in range(1, 11):
                explotacion_id = request.form.get(f'explotacion_id_{i}')
                anio_explotacion = request.form.get(f'anio_explotacion_{i}')
                valor_explotacion = request.form.get(f'valor_explotacion_{i}')
                if anio_explotacion and valor_explotacion:
                    explotaciones.append((explotacion_id, anio_explotacion, valor_explotacion))

            ejercicios = []
            for i in range(1, 11):  # Máximo de 10 responsables
                ejercicio_id = request.form.get(f'ejercicio_id_{i}')
                anio_ejercicio = request.form.get(f'anio_ejercicio_{i}')
                valor_ejercicio = request.form.get(f'valor_ejercicio_{i}')
                if anio_ejercicio and valor_ejercicio:  # Si se proporciona nombre y cargo
                    ejercicios.append((ejercicio_id, anio_ejercicio, valor_ejercicio))

            inversiones = []
            categorias = []
            for i in range(1, 11):  # Máximo de 10 responsables
                inversion_id = request.form.get(f'id_inversion_{i}')
                anio_inversion = request.form.get(f'anio_inversion_{i}')
                valor_inversion = request.form.get(f'valor_inversion_{i}')
                # Obtener los resultados de categorias de inversiones del formulario
                for j in range(1, 11):  # Máximo de 10 responsables
                    nombre_categoria = request.form.get(f'nombre_categoria_{j}')
                    valor_categoria = request.form.get(f'valor_categoria_{j}')
                    if nombre_categoria and valor_categoria:  # Si se proporciona nombre y cargo
                        categorias.append((nombre_categoria, valor_categoria))
                if anio_inversion and valor_inversion:  # Si se proporciona nombre y cargo
                    inversiones.append((inversion_id, anio_inversion, valor_inversion))

            zonas = []
            for i in range(1, 11):  # Máximo de 10 responsables
                zona_id = request.form.get(f'id_zona_{i}')
                zona_nombre = request.form.get(f'zona_nombre_{i}')
                zona_consumo = request.form.get(f'zona_consumo_{i}')
                if zona_nombre and zona_consumo:  # Si se proporciona nombre y cargo
                    zonas.append((zona_id,zona_nombre, zona_consumo))

            franjas = []
            for i in range(1, 11):  # Máximo de 10 responsables
                franja_id = request.form.get(f'franja_id_{i}')
                franja_inicio = request.form.get(f'franja_inicio_{i}')
                franja_fin = request.form.get(f'franja_fin_{i}')
                franja_consumo = request.form.get(f'franja_consumo_{i}')
                if franja_inicio and franja_fin and franja_consumo:  # Si se proporciona nombre y cargo
                    franjas.append((franja_id, franja_inicio, franja_fin, franja_consumo))

            usos = []
            for i in range(1, 11):  # Máximo de 10 responsables
                uso_id = request.form.get(f'uso_id_{i}')
                uso_nombre = request.form.get(f'uso_nombre_{i}')
                uso_consumo = request.form.get(f'uso_consumo_{i}')

                if uso_nombre and uso_consumo:  # Si se proporciona nombre y cargo
                    usos.append((uso_id, uso_nombre, uso_consumo))

            diques = []
            for i in range(1, 11):  # Máximo de 10 responsables
                dique_id = request.form.get(f'dique_id_{i}')
                nombre_dique = request.form.get(f'dique_nombre_{i}')
                amplitud = request.form.get(f'dique_amplitud_{i}')
                periodo = request.form.get(f'dique_periodo_{i}')
                velocidad = request.form.get(f'dique_velocidad_{i}')
                longitud_onda = request.form.get(f'dique_longitud_{i}')
                profundidad = request.form.get(f'dique_profundidad_{i}')
                escullera = request.form.get(f'dique_escullera_{i}')

                if nombre_dique and amplitud and periodo and velocidad and longitud_onda and profundidad and escullera:
                    diques.append((dique_id, nombre_dique, amplitud, periodo, velocidad, longitud_onda, profundidad, escullera))

            # Conexión a la base de datos
            conn = sqlite3.connect('puertos.db')
            cursor = conn.cursor()

            # Actualizar datos del puerto en la tabla
            cursor.execute('''
                UPDATE Generales
                SET nombre_pu=?, direccion=?, telefono=?, mail=?
                WHERE puerto_id=?
            ''', (nombre_pu, direccion, telefono, mail, puerto_id))

            # Insertar datos en la tabla 'Socioeconomicos'
            cursor.execute('''
                UPDATE Socioeconomicos 
                SET trab_total=?, trab_hombres=?, trab_mujeres=?, volumen_ventas=?, colaboracion=?, plan_estrategico_enlace=?, plan_estrategico_descripcion=?, plan_transicion_energetica_enlace=?, plan_transicion_energetica_descripcion=?, plan_igualdad_enlace=?, plan_igualdad_descripcion=?
                WHERE puerto_id=?
            ''', (
                num_trabajadores_total, num_trabajadores_hombres, num_trabajadores_mujeres, volumen_ventas,
                colaboracion, plan_estrategico_enlace, plan_estrategico_descripcion,
                plan_transicion_energetica_enlace, plan_transicion_energetica_descripcion, plan_igualdad_enlace,
                plan_igualdad_descripcion, puerto_id))

            cursor.execute('''
                    UPDATE Tecnicos 
                    SET consumo_electrico_total=?, autoconsumo=?, consumo_electrico_clientes=?, venta_energetica_red=?, nivel_proteccion_ambiental=?
                    WHERE puerto_id=?
                ''', (
                 consumo_electrico_total, consumo_electrico_autoconsumo, consumo_electrico_clientes,
                venta_energetica_red, nivel_proteccion_ambiental,puerto_id))

           # Insertar nuevos responsables en la tabla 'responsables' o actualizar los existentes si ya están presentes
            for responsable in responsables:
                # Verificar si el responsable ya existe en la base de datos

                cursor.execute('''
                    SELECT * FROM Responsables
                    WHERE responsable_id=?
                ''', (responsable[0],))
                existing_responsible = cursor.fetchone()

                if existing_responsible:
                    # Si el responsable ya existe, actualizar los datos correspondientes
                    cursor.execute('''
                        UPDATE Responsables
                        SET nombre_res = ?, apellidos = ?, cargo_res = ?
                        WHERE responsable_id = ?
                    ''', (responsable[1], responsable[2], responsable[3], responsable[0]))
                else:
                    # Si el responsable no existe, insertar un nuevo registro
                    cursor.execute('''
                        INSERT INTO Responsables (puerto_id, nombre_res, apellidos, cargo_res)
                        VALUES (?, ?, ?, ?)
                    ''', (puerto_id, responsable[1], responsable[2], responsable[3]))


            # Para las explotaciones
            for explotacion in explotaciones:
                cursor.execute('''
                    SELECT * FROM ResultadoExplotacion
                    WHERE resultado_id=?
                ''', (explotacion[0],))
                existing_explotacion = cursor.fetchone()

                if existing_explotacion:
                    cursor.execute('''
                        UPDATE ResultadoExplotacion
                        SET anio_ex = ?, valor_ex = ?
                        WHERE resultado_id = ?
                    ''', (explotacion[1], explotacion[2], existing_explotacion[0]))
                else:
                    cursor.execute('''
                        INSERT INTO ResultadoExplotacion (puerto_id, anio_ex, valor_ex)
                        VALUES (?, ?, ?)
                    ''', (puerto_id, explotacion[1], explotacion[2]))

            # Para los ejercicios
            for ejercicio in ejercicios:
                cursor.execute('''
                    SELECT * FROM ResultadoEjercicio
                    WHERE resultado_id = ?
                ''', (ejercicio[0],))
                existing_ejercicio = cursor.fetchone()

                if existing_ejercicio:
                    cursor.execute('''
                        UPDATE ResultadoEjercicio
                        SET anio_ej = ?, valor_ej=?
                        WHERE resultado_id = ?
                    ''', (ejercicio[1], ejercicio[2], existing_ejercicio[0]))
                else:
                    cursor.execute('''
                        INSERT INTO ResultadoEjercicio (puerto_id, anio_ej, valor_ej)
                        VALUES (?, ?, ?)
                    ''', (puerto_id, ejercicio[1], ejercicio[2]))

            # Para las inversiones
            for inversion in inversiones:
                cursor.execute('''
                    SELECT * FROM Inversiones
                    WHERE inversion_id =?
                ''', (inversion[0],))
                existing_inversion = cursor.fetchone()

                if existing_inversion:
                    cursor.execute('''
                        UPDATE Inversiones
                        SET anio_in =?, valor_in = ?
                        WHERE inversion_id = ?
                    ''', (inversion[1], inversion[2],existing_inversion[0]))
                    inversion_id_cat = existing_inversion[0]
                else:
                    cursor.execute('''
                        INSERT INTO Inversiones (puerto_id, anio_in, valor_in)
                        VALUES (?, ?, ?)
                    ''', (puerto_id, inversion[1], inversion[2]))
                    inversion_id_cat = cursor.lastrowid

                for categoria in categorias:
                    cursor.execute('''
                            INSERT OR REPLACE INTO CategoriasInversiones (inversion_id, puerto_id, nombre_cat, valor_cat)
                            VALUES (?, ?, ?, ?)
                        ''', (inversion_id_cat, puerto_id, categoria[0], categoria[1]))

            for zona in zonas:
                cursor.execute('''
                    SELECT * FROM ZonasConsumoElectrico
                    WHERE zona_id = ?
                ''', (zona[0],))
                existing_zona = cursor.fetchone()

                if existing_zona:
                    cursor.execute('''
                        UPDATE ZonasConsumoElectrico
                        SET nombre_zona = ?, valor_zona=?
                        WHERE zona_id = ?
                    ''', (zona[1], zona[2], existing_zona[0]))
                else:
                    cursor.execute('''
                        INSERT INTO ZonasConsumoElectrico (puerto_id, nombre_zona, valor_zona)
                        VALUES (?, ?, ?)
                    ''', (puerto_id, zona[1], zona[2]))

            for franja in franjas:
                cursor.execute('''
                                    SELECT * FROM FranjasHorariasConsumoElectrico
                                    WHERE franja_id = ?
                                ''', (franja[0],))
                existing_franja = cursor.fetchone()

                if existing_franja:
                    cursor.execute('''
                            UPDATE FranjasHorariasConsumoElectrico
                            SET franja_inicio = ?, franja_fin=?, valor_franja=?
                            WHERE franja_id = ?
                        ''', (franja[1], franja[2], franja[3],existing_franja[0]))
                else:
                    cursor.execute('''
                        INSERT INTO FranjasHorariasConsumoElectrico (puerto_id, franja_inicio, franja_fin, valor_franja)
                   VALUES (?, ?, ?, ?)
               ''', (puerto_id, franja[1], franja[2], franja[3]))

            for uso in usos:
                cursor.execute('''
                        SELECT * FROM UsosConsumoElectrico
                        WHERE uso_id = ?
                    ''', (uso[0],))
                existing_uso = cursor.fetchone()

                if existing_uso:
                    cursor.execute('''
                        UPDATE UsosConsumoElectrico
                        SET nombre_uso = ?, valor_uso=?
                        WHERE uso_id = ?
                    ''', (uso[1], uso[2], existing_uso[0]))
                else:
                    cursor.execute('''
                            INSERT INTO UsosConsumoElectrico (puerto_id, nombre_uso, valor_uso)
                            VALUES (?, ?, ?)
                       ''', (puerto_id, uso[1], uso[2]))

            for dique in diques:
                cursor.execute('''
                        SELECT * FROM Diques
                        WHERE dique_id = ?
                    ''', (dique[0],))
                existing_dique = cursor.fetchone()

                if existing_dique:
                    cursor.execute('''
                        UPDATE Diques
                        SET nombre_dique = ?, amplitud=?, periodo=?, velocidad=?, longitud_onda=?, profundidad=?, escullera=?
                        WHERE dique_id = ?
                    ''', (dique[1], dique[2],dique[3], dique[4], dique[5], dique[6], dique[7], existing_dique[0]))
                else:
                    cursor.execute('''
                        INSERT INTO Diques (puerto_id, nombre_dique, amplitud, periodo, velocidad, longitud_onda, profundidad, escullera)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (puerto_id, dique[1], dique[2], dique[3], dique[4], dique[5], dique[6], dique[7]))

            # Confirmar cambios y cerrar conexión
            conn.commit()
            conn.close()

            return redirect(url_for('index'))
    else:
        # Si el usuario hace clic en "Cancelar", volver a mostrar la página modify.html
        # Obtener los datos actuales del puerto
        conn = sqlite3.connect('puertos.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Generales WHERE puerto_id=?", (puerto_id,))
        generales = cursor.fetchone()
        cursor.execute("SELECT * FROM Responsables WHERE puerto_id=?", (puerto_id,))
        responsables = cursor.fetchall()
        cursor.execute("SELECT * FROM Socioeconomicos WHERE puerto_id=?", (puerto_id,))
        socioeconomicos = cursor.fetchone()
        cursor.execute("SELECT * FROM Tecnicos WHERE puerto_id=?", (puerto_id,))
        tecnicos = cursor.fetchone()
        cursor.execute("SELECT * FROM ResultadoExplotacion WHERE puerto_id=?", (puerto_id,))
        explotacion = cursor.fetchall()
        cursor.execute("SELECT * FROM ResultadoEjercicio WHERE puerto_id=?", (puerto_id,))
        ejercicios = cursor.fetchall()
        cursor.execute("SELECT * FROM Inversiones WHERE puerto_id=?", (puerto_id,))
        inversiones = cursor.fetchall()
        cursor.execute("SELECT * FROM CategoriasInversiones WHERE puerto_id=?", (puerto_id,))
        categorias = cursor.fetchall()
        cursor.execute("SELECT * FROM ZonasConsumoElectrico WHERE puerto_id=?", (puerto_id,))
        zonas = cursor.fetchall()
        cursor.execute("SELECT * FROM FranjasHorariasConsumoElectrico WHERE puerto_id=?", (puerto_id,))
        franjas = cursor.fetchall()
        cursor.execute("SELECT * FROM UsosConsumoElectrico WHERE puerto_id=?", (puerto_id,))
        usos = cursor.fetchall()
        cursor.execute("SELECT * FROM Diques WHERE puerto_id=?", (puerto_id,))
        diques = cursor.fetchall()
        conn.close()
        return render_template('modify.html', generales=generales, responsables=responsables,
                               socioeconomicos=socioeconomicos, tecnicos=tecnicos, explotacion=explotacion,
                               ejercicios=ejercicios, inversiones=inversiones, categorias=categorias,
                               zonas=zonas, franjas=franjas, usos=usos, diques=diques)

    # Obtener los datos actuales del puerto
    conn = sqlite3.connect('puertos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Generales WHERE puerto_id=?", (puerto_id,))
    generales = cursor.fetchone()
    cursor.execute("SELECT * FROM Responsables WHERE puerto_id=?", (puerto_id,))
    responsables = cursor.fetchall()
    cursor.execute("SELECT * FROM Socioeconomicos WHERE puerto_id=?", (puerto_id,))
    socioeconomicos = cursor.fetchone()
    cursor.execute("SELECT * FROM Tecnicos WHERE puerto_id=?", (puerto_id,))
    tecnicos = cursor.fetchone()
    cursor.execute("SELECT * FROM ResultadoExplotacion WHERE puerto_id=?", (puerto_id,))
    explotacion = cursor.fetchall()
    cursor.execute("SELECT * FROM ResultadoEjercicio WHERE puerto_id=?", (puerto_id,))
    ejercicios = cursor.fetchall()
    cursor.execute("SELECT * FROM Inversiones WHERE puerto_id=?", (puerto_id,))
    inversiones = cursor.fetchall()
    cursor.execute("SELECT * FROM CategoriasInversiones WHERE puerto_id=?", (puerto_id,))
    categorias = cursor.fetchall()
    cursor.execute("SELECT * FROM ZonasConsumoElectrico WHERE puerto_id=?", (puerto_id,))
    zonas = cursor.fetchall()
    cursor.execute("SELECT * FROM FranjasHorariasConsumoElectrico WHERE puerto_id=?", (puerto_id,))
    franjas = cursor.fetchall()
    cursor.execute("SELECT * FROM UsosConsumoElectrico WHERE puerto_id=?", (puerto_id,))
    usos = cursor.fetchall()
    cursor.execute("SELECT * FROM Diques WHERE puerto_id=?", (puerto_id,))
    diques = cursor.fetchall()
    conn.close()
    return render_template('modify.html', generales=generales, responsables=responsables,
                           socioeconomicos=socioeconomicos, tecnicos=tecnicos, explotacion=explotacion,
                           ejercicios=ejercicios, inversiones=inversiones, categorias=categorias,
                           zonas=zonas, franjas=franjas, usos=usos, diques=diques)

@app.route('/show_details')
def show_details():
    return "Página para consultar puerto"

@app.route('/delete_port', methods=['POST'])
def delete_port():
    # Obtener el puerto_id del formulario
    puerto_id = request.form['puerto_id']
    # Conexión a la base de datos
    conn = sqlite3.connect('puertos.db')
    cursor = conn.cursor()

    # Eliminar el puerto
    cursor.execute("DELETE FROM Generales WHERE puerto_id  = ?", (puerto_id,))
    cursor.execute("DELETE FROM Responsables WHERE puerto_id  = ?", (puerto_id,))
    cursor.execute("DELETE FROM Socioeconomicos WHERE puerto_id  = ?", (puerto_id,))
    cursor.execute("DELETE FROM ResultadoExplotacion WHERE puerto_id  = ?", (puerto_id,))
    cursor.execute("DELETE FROM ResultadoEjercicio WHERE puerto_id  = ?", (puerto_id,))
    cursor.execute("DELETE FROM Inversiones WHERE puerto_id  = ?", (puerto_id,))
    cursor.execute("DELETE FROM CategoriasInversiones WHERE puerto_id  = ?", (puerto_id,))
    cursor.execute("DELETE FROM Tecnicos WHERE puerto_id  = ?", (puerto_id,))
    cursor.execute("DELETE FROM ZonasConsumoElectrico WHERE puerto_id  = ?", (puerto_id,))
    cursor.execute("DELETE FROM FranjasHorariasConsumoElectrico WHERE puerto_id  = ?", (puerto_id,))
    cursor.execute("DELETE FROM UsosConsumoElectrico WHERE puerto_id  = ?", (puerto_id,))
    cursor.execute("DELETE FROM Diques WHERE puerto_id  = ?", (puerto_id,))


    # Confirmar cambios y cerrar conexión
    conn.commit()
    conn.close()

    return redirect(url_for('index'))  # Redireccionar a la página index.html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000,debug=False)
