"""
create topic:

~/kafka/bin/kafka-topics.sh
--create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic DataVisualizationG3

"""
import random
import csv
import random
import time

from kafka import KafkaProducer
from datetime import datetime



KAFKA_TOPIC_NAME = "DataVisualizationG3"
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"

location_choices = ["windsor", "london", "toronto", "montreal", "kitchener", "sarnia"]
status_choices = ["DELIEVERED", "CANCELLED", "UNDELIEVERED"]


if __name__ == "__main__":
    print("Kakfa Producer Application Started....")
    kafka_producer_obj =  KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    while True:
        message = f"{random.randrange(1,11)},{random.choice(location_choices)},{random.choice(status_choices)}"
        print("Sending message to Kafka..")
        kafka_producer_obj.send(KAFKA_TOPIC_NAME, message.encode('utf-8'))
        print("Message sent successfully!")
        time.sleep(2)
