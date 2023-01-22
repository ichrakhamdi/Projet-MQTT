# Projet-MQTT
On désire implémenter une application qui permet de surveiller la température d’une pièce.
L’application se base sur l’utilisation du protocole MQTT.
On va simuler un capteur de température avec un client MQTT (publisher) qui permet de publier régulièrement une valeur correspondant à la température.
Une seconde application cliente (subscriber) permettra d’afficher à la demande les valeurs publiées et recevra également une alerte automatiquement si la température dépasse un
certain seuil.
On va utiliser un broker MQTT public et gratuit parmi les brokers disponibles sur Internet afin de faire communiquer les deux applications.
