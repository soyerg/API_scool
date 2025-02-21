# Utiliser une version plus récente de Python
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Définir le répertoire de travail
WORKDIR /app

# Copier tout le projet (y compris le dossier "app")
COPY . /app

# Installer les dépendances
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Ajouter wait-for-it
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# S'assurer que import_csv.py est exécutable
RUN chmod +x /app/app/import_csv.py

# Lancer FastAPI
CMD ["/wait-for-it.sh", "db:5432", "--", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
