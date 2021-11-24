# Ejemplo Streaming por Kafka

Implimentacion de un servicio de Streming con Kafka

## Armar un entorno virtual para Python

Altamente recomendado para no tener conflicto entre las librerias...y siempre hay conflicto entre las liberias de Python

```sh
python -m pip install virtualenv
virtualenv venv
source venv/bin/activate 
#si tienen windows es venv\Scripts\activate
```

## Instalando Librerias

Para esta API se utilizan:
- confluent-kafka: Confluent es la compañia formada por los devs de Kafka. Si bien es codigo abierto este sistema, ellos comercializan el ambiente cloud ya optimizado para este servicio. Este ejemplo se levanta un Kafka local 


```sh
python -m pip install confluent-kafka
```

## Descargando el servidor Kafka
```sh
#descargamos
wget https://dlcdn.apache.org/kafka/3.0.0/kafka_2.13-3.0.0.tgz
#descomprimimos
tar -xvzf kafka_2.13-3.0.0.tgz
#entramos al dir
cd kafka_2.13-3.0.0
```

## Para ejecutar el servicio

Una vez dentro del directorio, hay 2 servicios para levantar. El zookeeper y el Kafka.

```sh
bin/zookeeper-server-start.sh config/zookeeper.properties
```
y en otra terminal:

```sh
bin/kafka-server-start.sh config/server.properties
```

## Creamos el Canal(Topic) q va a ser consumido

```sh
bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
```
y verificamos q el *topic* este creado
```sh
bin/kafka-topics.sh --describe --topic quickstart-events --bootstrap-server localhost:9092
```

## Creacion de Productores y Consumidores

Los consumidores se abren con

```sh
python kafka_consumer.py
```

Se puede abrir tantos consumidores como se quiera. Luego ese canal se popula con mensajes provenientes de los productores:

```sh
python kafka_producer.py
```

