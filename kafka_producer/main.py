import requests
from confluent_kafka import Producer
import time
import json 

KAFKA_TOPIC = 'latest_events'
KAFKA_BOOTSTRAP_SERVERS = 'broker:9092'
REQUEST_URL2 = "http://fact_api/fact"
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

    while True:
        # Read the Wikimedia stream and produce messages to Kafka
        
        try:
            res_json = requests.get(REQUEST_URL2).json()
            res_json = json.dumps(res_json)
            message = res_json.encode('ascii')
            print(res_json, message)
            producer.produce(KAFKA_TOPIC, message, callback=delivery_callback)
            producer.flush()
            time.sleep(2)
        except Exception as e:
            print(e)
            print("test line 30\n")    
    producer.close()

if __name__ == '__main__':
    main()
