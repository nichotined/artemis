from artemis.backend.core.kafka import KafkaClient


if __name__ == "__main__":
    config = {
        "bootstrap.servers": "10.222.15.158:9092",
        "group.id": "bid_loans",
        "session.timeout.ms": 6000,
        "auto.offset.reset": "earliest",
        "debug": "all",
    }

    consumer = KafkaClient().new_consumer(config)
    consumer.subscribe(["bid_loans"])
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        print("Received message: {}".format(msg.value().decode("utf-8")))
    consumer.close()
