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

### Envoi à plusieurs destinataires (liste)

```python
from mailer import envoyer_email

envoyer_email(
    destinataire=["client1@example.com", "client2@example.com", "manager@example.com"],
    sujet="Rapport hebdomadaire",
    corps="Bonjour à tous, veuillez trouver ci-joint votre rapport."
)
```

### Envoi avec CC et BCC

```python
from mailer import envoyer_email

envoyer_email(
    destinataire="client@example.com",
    sujet="Rapport avec copie",
    corps="Bonjour, votre rapport est disponible.",
    cc=["chef@example.com", "assistant@example.com"],
    bcc="archive@example.com"
)
```

### Envoi HTML simple

```python
from mailer import envoyer_email

envoyer_email(
    destinataire="client@example.com",
    sujet="Rapport HTML",
    corps="<h1>Bonjour</h1><p>Votre rapport est <b>disponible</b>.</p>",
    html=True
)
```

### Envoi HTML avancé (avec fallback texte)

```python
from mailer import envoyer_email

html_body = """
<html>
  <body>
    <h2 style='color:#2c3e50;'>Rapport Hebdomadaire</h2>
    <p>Bonjour,</p>
    <p>Veuillez trouver ci-dessous un résumé de la semaine :</p>
    <table border='1' cellpadding='8' style='border-collapse:collapse;'>
      <tr style='background:#2c3e50;color:white;'>
        <th>Produit</th><th>Ventes</th><th>Stock</th>
      </tr>
      <tr><td>Vis M6</td><td>340</td><td>1200</td></tr>
      <tr><td>Boulons</td><td>210</td><td>850</td></tr>
    </table>
    <br>
    <p style='color:gray;font-size:12px;'>— Analyses Commercial | Quincaillerie NC</p>
  </body>
</html>
"""

envoyer_email(
    destinataire=["direction@quincaillerie.nc", "manager@quincaillerie.nc"],
    sujet="Rapport Hebdomadaire — Semaine 42",
    corps=html_body,
    html=True,
    texte_fallback="Rapport hebdomadaire disponible. Ouvrez cet email dans un client compatible HTML."
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

### Envoi avec plusieurs pièces jointes

```python
from mailer import envoyer_email

envoyer_email(
    destinataire="client@example.com",
    sujet="Rapport complet",
    corps="Veuillez trouver ci-joint les fichiers de la semaine.",
    chemin_piece_jointe=["rapport.pdf", "stats.xlsx", "facture.pdf"]
)
```

### Combinaison complète

```python
from mailer import envoyer_email

envoyer_email(
    destinataire=["client@example.com", "direction@example.com"],
    sujet="Rapport complet — Semaine 42",
    corps="<h1>Rapport</h1><p>Voir les pièces jointes.</p>",
    html=True,
    texte_fallback="Rapport de la semaine 42 en pièce jointe.",
    cc="assistant@example.com",
    bcc="archive@example.com",
    chemin_piece_jointe=["rapport.pdf", "stats.xlsx"]
)
```

---

## 🧪 Lancer le test

```bash
python test_mailer.py
```

Ce script envoie un email de test à l'adresse configurée dans `.env` pour vérifier que la connexion Hostinger SMTP fonctionne correctement.

---

## 🔧 Paramètres de la fonction `envoyer_email()`

| Paramètre            | Type               | Obligatoire | Description                                          |
|----------------------|--------------------|-------------|------------------------------------------------------|
| `destinataire`       | str ou list        | ✅ Oui      | Adresse(s) email du/des destinataire(s)              |
| `sujet`              | str                | ✅ Oui      | Sujet de l'email                                     |
| `corps`              | str                | ✅ Oui      | Contenu du message (texte ou HTML)                   |
| `html`               | bool               | ❌ Non      | `True` pour envoyer en format HTML (défaut: `False`) |
| `texte_fallback`     | str                | ❌ Non      | Texte alternatif si le client ne supporte pas HTML   |
| `cc`                 | str ou list        | ❌ Non      | Adresse(s) en copie                                  |
| `bcc`                | str ou list        | ❌ Non      | Adresse(s) en copie cachée                           |
| `chemin_piece_jointe`| str ou list        | ❌ Non      | Chemin(s) vers fichier(s) à joindre                  |

---

## 📤 Valeurs de retour

La fonction retourne `True` si l'envoi est réussi, `False` en cas d'erreur.

```python
succes = envoyer_email(destinataire="test@example.com", sujet="Test", corps="Hello")
if succes:
    print("Email envoyé avec succès ✅")
else:
    print("Échec de l'envoi ❌")
```

---

## 🔒 Sécurité

- Les credentials SMTP sont chargés uniquement via le fichier `.env`
- Le fichier `.env` est ignoré par Git via `.gitignore`
- Connexion sécurisée **SSL sur le port 465** (Hostinger)
- Aucun mot de passe en clair dans le code source

---

## 📦 Dépendances

| Package        | Usage                          |
|----------------|--------------------------------|
| `python-dotenv`| Chargement des variables .env  |
| `smtplib`      | Envoi SMTP (inclus Python)     |
| `ssl`          | Connexion sécurisée (inclus)   |
| `email`        | Construction des messages      |

---

## 🛠️ Serveur SMTP Hostinger

| Paramètre | Valeur               |
|-----------|----------------------|
| Hôte      | `smtp.hostinger.com` |
| Port      | `465`                |
| Sécurité  | SSL                  |

---

## ❓ Erreurs fréquentes

| Erreur                          | Cause probable                          | Solution                                      |
|---------------------------------|-----------------------------------------|-----------------------------------------------|
| `SMTPAuthenticationError`       | Mauvais identifiants SMTP               | Vérifier `SMTP_USER` et `SMTP_PASSWORD`       |
| `ConnectionRefusedError`        | Mauvais port ou hôte                    | Vérifier `SMTP_HOST` et `SMTP_PORT`           |
| `FileNotFoundError`             | Pièce jointe introuvable                | Vérifier le chemin du fichier                 |
| `No module named 'dotenv'`      | `python-dotenv` non installé            | Lancer `pip install python-dotenv`            |
| `No module named 'mailer'`      | Script lancé depuis le mauvais dossier  | Lancer depuis la racine du projet             |

---

## 📝 Licence

Projet interne — Quincaillerie NC. Tous droits réservés.
