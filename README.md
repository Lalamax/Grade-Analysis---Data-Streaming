# Grade Analysis - Data Streaming

Ce projet ambitieux a été réalisé dans le cadre de notre cours avancé de Data Engineering. Notre objectif principal était de développer une application robuste pour le suivi en temps réel des notes des étudiants. Pour ce faire, nous avons choisi d'utiliser Kafka, une plateforme de streaming de données hautement évolutive, ainsi que Tkinter pour concevoir une interface utilisateur intuitive.

## Producer

<img width="695" alt="image" src="https://github.com/Lalamax/Grade-Analysis---Data-Streaming/assets/20906460/d743414c-9e35-4e4d-84d8-1e873a47207d">

Le producteur joue un rôle crucial dans notre architecture. Il est chargé de générer des données simulées représentant les notes des étudiants et de les envoyer de manière continue au sujet Kafka nommé "student-scores". Ce composant est conçu pour simuler un environnement réaliste de collecte de données, essentiel pour tester et démontrer la capacité de notre système à gérer des flux de données en direct.

## Consumer

<img width="695" alt="image" src="https://github.com/Lalamax/Grade-Analysis---Data-Streaming/assets/20906460/50b6a15a-5895-4965-87b4-792920f14a4c">

Le consommateur est l'autre moitié de notre système de streaming de données. Il est responsable de récupérer les données à partir du sujet Kafka "student-scores" et de les afficher de manière lisible dans la console. Cette partie du projet met l'accent sur la fiabilité et l'efficacité du traitement des données en streaming, en assurant que les informations sont reçues et traitées de manière opportune et précise.

## Application avec Tkinter

![](https://github.com/Lalamax/Grade-Analysis---Data-Streaming/blob/main/APP%20test.gif)

L'application développée avec Tkinter est une vitrine visuelle de notre système de suivi des notes. Elle offre une interface graphique conviviale qui affiche en temps réel les données provenant de Kafka. Un aspect clé de cette interface est la visualisation des moyennes de notes par matière, présentées dans un tableau interactif. Cette fonctionnalité permet aux utilisateurs, qu'ils soient enseignants ou administrateurs, de comprendre rapidement les performances des étudiants dans différentes disciplines.


## Application avec Docker

<img width="1655" alt="image" src="https://github.com/Lalamax/Grade-Analysis---Data-Streaming/assets/20906460/2b4e21e8-bd0d-453b-aeca-ca372663950b">

Pour assurer une gestion des dépendances simplifiée et une portabilité accrue, nous avons dockerisé notre application complète. Docker offre un environnement conteneurisé où tous les composants nécessaires, y compris Kafka, Tkinter et leurs dépendances, sont encapsulés. Cela facilite grandement le déploiement et l'exécution de notre application dans divers environnements, minimisant ainsi les problèmes liés aux différences de configuration et assurant une cohérence entre les environnements de développement, de test et de production.

## Conclusion

En résumé, notre projet de suivi des notes en temps réel combine des technologies modernes telles que Kafka et Tkinter avec des pratiques de développement robustes comme la conteneurisation Docker. Ce README vise à fournir une vue d'ensemble claire et complète de notre solution, de son architecture à son fonctionnement pratique, pour inspirer et guider ceux qui souhaitent explorer les domaines passionnants du Data Engineering et du streaming de données.






