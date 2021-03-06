from kafka import KafkaConsumer
import sqlite3
from json import loads, dumps

# Key, this program will not send any duplicate messages to the database
consumer = KafkaConsumer(
    'numtest',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
)
# add this param to turn the messages into dictionaries
# value_deserializer=lambda x: loads(x.decode('utf-8'))
# note that you don't have to initially tie consumer to a topic(s)
# you can subscribe to a topic(s) after set up with the line: 
# consumer.subscribe(topics)

# Sqlite3 connenction 
conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS collection (data json);')
conn.commit()

# look at messages then put in into sqlite db
try:
    for message in consumer:

        print(message)
        print('Key: {}, Value: {} at offset: {}\n'.format(message.key, message.value, message.offset))

        c.execute('insert into collection values (?)', [message.value])
        conn.commit()
except Exception as e:
    print(f'Unexpected error: {e}')
    
conn.close()