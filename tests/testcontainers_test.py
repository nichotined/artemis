from testcontainers.kafka import KafkaContainer
from confluent_kafka import Producer, Consumer, KafkaException
import time
import requests


# Function to simulate an API call
def trigger_api_call(event_data):
    url = "https://jsonplaceholder.typicode.com/posts"  # Dummy API for testing
    payload = {"event": event_data}
    response = requests.post(url, json=payload)
    print(f"API called with data: {payload}, Response: {response.status_code}")


# Start Kafka container
with KafkaContainer() as kafka:
    bootstrap_servers = kafka.get_bootstrap_server()
    print(f"Kafka is running at: {bootstrap_servers}")

    # Configure producer
    producer_config = {"bootstrap.servers": bootstrap_servers}
    producer = Producer(producer_config)

    # Produce test messages
    topic = "test_topic"
    messages = [
        ("key1", "normal_event"),
        ("key2", "trigger_api"),  # This should trigger the API call
        ("key3", "another_event"),
    ]

    for key, value in messages:
        producer.produce(topic, key=key, value=value)
    producer.flush()
    print("Messages sent.")

    # Configure consumer
    consumer_config = {
        "bootstrap.servers": bootstrap_servers,
        "group.id": "test-group",
        "auto.offset.reset": "earliest",
    }
    consumer = Consumer(consumer_config)
    consumer.subscribe([topic])

    # Poll for messages
    timeout = 10
    start_time = time.time()
    while time.time() - start_time < timeout:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())

        message_value = msg.value().decode()
        print(f"Received message: {message_value} from topic {msg.topic()}")

        # If the event is "trigger_api", call the API
        if message_value == "trigger_api":
            trigger_api_call(message_value)

    consumer.close()
