from time import sleep
from json import dumps
from kafka import KafkaProducer
import atexit

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                        value_serializer=lambda x:
                        dumps(x).encode('utf-8'))
# bootstrap_servers sets host, defaults to 9092
# value_serializer sets how value should be serialized before sending to broker
# lambda x:dumps(x).encode('utf-8') converts the data to a JSON file and encodes it to utf-8

# when program ends or is shutdown, this code will close the producer
@atexit.register
def cleanup():
    print('Shutting down producer')
    producer.close()

for e in range(1000):
    data = {'number': e}
    producer.send('numtest', key=b'test', value=data)
    # key although data is a key value pair, data itself is the value and it has a null topic key
    sleep(3)
    
