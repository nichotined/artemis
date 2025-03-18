from confluent_kafka import Consumer, Producer


class KafkaClient:
    def __init__(self):
        pass

    def new_consumer(self, config: dict) -> Consumer:
        return Consumer(config)

    def new_producer(self, config: dict) -> Producer:
        return Producer(config)
