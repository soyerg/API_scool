# API de Données des Écoles

Ce projet est une application basée sur FastAPI qui gère les données des écoles et fournit des endpoints pour la récupération et la visualisation des données. Le projet inclut également une application Dash pour visualiser la distribution des valeurs IPS (Indice de Position Sociale).

## Structure du Projet

```
/api/tp
├── app
│   ├── __init__.py
│   ├── auth.py
│   ├── database.py
│   ├── import_csv.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── services.py
├── dash_app
│   ├── __init__.py
│   ├── app.py
│   ├── requirements.txt
├── .env
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Fichiers et leurs Interactions

### app/auth.py

Ce fichier contient des fonctions pour encoder et décoder les tokens JWT, ainsi que pour vérifier les tokens pour l'authentification. Il utilise la bibliothèque `jwt` pour gérer les opérations JWT.

### app/database.py

Ce fichier configure la connexion à la base de données en utilisant SQLAlchemy. Il définit `SessionLocal` et `engine` pour interagir avec la base de données.

### app/import_csv.py

Ce fichier contient une fonction pour importer les données des écoles à partir d'un fichier CSV dans la base de données. Il lit le fichier CSV, traite chaque ligne et insère les données dans la table `schools`.

### app/main.py

Ceci est le point d'entrée principal pour l'application FastAPI. Il définit les endpoints de l'API et inclut des dépendances globales pour la vérification des tokens. Les endpoints incluent :
- `/`: Un simple endpoint racine.
- `/current-date`: Retourne la date et l'heure actuelles.
- `/read-header/`: Lit un en-tête personnalisé de la requête.
- `/schools/`: Récupère toutes les données des écoles.
- `/first-school/`: Récupère le premier enregistrement d'école.
- `/schools/{school_id}`: Récupère une école spécifique par ID.
- `/load-data/`: Charge les données à partir d'un fichier CSV dans la base de données.
- `/token`: Génère un token JWT pour l'authentification.
- `/secure-data`: Un endpoint sécurisé qui nécessite une authentification.

### app/models.py

Ce fichier définit les modèles SQLAlchemy pour la base de données. Il inclut le modèle `School`, qui représente la table `schools`.

### app/schemas.py

Ce fichier définit les schémas Pydantic pour la validation et la sérialisation des données. Il inclut des schémas pour créer et récupérer les données des écoles.

### app/services.py

Ce fichier est destiné aux fonctions de service liées à l'application. Actuellement, il est vide car les services pour `Item` ont été supprimés.

### dash_app/app.py

Ce fichier contient l'application Dash pour visualiser la distribution des valeurs IPS. Il récupère les données du service FastAPI et affiche un histogramme des valeurs IPS.

### dash_app/requirements.txt

Ce fichier liste les dépendances pour l'application Dash.

### .env

Ce fichier contient les variables d'environnement pour le projet, y compris les identifiants de la base de données et les clés secrètes JWT.

### docker-compose.yml

Ce fichier définit la configuration Docker Compose pour le projet. Il inclut des services pour l'application FastAPI, la base de données PostgreSQL et l'application Dash.

### Dockerfile

Ce fichier définit l'image Docker pour l'application FastAPI. Il installe les dépendances et configure l'application pour s'exécuter avec Uvicorn.

### requirements.txt

Ce fichier liste les dépendances pour l'application FastAPI.

## Comment Exécuter le Projet

1. **Démarrer les Conteneurs Docker**:
   Assurez-vous que vos conteneurs Docker sont en cours d'exécution. Vous pouvez utiliser la commande suivante pour démarrer les conteneurs :
   ```sh
   docker-compose up --build
   ```

2. **Générer un Token JWT**:
naviguer entre http://localhost:5000/docs et http://localhost:8050/
il faut penser a charger les donnés avant de faire des requetes avec load data



