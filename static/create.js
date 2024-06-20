function toggleLastDeleteButton(selector, displayStyle) {
    const elements = document.querySelectorAll(selector);
    if (elements.length > 0) {
        const lastElement = elements[elements.length - 1];
        const deleteButton = lastElement.querySelector("button");
        if (deleteButton) {
            deleteButton.style.display = displayStyle;
        }
    }
}

function hideLastDeleteButton(selector) {
    toggleLastDeleteButton(selector, "none");
}

function showLastDeleteButton(selector) {
    toggleLastDeleteButton(selector, "inline-block");
}

function createDeleteButton(container, selector) {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = "Eliminar";
    button.className = "delete-button";
    button.onclick = function () {
        container.remove();
        showLastDeleteButton(selector);
    };
    return button;
}

function createField(labelText, inputType, inputId, inputName, required = false, step = null) {
    const fragment = document.createDocumentFragment();

    const label = document.createElement("label");
    label.htmlFor = inputId;
    label.textContent = labelText;
    fragment.appendChild(label);

    const input = document.createElement("input");
    input.type = inputType;
    input.id = inputId;
    input.name = inputName;
    if (required) input.required = true;
    if (step) input.step = step;
    fragment.appendChild(input);

    return fragment;
}

function addElement(containerId, idPrefix, fields) {
    const container = document.getElementById(containerId);
    const numElements = document.querySelectorAll(`[id^="${idPrefix}_"]`).length + 1;
    hideLastDeleteButton(`[id^="${idPrefix}_"]`);

    const divElement = document.createElement("div");
    divElement.id = `${idPrefix}_${numElements}`;

    fields.forEach(field => {
        divElement.appendChild(createField(field.label, field.type, `${field.idPrefix}_${numElements}`, `${field.namePrefix}_${numElements}`, field.required, field.step));
    });

    divElement.appendChild(createDeleteButton(divElement, `[id^="${idPrefix}_"]`));
    container.appendChild(divElement);
}

function addResponsable() {
    addElement("responsables", "responsable", [
        { label: "Nombre", type: "text", idPrefix: "nombre_responsable", namePrefix: "nombre_responsable", required: true },
        { label: "Apellidos", type: "text", idPrefix: "apellidos_responsable", namePrefix: "apellidos_responsable", required: true },
        { label: "Cargo", type: "text", idPrefix: "cargo_responsable", namePrefix: "cargo_responsable", required: true }
    ]);
}

function addResultExplotacion() {
    addElement("resultados_explotacion", "resultado_explotacion", [
        { label: "Año", type: "number", idPrefix: "anio_explotacion", namePrefix: "anio_explotacion" },
        { label: "Valor", type: "number", idPrefix: "valor_explotacion", namePrefix: "valor_explotacion", step: "0.01" }
    ]);
}

function addResultEjercicio() {
    addElement("resultados_ejercicio", "resultado_ejercicio", [
        { label: "Año", type: "number", idPrefix: "anio_ejercicio", namePrefix: "anio_ejercicio" },
        { label: "Valor", type: "number", idPrefix: "valor_ejercicio", namePrefix: "valor_ejercicio", step: "0.01" }
    ]);
}

function addInversion() {
    const containerId = "inversiones";
    const idPrefix = "inversion";
    const numInversiones = document.querySelectorAll(`[id^="${idPrefix}_"]`).length + 1;
    hideLastDeleteButton(`[id^="${idPrefix}_"]`);

    const divInversion = document.createElement("div");
    divInversion.id = `${idPrefix}_${numInversiones}`;

    divInversion.appendChild(createField("Año", "number", `anio_inversion_${numInversiones}`, `anio_inversion_${numInversiones}`));
    divInversion.appendChild(createField("Valor", "number", `valor_inversion_${numInversiones}`, `valor_inversion_${numInversiones}`, false, "0.01"));

    const numCategoriasLabel = document.createElement("label");
    numCategoriasLabel.textContent = "Número de Categorías";
    divInversion.appendChild(numCategoriasLabel);

    const numCategoriasSelect = document.createElement("select");
    numCategoriasSelect.id = `num_categorias_${numInversiones}`;
    numCategoriasSelect.name = `num_categorias_${numInversiones}`;
    numCategoriasSelect.innerHTML = `
        <option value="0"></option>
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
        <option value="6">6</option>
        <option value="7">7</option>`;
    numCategoriasSelect.onchange = () => crearCamposCategoria(numInversiones);
    divInversion.appendChild(numCategoriasSelect);

    divInversion.appendChild(createDeleteButton(divInversion, `[id^="${idPrefix}_"]`));

    const camposCategoriasDiv = document.createElement("div");
    camposCategoriasDiv.id = `campos_categorias_${numInversiones}`;
    divInversion.appendChild(camposCategoriasDiv);

    document.getElementById(containerId).appendChild(divInversion);
}

function crearCamposCategoria(numInversion) {
    const numCategorias = parseInt(document.getElementById(`num_categorias_${numInversion}`).value);
    const camposCategoriasDiv = document.getElementById(`campos_categorias_${numInversion}`);
    camposCategoriasDiv.innerHTML = "";

    for (let i = 1; i <= numCategorias; i++) {
        const divCategoria = document.createElement("div");
        divCategoria.appendChild(createField(`Nombre de Categoría ${i}`, "text", `nombre_categoria_${numInversion}_${i}`, `nombre_categoria_${numInversion}_${i}`));
        divCategoria.appendChild(createField(`Valor de Categoría ${i}`, "number", `valor_categoria_${numInversion}_${i}`, `valor_categoria_${numInversion}_${i}`, false, "0.01"));
        camposCategoriasDiv.appendChild(divCategoria);
    }
}

function crearCampos(elementId, prefix, fields) {
    const numElements = parseInt(document.getElementById(elementId).value);
    const container = document.getElementById(`${prefix}_campos`);
    container.innerHTML = "";

    for (let i = 1; i <= numElements; i++) {
        const divElement = document.createElement("div");
        fields.forEach(field => {
            divElement.appendChild(createField(field.label.replace("{i}", i), field.type, `${field.idPrefix}_${i}`, `${field.namePrefix}_${i}`, field.required, field.step));
        });
        container.appendChild(divElement);
    }
}

function crearCamposZonas() {
    crearCampos("num_zonas", "zonas", [
        { label: "Zona {i}", type: "text", idPrefix: "zona_nombre", namePrefix: "zona_nombre" },
        { label: "Consumo en esta zona", type: "number", idPrefix: "zona_consumo", namePrefix: "zona_consumo", step: "0.01" }
    ]);
}

function crearCamposFranjas() {
    crearCampos("num_franjas", "franjas", [
        { label: "Franja Horaria {i}", type: "time", idPrefix: "franja_inicio", namePrefix: "franja_inicio" },
        { label: "", type: "time", idPrefix: "franja_fin", namePrefix: "franja_fin" },
        { label: "Consumo eléctrico", type: "number", idPrefix: "franja_consumo", namePrefix: "franja_consumo", step: "0.01" }
    ]);
}

function crearCamposUsos() {
    crearCampos("num_usos", "usos", [
        { label: "Uso {i}", type: "text", idPrefix: "uso_nombre", namePrefix: "uso_nombre" },
        { label: "Consumo eléctrico", type: "number", idPrefix: "uso_consumo", namePrefix: "uso_consumo", step: "0.01" }
    ]);
}

function crearCamposDiques() {
    const numDiques = parseInt(document.getElementById("num_diques").value);
    const diquesCamposDiv = document.getElementById("diques_campos");
    diquesCamposDiv.innerHTML = ""; // Limpiar div antes de agregar campos nuevos

    for (let i = 1; i <= numDiques; i++) {
        const fieldsetDique = document.createElement("fieldset"); // Nuevo fieldset para cada dique

        const legendDique = document.createElement("legend"); // Nuevo legend para el fieldset
        legendDique.textContent = "Dique " + i;
        fieldsetDique.appendChild(legendDique);

        // Lista de campos a agregar
        const fields = [
            { label: "Nombre ", type: "text", id: `dique_nombre_${i}`, name: `dique_nombre_${i}` },
            { label: "Amplitud ", type: "number", step: "0.01", id: `dique_amplitud_${i}`, name: `dique_amplitud_${i}` },
            { label: "Periodo ", type: "number", step: "0.01", id: `dique_periodo_${i}`, name: `dique_periodo_${i}` },
            { label: "Velocidad ", type: "number", step: "0.01", id: `dique_velocidad_${i}`, name: `dique_velocidad_${i}` },
            { label: "Longitud de Onda ", type: "number", step: "0.01", id: `dique_longitud_${i}`, name: `dique_longitud_${i}` },
            { label: "Profundidad ", type: "number", step: "0.01", id: `dique_profundidad_${i}`, name: `dique_profundidad_${i}` },
        ];

        // Agregar campos al fieldset
        fields.forEach((field, index) => {
            const label = document.createElement("label");
            label.textContent = field.label;
            fieldsetDique.appendChild(label);

            const input = document.createElement("input");
            input.type = field.type;
            if (field.step) input.step = field.step;
            input.id = field.id;
            input.name = field.name;
            fieldsetDique.appendChild(input);

            // Añadir salto de línea después de cada tercer campo
            if ((index + 1) % 3 === 0 && index < fields.length - 1) {
                fieldsetDique.appendChild(document.createElement("br"));
            }
        });

        // Campo select para escullera
        const esculleraLabel = document.createElement("label");
        esculleraLabel.textContent = "¿Hay Escullera? ";
        fieldsetDique.appendChild(esculleraLabel);

        const esculleraSelect = document.createElement("select");
        esculleraSelect.id = `dique_escullera_${i}`;
        esculleraSelect.name = `dique_escullera_${i}`;
        const optionVacio = document.createElement("option");
        optionVacio.value = "";
        optionVacio.textContent = "";
        const optionSi = document.createElement("option");
        optionSi.value = "1";
        optionSi.textContent = "Sí";
        const optionNo = document.createElement("option");
        optionNo.value = "0";
        optionNo.textContent = "No";
        esculleraSelect.appendChild(optionVacio);
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
    function validarTelefono(input) {
        // Reemplazar todos los caracteres que no sean números, signos más, o espacios
        input.value = input.value.replace(/[^0-9+ ]/g, '');
    }

    function validarFormulario() {
        var hombres = parseInt(document.getElementById("num_trabajadores_hombres").value);
        var mujeres = parseInt(document.getElementById("num_trabajadores_mujeres").value);
        var total = parseInt(document.getElementById("num_trabajadores_total").value);

        if ((hombres + mujeres) > total) {
            alert("La suma de hombres y mujeres no puede ser mayor que el total.");
            return false; // Evita el envío del formulario
        }

        var venta = parseInt(document.getElementById("venta_energetica_red").value);
        var clientes = parseInt(document.getElementById("consumo_electrico_clientes").value);
        var autoconsumo = parseInt(document.getElementById("consumo_electrico_autoconsumo").value);
        var consumo = parseInt(document.getElementById("consumo_electrico_total").value);

        if (autoconsumo) {
            sumaEnergia += parseInt(autoconsumo);
        }
        if (venta) {
            sumaEnergia += parseInt(venta);
        }
        if (clientes) {
            sumaEnergia += parseInt(clientes);
        }

        if (sumaEnergia > totalEnergia) {
            alert("La suma de autoconsumo, venta y clientes no puede ser mayor que el total de energía.");
            return false; // Evita el envío del formulario
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
