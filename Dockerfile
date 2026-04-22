# FROM : image de base — on part d'une image Python officielle
# "slim" = version allégée (moins de poids, idéale pour la prod)
FROM python:3.11-slim

# WORKDIR : définit le dossier de travail dans le conteneur
# Toutes les commandes suivantes s'exécutent depuis ce dossier
WORKDIR /app

# COPY : copie les fichiers depuis ta machine vers le conteneur
# On copie requirements.txt EN PREMIER (optimisation du cache)
COPY requirements.txt .

# RUN : exécute une commande lors de la construction de l'image
# --no-cache-dir évite de stocker le cache pip dans l'image
RUN pip install --no-cache-dir -r requirements.txt

# COPY : copie maintenant tout le reste du code
COPY . .

# CMD : commande lancée quand on démarre un conteneur
# C'est le point d'entrée de ton application
CMD ["python", "app.py"]
