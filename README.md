# Grade Analysis - Data Streaming

Ce projet a été réalisé dans le cadre de notre cours de Data Engineering. Il s'agit d'une application de suivi des notes en temps réel à l'aide de Kafka pour le streaming des données et de Tkinter pour l'interface graphique.

## Producer

![Producer](https://github.com/Lalamax/Grade-Analysis---Data-Streaming/blob/main/assets/producer.png)

Le producteur génère des données de manière simulée et les envoie au sujet Kafka "student-scores".

## Consumer

![Consumer](https://github.com/Lalamax/Grade-Analysis---Data-Streaming/blob/main/assets/consumer.png)

Le consommateur récupère les données du sujet Kafka "student-scores" et les affiche dans la console.

## Application avec Tkinter

![Application Tkinter](https://github.com/Lalamax/Grade-Analysis---Data-Streaming/blob/main/assets/app.gif)

L'application Tkinter affiche les données en temps réel à partir de Kafka. Elle comprend un tableau pour visualiser la moyenne des notes par matiére.
## Application avec Docker

![Application Docker](https://github.com/Lalamax/Grade-Analysis---Data-Streaming/blob/main/assets/docker.png)

L'application est également dockerisée pour une gestion simplifiée des dépendances et de l'exécution.






