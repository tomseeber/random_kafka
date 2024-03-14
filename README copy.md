# Oven Temperatures Lab Part 2 Solution

## Overview
There are four main components to the solution:
1. Kafka Zookeeper: `zookeeper/`
2. Kakfa Broker: `broker/`
3. Kafka Producer (Python): `kafka_producer/`
4. Kafka Consumer (Python): `kafka_consumer/`

In each respective directory is the associated `Dockerfile` used to build the docker image for each component.

## Steps
1. For each component, enter the directory and build the docker image. For example for the Kafka Zookeeper, you would:
```
$ cd zookeeper
$ docker build -t zookeeper:latest .
```
The following steps must be taken in each `Dockerfile`:
* Zookeeper: 
  * build from `confluentinc/cp-zookeeper:7.3.0`
  * set environment variables
  * Just as reference, this guide simply shows how to install locally without Docker: [getting started guide](https://developer.confluent.io/get-started/python/#kafka-setup) for guidance (with kafka location set to `Local`)
* Broker: use the [getting started guide](https://developer.confluent.io/get-started/python/#kafka-setup) for guidance (with kafka location set to `Local`)
  * build from `confluentinc/cp-kafka:7.3.0`
  * set environment variables
  * create a new topic called `oven`
* Kafka Producer
  * build from `confluentinc/cp-kafka`
  * copy a `requirements.txt` file containing the required python libraries
  * run `pip install` using the copied `requirements.txt` file
  * run `main.py` containing kafka producer
* Kafka Consumer
  * build from `confluentinc/cp-kafka`
  * copy a `requirements.txt` file containing the required python libraries
  * run `pip install` using the copied `requirements.txt` file
  * run `main.py` containing kafka producer

**NOTE: Apple M1 Machines**: If you are using an Apple M1 laptop, update the first line in `kafka_producer/Dockerfile` from `FROM confluentinc/cp-kafka:latest` to
`FROM confluentinc/cp-kafka:latest.amd64`
2. In the root directory where the `docker-compose.yaml` file is located, bring the containers up by running:
```
$ docker compose up
```
