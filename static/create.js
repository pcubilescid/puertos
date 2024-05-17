function agregarResponsable() {
        var numResponsables = document.querySelectorAll('[id^="responsable_"]').length + 1;

        var divResponsable = document.createElement("div");
        divResponsable.id = "responsable_" + numResponsables;

        var nombreLabel = document.createElement("label");
        nombreLabel.htmlFor = "responsable_nombre_" + numResponsables;
        nombreLabel.textContent = "Nombre";
        divResponsable.appendChild(nombreLabel);

        var nombreInput = document.createElement("input");
        nombreInput.type = "text";
        nombreInput.id = "nombre_responsable_" + numResponsables;
        nombreInput.name = "nombre_responsable_" + numResponsables;
        nombreInput.required = true;
        divResponsable.appendChild(nombreInput);

        var apellidosLabel = document.createElement("label");
        apellidosLabel.htmlFor = "responsable_apellidos_" + numResponsables;
        apellidosLabel.textContent = "Apellidos";
        divResponsable.appendChild(apellidosLabel);

        var apellidosInput = document.createElement("input");
        apellidosInput.type = "text";
        apellidosInput.id = "apellidos_responsable_" + numResponsables;
        apellidosInput.name = "apellidos_responsable_" + numResponsables;
        apellidosInput.required = true;
        divResponsable.appendChild(apellidosInput);

        var cargoLabel = document.createElement("label");
        cargoLabel.htmlFor = "cargo_responsable_" + numResponsables;
        cargoLabel.textContent = "Cargo";
        divResponsable.appendChild(cargoLabel);

        var cargoInput = document.createElement("input");
        cargoInput.type = "text";
        cargoInput.id = "cargo_responsable_" + numResponsables;
        cargoInput.name = "cargo_responsable_" + numResponsables;
        cargoInput.required = true;
        divResponsable.appendChild(cargoInput);

        var buttonEliminar = document.createElement("button");
        buttonEliminar.type = "button";
        buttonEliminar.textContent = "Eliminar";
        buttonEliminar.style.backgroundColor = "#ff0000";
        buttonEliminar.style.color = "#fff";
        buttonEliminar.style.marginLeft = "10px";
        buttonEliminar.onclick = function() {
            divResponsable.remove(); // Eliminar el div del responsable
        };
        divResponsable.appendChild(buttonEliminar);

        var responsablesDiv = document.getElementById("responsables");
        responsablesDiv.appendChild(divResponsable);
    }

    function agregarResultadoExplotacion() {
        var numResultadosExplotacion = document.querySelectorAll('[id^="resultado_explotacion_"]').length + 1;

        var divResultadoExplotacion = document.createElement("div");
        divResultadoExplotacion.id = "resultado_explotacion_" + numResultadosExplotacion;

        var anioLabel = document.createElement("label");
        anioLabel.htmlFor = "anio_explotacion_" + numResultadosExplotacion;
        anioLabel.textContent = "Año";
        divResultadoExplotacion.appendChild(anioLabel);

        var anioInput = document.createElement("input");
        anioInput.type = "number";
        anioInput.id = "anio_explotacion_" + numResultadosExplotacion;
        anioInput.name = "anio_explotacion_" + numResultadosExplotacion;
        divResultadoExplotacion.appendChild(anioInput);

        var valorLabel = document.createElement("label");
        valorLabel.htmlFor = "valor_explotacion_" + numResultadosExplotacion;
        valorLabel.textContent = "Valor";
        divResultadoExplotacion.appendChild(valorLabel);

        var valorInput = document.createElement("input");
        valorInput.type = "number";
        valorInput.id = "valor_explotacion_" + numResultadosExplotacion;
        valorInput.name = "valor_explotacion_" + numResultadosExplotacion;
        valorInput.step = "0.01";
        divResultadoExplotacion.appendChild(valorInput);

        var buttonEliminar = document.createElement("button");
        buttonEliminar.type = "button";
        buttonEliminar.textContent = "Eliminar";
        buttonEliminar.style.backgroundColor = "#ff0000";
        buttonEliminar.style.color = "#fff";
        buttonEliminar.style.marginLeft = "10px";
        buttonEliminar.onclick = function() {
            divResultadoExplotacion.remove();
        };
        divResultadoExplotacion.appendChild(buttonEliminar);

        var resultadosExplotacionDiv = document.getElementById("resultados_explotacion");
        resultadosExplotacionDiv.appendChild(divResultadoExplotacion);
    }

    function agregarResultadoEjercicio() {
        var numResultadosEjercicio = document.querySelectorAll('[id^="resultado_ejercicio_"]').length + 1;

        var divResultadoEjercicio = document.createElement("div");
        divResultadoEjercicio.id = "resultado_ejercicio_" + numResultadosEjercicio;

        var anioLabel = document.createElement("label");
        anioLabel.htmlFor = "anio_ejercicio_" + numResultadosEjercicio;
        anioLabel.textContent = "Año";
        divResultadoEjercicio.appendChild(anioLabel);

        var anioInput = document.createElement("input");
        anioInput.type = "number";
        anioInput.id = "anio_ejercicio_" + numResultadosEjercicio;
        anioInput.name = "anio_ejercicio_" + numResultadosEjercicio;
        divResultadoEjercicio.appendChild(anioInput);

        var valorLabel = document.createElement("label");
        valorLabel.htmlFor = "valor_ejercicio_" + numResultadosEjercicio;
        valorLabel.textContent = "Valor";
        divResultadoEjercicio.appendChild(valorLabel);

        var valorInput = document.createElement("input");
        valorInput.type = "number";
        valorInput.id = "valor_ejercicio_" + numResultadosEjercicio;
        valorInput.name = "valor_ejercicio_" + numResultadosEjercicio;
        valorInput.step = "0.01";
        divResultadoEjercicio.appendChild(valorInput);

        var buttonEliminar = document.createElement("button");
        buttonEliminar.type = "button";
        buttonEliminar.textContent = "Eliminar";
        buttonEliminar.style.backgroundColor = "#ff0000";
        buttonEliminar.style.color = "#fff";
        buttonEliminar.style.marginLeft = "10px";
        buttonEliminar.onclick = function() {
            divResultadoEjercicio.remove();
        };
        divResultadoEjercicio.appendChild(buttonEliminar);

        var resultadosEjercicioDiv = document.getElementById("resultados_ejercicio");
        resultadosEjercicioDiv.appendChild(divResultadoEjercicio);
    }

    function agregarInversion() {
        var numInversiones = document.querySelectorAll('[id^="inversion_"]').length + 1;
        var divInversion = document.createElement("div");
        divInversion.id = "inversion_" + numInversiones;

        var anioLabel = document.createElement("label");
        anioLabel.htmlFor = "anio_inversion_" + numInversiones;
        anioLabel.textContent = "Año";
        divInversion.appendChild(anioLabel);

        var anioInput = document.createElement("input");
        anioInput.type = "number";
        anioInput.id = "anio_inversion_" + numInversiones;
        anioInput.name = "anio_inversion_" + numInversiones;
        divInversion.appendChild(anioInput);

        var valorLabel = document.createElement("label");
        valorLabel.htmlFor = "valor_inversion_" + numInversiones;
        valorLabel.textContent = "Valor";
        divInversion.appendChild(valorLabel);

        var valorInput = document.createElement("input");
        valorInput.type = "number";
        valorInput.id = "valor_inversion_" + numInversiones;
        valorInput.name = "valor_inversion_" + numInversiones;
        valorInput.step = "0.01";
        divInversion.appendChild(valorInput);

        var numCategoriasLabel = document.createElement("label");
        numCategoriasLabel.textContent = "Número de Categorías";
        divInversion.appendChild(numCategoriasLabel);

        var numCategoriasSelect = document.createElement("select");
        numCategoriasSelect.id = "num_categorias_" + numInversiones;
        numCategoriasSelect.name = "num_categorias_" + numInversiones;
        numCategoriasSelect.innerHTML = `
            <option value="0"></option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
            <option value="6">6</option>
            <option value="7">7</option>`;


        numCategoriasSelect.onchange = function() {
            crearCamposCategoria(numInversiones);
        };
        divInversion.appendChild(numCategoriasSelect);

        var buttonEliminar = document.createElement("button");
        buttonEliminar.type = "button";
        buttonEliminar.textContent = "Eliminar";
        buttonEliminar.style.backgroundColor = "#ff0000";
        buttonEliminar.style.color = "#fff";
        buttonEliminar.style.marginLeft = "10px";
        buttonEliminar.onclick = function() {
            divInversion.remove();
        };

        divInversion.appendChild(buttonEliminar);

        var camposCategoriasDiv = document.createElement("div");
        camposCategoriasDiv.id = "campos_categorias_" + numInversiones;
        divInversion.appendChild(camposCategoriasDiv);

        var inversionesDiv = document.getElementById("inversiones");
        inversionesDiv.appendChild(divInversion);
    }

    function crearCamposCategoria(numInversion) {
        var numCategorias = parseInt(document.getElementById("num_categorias_" + numInversion).value);
        var camposCategoriasDiv = document.getElementById("campos_categorias_" + numInversion);
        camposCategoriasDiv.innerHTML = ""; // Limpiar div antes de agregar campos nuevos

        for (var i = 1; i <= numCategorias; i++) {
            var divCategoria = document.createElement("div");

            var nombreLabel = document.createElement("label");
            nombreLabel.textContent = "Nombre de Categoría " + i;
            divCategoria.appendChild(nombreLabel);

            var nombreInput = document.createElement("input");
            nombreInput.type = "text";
            nombreInput.id = "nombre_categoria_" + numInversion + "_" + i;
            nombreInput.name = "nombre_categoria_" + numInversion + "_" + i;
            divCategoria.appendChild(nombreInput);

            var valorLabel = document.createElement("label");
            valorLabel.textContent = "Valor de Categoría " + i;
            divCategoria.appendChild(valorLabel);

            var valorInput = document.createElement("input");
            valorInput.type = "number";
            valorInput.step = "0.01";
            valorInput.id = "valor_categoria_" + numInversion + "_" + i;
            valorInput.name = "valor_categoria_" + numInversion + "_" + i;
            divCategoria.appendChild(valorInput);

            camposCategoriasDiv.appendChild(divCategoria);
        }
    }

    function crearCamposZonas() {
        var numZonas = parseInt(document.getElementById("num_zonas").value);
        var zonasCamposDiv = document.getElementById("zonas_campos");
        zonasCamposDiv.innerHTML = ""; // Limpiar div antes de agregar campos nuevos

        for (var i = 1; i <= numZonas; i++) {
            var divZona = document.createElement("div");

            var nombreLabel = document.createElement("label");
            nombreLabel.textContent = "Zona " + i + "";
            divZona.appendChild(nombreLabel);

            var nombreInput = document.createElement("input");
            nombreInput.type = "text";
            nombreInput.id = "zona_nombre_" + i;
            nombreInput.name = "zona_nombre_" + i;
            divZona.appendChild(nombreInput);

            var consumoLabel = document.createElement("label");
            consumoLabel.textContent = "Consumo en esta zona";
            divZona.appendChild(consumoLabel);

            var consumoInput = document.createElement("input");
            consumoInput.type = "number";
            consumoInput.step = "0.01";
            consumoInput.id = "zona_consumo_" + i;
            consumoInput.name = "zona_consumo_" + i;
            divZona.appendChild(consumoInput);

            zonasCamposDiv.appendChild(divZona);
        }
    }

    function crearCamposFranjas() {
        var numFranjas = parseInt(document.getElementById("num_franjas").value);
        var franjasCamposDiv = document.getElementById("franjas_campos");
        franjasCamposDiv.innerHTML = ""; // Limpiar div antes de agregar campos nuevos

        for (var i = 1; i <= numFranjas; i++) {
            var divFranja = document.createElement("div");

            var nombreLabel = document.createElement("label");
            nombreLabel.textContent = "Franja Horaria " + i + ":";
            divFranja.appendChild(nombreLabel);

            var inicioInput = document.createElement("input");
            inicioInput.type = "time";
            inicioInput.id = "franja_inicio_" + i;
            inicioInput.name = "franja_inicio_" + i;
            divFranja.appendChild(inicioInput);

            var finInput = document.createElement("input");
            finInput.type = "time";
            finInput.id = "franja_fin_" + i;
            finInput.name = "franja_fin_" + i;
            divFranja.appendChild(finInput);

            var consumoLabel = document.createElement("label");
            consumoLabel.textContent = "Consumo eléctrico ";
            divFranja.appendChild(consumoLabel);

            var consumoInput = document.createElement("input");
            consumoInput.type = "number";
            consumoInput.step = "0.01";
            consumoInput.id = "franja_consumo_" + i;
            consumoInput.name = "franja_consumo_" + i;
            divFranja.appendChild(consumoInput);

            franjasCamposDiv.appendChild(divFranja);
        }
    }

    function crearCamposUsos() {
        var numUsos = parseInt(document.getElementById("num_usos").value);
        var usosCamposDiv = document.getElementById("usos_campos");
        usosCamposDiv.innerHTML = ""; // Limpiar div antes de agregar campos nuevos

        for (var i = 1; i <= numUsos; i++) {
            var divUso = document.createElement("div");

            var nombreLabel = document.createElement("label");
            nombreLabel.textContent = "Uso " + i;
            divUso.appendChild(nombreLabel);

            var usoInput = document.createElement("input");
            usoInput.type = "text";
            usoInput.id = "uso_nombre_" + i;
            usoInput.name = "uso_nombre_" + i;
            divUso.appendChild(usoInput);

            var consumoLabel = document.createElement("label");
            consumoLabel.textContent = "Consumo eléctrico";
            divUso.appendChild(consumoLabel);

            var consumoInput = document.createElement("input");
            consumoInput.type = "number";
            consumoInput.step = "0.01";
            consumoInput.id = "uso_consumo_" + i;
            consumoInput.name = "uso_consumo_" + i;
            divUso.appendChild(consumoInput);

            usosCamposDiv.appendChild(divUso);
        }
    }

    function crearCamposDiques() {
        var numDiques = parseInt(document.getElementById("num_diques").value);
        var diquesCamposDiv = document.getElementById("diques_campos");
        diquesCamposDiv.innerHTML = ""; // Limpiar div antes de agregar campos nuevos

        for (var i = 1; i <= numDiques; i++) {
            var fieldsetDique = document.createElement("fieldset"); // Nuevo fieldset para cada dique

            var legendDique = document.createElement("legend"); // Nuevo legend para el fieldset
            legendDique.textContent = "Dique " + i;
            fieldsetDique.appendChild(legendDique);

            var nombreLabel = document.createElement("label");
            nombreLabel.textContent = "Nombre ";
            fieldsetDique.appendChild(nombreLabel);

            var nombreInput = document.createElement("input");
            nombreInput.type = "text";
            nombreInput.id = "dique_nombre_" + i;
            nombreInput.name = "dique_nombre_" + i;
            fieldsetDique.appendChild(nombreInput);

            var amplitudLabel = document.createElement("label");
            amplitudLabel.textContent = "Amplitud ";
            fieldsetDique.appendChild(amplitudLabel);

            var amplitudInput = document.createElement("input");
            amplitudInput.type = "number";
            amplitudInput.step = "0.01";
            amplitudInput.id = "dique_amplitud_" + i;
            amplitudInput.name = "dique_amplitud_" + i;
            fieldsetDique.appendChild(amplitudInput);

            var periodoLabel = document.createElement("label");
            periodoLabel.textContent = "Periodo ";
            fieldsetDique.appendChild(periodoLabel);

            var periodoInput = document.createElement("input");
            periodoInput.type = "number";
            periodoInput.step = "0.01";
            periodoInput.id = "dique_periodo_" + i;
            periodoInput.name = "dique_periodo_" + i;
            fieldsetDique.appendChild(periodoInput);

            var lineBreak = document.createElement("br");
            fieldsetDique.appendChild(lineBreak);

            var velocidadLabel = document.createElement("label");
            velocidadLabel.textContent = "Velocidad ";
            fieldsetDique.appendChild(velocidadLabel);

            var velocidadInput = document.createElement("input");
            velocidadInput.type = "number";
            velocidadInput.step = "0.01";
            velocidadInput.id = "dique_velocidad_" + i;
            velocidadInput.name = "dique_velocidad_" + i;
            fieldsetDique.appendChild(velocidadInput);

            var longitudLabel = document.createElement("label");
            longitudLabel.textContent = "Longitud de Onda ";
            fieldsetDique.appendChild(longitudLabel);

            var longitudInput = document.createElement("input");
            longitudInput.type = "number";
            longitudInput.step = "0.01";
            longitudInput.id = "dique_longitud_" + i;
            longitudInput.name = "dique_longitud_" + i;
            fieldsetDique.appendChild(longitudInput);

            var profundidadLabel = document.createElement("label");
            profundidadLabel.textContent = "Profundidad ";
            fieldsetDique.appendChild(profundidadLabel);

            var profundidadInput = document.createElement("input");
            profundidadInput.type = "number";
            profundidadInput.step = "0.01";
            profundidadInput.id = "dique_profundidad_" + i;
            profundidadInput.name = "dique_profundidad_" + i;
            fieldsetDique.appendChild(profundidadInput);

            var lineBreak = document.createElement("br");
            fieldsetDique.appendChild(lineBreak);

            var esculleraLabel = document.createElement("label");
            esculleraLabel.textContent = "¿Hay Escullera? ";
            fieldsetDique.appendChild(esculleraLabel);

            var esculleraSelect = document.createElement("select");
            esculleraSelect.id = "dique_escullera_" + i;
            esculleraSelect.name = "dique_escullera_" + i;
            var optionSi = document.createElement("option");
            optionSi.value = "1";
            optionSi.textContent = "Sí";
            var optionNo = document.createElement("option");
            optionNo.value = "0";
            optionNo.textContent = "No";
            esculleraSelect.appendChild(optionSi);
            esculleraSelect.appendChild(optionNo);
            fieldsetDique.appendChild(esculleraSelect);

            diquesCamposDiv.appendChild(fieldsetDique);
        }
    }

    function validarCorreo() {
        var email = document.getElementById("email").value;
        var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }

    function validarFormulario() {
        var telefono = document.getElementById("telefono").value;
        if (isNaN(telefono)) {
            document.getElementById("telefono_error").style.display = "inline";
            return false;
        } else {
            document.getElementById("telefono_error").style.display = "none";
        }

        if (!validarCorreo()) {
            alert("Por favor, introduce un correo electrónico válido.");
            return false;
        }
        return true;
    }

    function confirmarAñadir() {
        if (confirm("¿Estás seguro de que deseas añadir este puerto?")) {
            // Si el usuario hace clic en "Aceptar"
            // Agregar un campo oculto al formulario para enviar la confirmación al servidor
            var confirmationInput = document.createElement("input");
            confirmationInput.type = "hidden";
            confirmationInput.name = "confirmacion";
            confirmationInput.value = "Aceptar";
            document.getElementById("addPortForm").appendChild(confirmationInput);

        } else {
            // Si el usuario hace clic en "Cancelar", no se hace nada
            return false;
        }
    }

    function confirmarModificar() {
        if (confirm("¿Estás seguro de que deseas modificar este puerto?")) {
            // Si el usuario hace clic en "Aceptar"
            // Agregar un campo oculto al formulario para enviar la confirmación al servidor
            var confirmationInput = document.createElement("input");
            confirmationInput.type = "hidden";
            confirmationInput.name = "confirmacion";
            confirmationInput.value = "Aceptar";
            document.getElementById("modifyPortForm").appendChild(confirmationInput);

        } else {
            // Si el usuario hace clic en "Cancelar", no se hace nada
            return false;
        }
    }
