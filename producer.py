from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def send_data():
    while True:
        classes = ['A', 'B', 'C']
        subjects = ['Math', 'Science', 'History']
        
        for class_name in classes:
            for subject in subjects:
                score = random.randint(0, 20)
                
                data = {'class': class_name, 'subject': subject, 'score': score}
                producer.send('student-scores', value=data)
                print(f"Sent: {data}")

        time.sleep(5)  

if __name__ == "__main__":
    send_data()
