# DBWONT
New Repeater for HTTP request, make the same work of repeater function of burpsuite bin in python. U can modified all information and join file. in the requests 
# REPEATER - Programme de répétition de requêtes HTTP

## Présentation
REPEATER est un programme Python qui permet d'envoyer des requêtes HTTP personnalisées et de répéter les requêtes précédentes avec des modifications si nécessaire. Il offre une interface simple pour interagir avec les serveurs HTTP et envoyer des requêtes GET, POST ou POST-FORM.

## Installation
1. Assurez-vous d'avoir Python installé sur votre système.
2. Clonez ce dépôt ou téléchargez le fichier source `repeater.py`.
3. Installez les dépendances requises en exécutant la commande suivante :
pip install -r requirements.txt

markdown


## Utilisation
1. Exécutez le programme en utilisant la commande suivante :

python repeater.py

bash

2. Suivez les instructions à l'écran pour spécifier l'URL de destination, la méthode HTTP, les en-têtes, les données et les fichiers à envoyer.
3. Vous pouvez choisir de répéter la requête précédente en répondant "yes" lorsque vous y êtes invité.
4. Pour modifier une requête précédente, répondez "yes" à la question "Do you want to modify the request?" et suivez les instructions supplémentaires.
5. Lorsque vous avez terminé d'utiliser le programme, vous pouvez arrêter l'exécution en appuyant sur Ctrl+C.

## Remarques
- Assurez-vous d'avoir une connexion Internet active pour pouvoir envoyer des requêtes HTTP avec succès.
- Le programme utilise les bibliothèques `pycurl` et `scapy`. Veuillez vous assurer de les installer en exécutant la commande `pip install -r requirements.txt` avant de lancer le programme.

N'hésitez pas à explorer le code source du programme pour plus de détails sur son fonctionnement interne et ses fonctionnalités avancées.
