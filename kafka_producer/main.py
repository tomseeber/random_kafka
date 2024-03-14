import requests
from confluent_kafka import Producer
import os
import json 


KAFKA_TOPIC = 'latest_events'
KAFKA_BOOTSTRAP_SERVERS = 'broker:9092'
base_url = "http://fact_api"

def delivery_callback(err, msg):
    if err:
        print('%% Message failed delivery: %s' % err)
    else:
        print('%% Message delivered to %s [%d]' % (msg.topic(), msg.partition()))

def main():
    # Kafka producer configuration
    conf = {'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS}

    # Create Kafka producer instance
    producer = Producer(conf)

    # Read the Wikimedia stream and produce messages to Kafka
    response = requests.get(f"{base_url}/fact").json()
    for adict in response:
        if adict:
            message = json.dumps(adict)
            # Produce message to Kafka
            producer.produce(KAFKA_TOPIC, message, callback=delivery_callback)

            # Flush messages to Kafka to ensure they are sent immediately
            producer.flush()

    # Close Kafka producer
    #producer.close()

if __name__ == '__main__':
    main()
