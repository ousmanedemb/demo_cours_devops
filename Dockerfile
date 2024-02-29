# Utiliser une image de base avec Python
FROM python:3.12.2

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

#RUN git clone https://github.com/streamlit/streamlit-example.git .
# Copier les fichiers nécessaires dans le conteneur
COPY Program.py /app
# Installer les dépendances Python
RUN pip install streamlit

# Exposer le port utilisé par Streamlit

EXPOSE 8501

# Commande pour exécuter l'application Streamlit

CMD ["streamlit", "run", "Program.py", "--server.port=8501"]

