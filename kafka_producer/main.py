import requests
from confluent_kafka import Producer

KAFKA_TOPIC = 'latest_events'
KAFKA_BOOTSTRAP_SERVERS = 'broker:9092'
REQUEST_URL = "https://stream.wikimedia.org/v2/stream/recentchange"

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
    response = requests.get(REQUEST_URL, stream=True)
    for line in response.iter_lines():
        if line:
            # Produce message to Kafka
            producer.produce(KAFKA_TOPIC, line, callback=delivery_callback)

            # Flush messages to Kafka to ensure they are sent immediately
            producer.flush()

    # Close Kafka producer
    producer.close()

if __name__ == '__main__':
    main()
