# 📧 quincaillerie-mailer

Module Python d'envoi d'emails via Hostinger SMTP pour le projet Quincaillerie.

---

## 📁 Structure du projet

```
quincaillerie-mailer/
├── mailer.py          → Module principal d'envoi
├── test_mailer.py     → Script de test
├── .env               → Variables d'environnement (non versionné)
├── .env.example       → Modèle de configuration
├── .gitignore         → Fichiers ignorés par Git
└── README.md          → Documentation
```

---

## ⚙️ Configuration SMTP Hostinger

Copier `.env.example` en `.env` et remplir vos identifiants :

```env
SMTP_HOST=smtp.hostinger.com
SMTP_PORT=465
SMTP_USER=support@robot-nc.com
SMTP_PASSWORD=ton_mot_de_passe
SMTP_FROM_NAME=Analyses Commercial
SMTP_FROM_EMAIL=support@robot-nc.com
```

> ⚠️ Ne jamais commiter le fichier `.env` sur GitHub.

---

## 🚀 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/ton-compte/quincaillerie-mailer.git
cd quincaillerie-mailer
```

### 2. Installer les dépendances

```bash
pip install python-dotenv
```

### 3. Créer le fichier .env

```bash
cp .env.example .env
```

Puis éditer `.env` avec vos vraies credentials Hostinger.

---

## 💡 Utilisation du module

### Envoi simple

```python
from mailer import envoyer_email

envoyer_email(
    destinataire="client@example.com",
    sujet="Rapport hebdomadaire",
    corps="Bonjour, veuillez trouver ci-joint votre rapport."
)
```

### Envoi avec pièce jointe

```python
from mailer import envoyer_email

envoyer_email(
    destinataire="client@example.com",
    sujet="Rapport avec fichier",
    corps="Bonjour, veuillez trouver ci-joint votre rapport.",
    chemin_piece_jointe="rapport.pdf"
)
```

### Envoi HTML

```python
from mailer import envoyer_email

envoyer_email(
    destinataire="client@example.com",
    sujet="Rapport HTML",
    corps="<h1>Bonjour</h1><p>Votre rapport est disponible.</p>",
    html=True
)
```

---

## 🧪 Lancer le test

```bash
python test_mailer.py
```

Ce script envoie un email de test à l'adresse configurée dans `.env` pour vérifier que la connexion Hostinger SMTP fonctionne correctement.

---

## 🔧 Paramètres de la fonction envoyer_email()

| Paramètre            | Type    | Obligatoire | Description                        |
|----------------------|---------|-------------|------------------------------------|
| destinataire         | str     | ✅ Oui      | Adresse email du destinataire      |
| sujet                | str     | ✅ Oui      | Sujet de l'email                   |
| corps                | str     | ✅ Oui      | Contenu du message                 |
| chemin_piece_jointe  | str     | ❌ Non      | Chemin vers un fichier à joindre   |
| html                 | bool    | ❌ Non      | True pour envoyer en format HTML   |

---

## 🔒 Sécurité

- Les credentials SMTP sont chargés uniquement via le fichier `.env`
- Le fichier `.env` est ignoré par Git via `.gitignore`
- Connexion sécurisée SSL sur le port 465 (Hostinger)
- Aucun mot de passe en clair dans le code source

---

## 📦 Dépendances

| Package        | Usage                          |
|----------------|--------------------------------|
| python-dotenv  | Chargement des variables .env  |
| smtplib        | Envoi SMTP (inclus Python)     |
| ssl            | Connexion sécurisée (inclus)   |

---

## 🛠️ Serveur SMTP Hostinger

| Paramètre | Valeur             |
|-----------|--------------------|
| Hôte      | smtp.hostinger.com |
| Port      | 465                |
| Sécurité  | SSL                |

---

## 📝 Licence

Projet interne — Quincaillerie NC. Tous droits réservés.
