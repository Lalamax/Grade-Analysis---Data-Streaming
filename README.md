# Grade Analysis - Data Streaming

Ce projet a été réalisé dans le cadre de notre cours de Data Engineering. Il s'agit d'une application de suivi des notes en temps réel à l'aide de Kafka pour le streaming des données et de Tkinter pour l'interface graphique.

## Producer

<img width="695" alt="image" src="https://github.com/Lalamax/Grade-Analysis---Data-Streaming/assets/20906460/d743414c-9e35-4e4d-84d8-1e873a47207d">

Le producteur génère des données de manière simulée et les envoie au sujet Kafka "student-scores".

## Consumer

<img width="695" alt="image" src="https://github.com/Lalamax/Grade-Analysis---Data-Streaming/assets/20906460/50b6a15a-5895-4965-87b4-792920f14a4c">

Le consommateur récupère les données du sujet Kafka "student-scores" et les affiche dans la console.

## Application avec Tkinter

![](https://github.com/Lalamax/Grade-Analysis---Data-Streaming/blob/main/APP%20test.gif)

L'application Tkinter affiche les données en temps réel à partir de Kafka. Elle comprend un tableau pour visualiser la moyenne des notes par matiére.

## Application avec Docker

<img width="1655" alt="image" src="https://github.com/Lalamax/Grade-Analysis---Data-Streaming/assets/20906460/2b4e21e8-bd0d-453b-aeca-ca372663950b">

L'application est également dockerisée pour une gestion simplifiée des dépendances et de l'exécution.






