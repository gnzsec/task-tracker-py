# Task Tracker CLI

## Descripción
Task Tracker es una aplicación de línea de comandos que permite a los usuarios gestionar sus tareas de manera eficiente. Puedes agregar, listar, actualizar y eliminar tareas fácilmente.

## Requisitos
- Python 3.x
- pip (gestor de paquetes de Python)

## Instalación

1. **Clonar el repositorio**
   Abre tu terminal y ejecuta el siguiente comando para clonar el proyecto:

   ```bash
   git clone https://github.com/tu_usuario/task-tracker.git
   ```

2. **Navegar al directorio del proyecto**
   ```bash
   cd task-tracker
   ```
3. **Ejecuta el archivo task-tracker.py**

   ```bash
   python task-tracker.py
   ```

## Uso

Para ejecutar la aplicación, utiliza el siguiente comando en la terminal:

```
### Comandos disponibles
- `add <descripcion>`: Agrega una nueva tarea.
- `list [estado]`: Lista todas las tareas, o solo las de un estado específico (por ejemplo, `done` o `in-progress`).
- `update <id_tarea> <nueva_descripcion>`: Actualiza la descripción de una tarea existente.
- `mark-done <id_tarea>`: Marca una tarea como completada.
- `mark-in-progress <id_tarea>`: Marca una tarea como en progreso.
- `delete <id_tarea>`: Elimina una tarea.
- `exit`: Salir de la aplicación.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
