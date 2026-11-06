# <img src="https://media.tenor.com/GvP5WfH4AKgAAAAj/bee-minecraft.gif" width="40" style="vertical-align: middle;" alt="Abeja"> Ejercicio 1: Ejecución Secuencial - Recolección de Néctar



## Descripción
Este proyecto demuestra el funcionamiento de la **ejecución secuencial** en Python mediante la simulación de un panal de abejas. 

Una única abeja obrera (`Abeja Obrera #1`) debe recolectar néctar de tres flores distintas (Rosa, Girasol y Tulipán). Al ser un proceso secuencial, cada tarea debe finalizar por completo antes de iniciar la siguiente, sumando un tiempo total de **6.00 segundos**.

## Requisitos
- Docker y Docker Compose instalados.

## Ejecución con Docker Compose

1. Clonar el repositorio y acceder al directorio:
   ```bash
   git clone https://github.com/talos0412/panal-ejercicio1-secuencial.git
   cd ejercicio1-secuencial
   ```

2. Iniciar el contenedor:
   ```
   docker compose up
   ```

3. Detener y eliminar el contenedor al finalizar:
   ```
   docker compose down
   ```

## Salida esperada en el contenedor:

```
Iniciando la recolección en solitario de néctar...
Abeja Obrera #1 está recolectando néctar de la Rosa.
Abeja Obrera #1 ha terminado de recolectar néctar de la Rosa.
Abeja Obrera #1 está recolectando néctar de la Girasol.
Abeja Obrera #1 ha terminado de recolectar néctar de la Girasol.
Abeja Obrera #1 está recolectando néctar de la Tulipán.
Abeja Obrera #1 ha terminado de recolectar néctar de la Tulipán.
Tiempo total de recolección: 6.00 segundos.
```
