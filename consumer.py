from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'student-scores',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  
    enable_auto_commit=True,
    group_id='student-score-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    data = message.value
    print(f"Received: {data}")

