# rabbitmq-hello-world

Trabajo Práctico de la materia Programación Distribuida II de la Universidad Nacional de Avellaneda

Este ejemplo básico de RabbitMQ cuenta con tres contenedores:

* Un servidor RabbitMQ
* Un publisher
* Un consumer

Tanto el publisher como el consumer estan hechos en Python y su código es una versión levemente modificada del disponible en la página web de RabbitMQ.

## Requisitos

Para usar la aplicación es necesario contar con Docker y Docker Compose instalado.

## Modo de uso

Para levantar los contenedores corremos el siguiente comando en el directorio raiz del respositorio:

```
docker-compose up
```

Hecho esto, luego de que los contenedores hayan podido conectarse deberíamos encontrarnos con que cada 5 segundos el publisher envía un "Hello World" a la cola, que es oportunamente desencolado por el consumer.
