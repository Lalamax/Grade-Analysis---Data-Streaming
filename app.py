import tkinter as tk
import tkinter.ttk as ttk
import json
from kafka import KafkaConsumer
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def consume_messages():
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
        update_data(data)

def update_data(data):
    scores.append(data)
    if len(scores) > 100:
        scores.pop(0)

   
    table.delete(*table.get_children())  
    for i, score in enumerate(scores):
        
        table.insert('', 'end', iid=i, values=(i, score['class'], score['subject'], score['score']))

    
    update_graph()


def update_graph():
    ax.clear()
    ax.set_ylim(0, 20)

    
    subject_means = {}
    for score in scores:
        subject = score['subject']
        score_value = score['score']
        if subject in subject_means:
            subject_means[subject]['sum'] += score_value
            subject_means[subject]['count'] += 1
        else:
            subject_means[subject] = {'sum': score_value, 'count': 1}

    subjects = []
    means = []
    for subject, data in subject_means.items():
        mean = data['sum'] / data['count']
        subjects.append(subject)
        means.append(mean)

    ax.bar(subjects, means, color='skyblue')
    ax.set_xlabel('Matière')
    ax.set_ylabel('Moyenne des eléves')
    ax.set_title('Note moyenne')
    canvas.draw()


window = tk.Tk()
window.title("Analyse des Résultats Scolaires en Temps Réel")

columns = ('ID', 'Class', 'Subject', 'Score')
table = ttk.Treeview(window, columns=columns, show='headings')
table.heading('ID', text='ID')
table.heading('Class', text='Class')
table.heading('Subject', text='Subject')
table.heading('Score', text='Score')
table.pack(side='top', fill='both', expand=True)

fig, ax = plt.subplots(figsize=(8, 4))
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

scores = []

threading.Thread(target=consume_messages, daemon=True).start()

window.mainloop()
