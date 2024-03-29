## Pruebas Software - Aseguramiento de Calidad E3

**Autor:** A01794327

**Número de Actividad:** A6.2

**Repositorio:** [https://github.com/JSOrtegaB/PruebasSoftwareAseguramientoCalidad_E3.git](https://github.com/JSOrtegaB/PruebasSoftwareAseguramientoCalidad_E3.git)

**Descripción:**

Este repositorio contiene el código fuente y las pruebas unitarias para un sistema de gestión de hoteles. El sistema permite:

- **Crear** y **modificar** hoteles.
- **Reservar** y **cancelar** habitaciones.
- **Obtener** información sobre un hotel específico.
- **Obtener** una lista de las habitaciones reservadas en un hotel.
- **Eliminar** un hotel.

**Pruebas Unitarias:**

El repositorio incluye pruebas unitarias para cada una de las funcionalidades del sistema. Las pruebas se basan en el marco de pruebas `unittest` de Python.

**Pruebas Negativas:**

1. test_read_file_not_found: Prueba que verifica que el sistema lanza una excepción si el archivo de hoteles no existe.
2. test_get_hotel: non_existing_id: Prueba que verifica que el sistema lanza una excepción si se intenta obtener un hotel que no existe.
3. test_delete_non_existing_hotel: Prueba que verifica que el sistema lanza una excepción si se intenta eliminar un hotel que no existe.
4. test_modify_non_existing_hotel: Prueba que verifica que el sistema lanza una excepción si se intenta modificar un hotel que no existe.
5. test_modify_nonexistent_customer: Prueba que verifica que el sistema lanza una excepción si se intenta modificar un cliente que no existe.

**Tecnologías:**

- Python 3
- Unittest

**Instrucciones de Ejecución:**

1. Clonar el repositorio:

```
git clone https://github.com/JSOrtegaB/PruebasSoftwareAseguramientoCalidad_E3.git
```

2. Instalar las dependencias:

```
pip install -r requirements.txt
```

3. Ejecutar las pruebas:

```
./pep8_flake8.sh
./coverage.sh
```

**Nota:**

Este repositorio es parte de la actividad A6.2 del curso de Pruebas Software y Aseguramiento de Calidad.
