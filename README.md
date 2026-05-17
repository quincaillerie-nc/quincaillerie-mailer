# 📬 Quincaillerie Mailer

> Module Python d'envoi d'emails officiel pour **Quincaillerie NC**.  
> Léger, simple à intégrer, sécurisé — conçu pour s'intégrer dans tous les services de l'écosystème Quincaillerie NC.

---

## 📋 Table des matières

- [Présentation](#-présentation)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Utilisation](#-utilisation)
- [Exemples avancés](#-exemples-avancés)
- [Structure du projet](#-structure-du-projet)
- [Tests](#-tests)
- [Dépendances](#-dépendances)
- [Sécurité](#-sécurité)
- [Contribuer](#-contribuer)
- [Auteur](#-auteur)

---

## 📖 Présentation

`quincaillerie-mailer` est un module Python autonome permettant l'envoi d'emails transactionnels pour les services de Quincaillerie NC.

Il est conçu pour être :
- **Importé** dans n'importe quel autre module Python du projet
- **Simple** à configurer via un fichier `.env`
- **Testé** avec une suite de tests unitaires intégrée
- **Sécurisé** — aucun credential dans le code source

Cas d'usage typiques :
- Confirmation de commande client
- Notification interne au personnel
- Alertes automatiques du serveur
- Envoi de factures ou documents

---

## ✅ Prérequis

- Python **3.10+**
- `pip` installé



---

## 📦 Installation

### Cloner le dépôt

```bash
git clone git@github.com:quincaillerie-nc/quincaillerie-mailer.git
cd quincaillerie-mailer
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Crée un fichier `.env` à la racine du projet :

```env
MAIL_SENDER=quincaillerie.nc@gmail.com
MAIL_PASSWORD=xxxx xxxx xxxx xxxx
```

| Variable | Description |
|---|---|
| `MAIL_SENDER` | Adresse email expéditeur Gmail |
| `MAIL_PASSWORD` | Mot de passe d'application Gmail (16 caractères) |

> ⚠️ **Ne jamais committer le fichier `.env`** — il est protégé par le `.gitignore`

---

## 🚀 Utilisation

### Import basique

```python
from mailer import send_email

send_email(
    to="client@example.com",
    subject="Votre commande est prête",
    body="Bonjour, votre commande est disponible en magasin."
)
```

### Paramètres de `send_email()`

| Paramètre | Type | Obligatoire | Description |
|---|---|---|---|
| `to` | `str` | ✅ | Adresse email du destinataire |
| `subject` | `str` | ✅ | Sujet de l'email |
| `body` | `str` | ✅ | Corps du message (texte brut) |

---

## 💡 Exemples avancés

### Confirmation de commande

```python
from mailer import send_email

def confirmer_commande(client_email, numero_commande):
    send_email(
        to=client_email,
        subject=f"Confirmation commande #{numero_commande}",
        body=(
            f"Bonjour,\n\n"
            f"Votre commande #{numero_commande} a bien été enregistrée.\n"
            f"Vous serez contacté dès qu'elle sera disponible.\n\n"
            f"Merci de votre confiance,\n"
            f"L'équipe Quincaillerie NC"
        )
    )
```

### Alerte interne

```python
from mailer import send_email

def alerter_stock(produit, quantite):
    send_email(
        to="responsable@quincaillerie.nc",
        subject=f"⚠️ Stock bas : {produit}",
        body=f"Le produit '{produit}' a atteint un stock critique : {quantite} unités restantes."
    )
```

### Intégration dans le serveur principal

```python
# Dans serveur-quincaillerie
import sys
sys.path.append('../quincaillerie-mailer')
from mailer import send_email

send_email(
    to="admin@quincaillerie.nc",
    subject="Serveur démarré",
    body="Le serveur Quincaillerie NC est opérationnel."
)
```

---

## 📁 Structure du projet

```
quincaillerie-mailer/
│
├── mailer.py            # Fonction principale send_email()
├── __init__.py          # Export du module
│
├── tests/
│   └── test_mailer.py   # Tests unitaires
│
├── .env                 # Variables d'environnement (NON commité)
├── .gitignore           # Fichiers ignorés par Git
├── requirements.txt     # Dépendances Python
└── README.md            # Documentation
```

---

## 🧪 Tests

Lancer tous les tests :

```bash
python -m pytest tests/ -v
```

Résultat attendu :

```
tests/test_mailer.py::test_send_email_success    PASSED
tests/test_mailer.py::test_missing_env_vars      PASSED
tests/test_mailer.py::test_invalid_recipient     PASSED
```

---

## 📚 Dépendances

| Package | Version | Rôle |
|---|---|---|
| `python-dotenv` | 1.0.0 | Chargement des variables `.env` |

Installation manuelle :

```bash
pip install python-dotenv
```

---

## 🔒 Sécurité

- Les credentials sont stockés dans `.env`, jamais dans le code
- Le `.gitignore` protège les fichiers sensibles
- Utilisation d'un **mot de passe d'application Gmail** dédié
- Aucune donnée client n'est stockée par le module

---

## 🤝 Contribuer

1. Fork le dépôt
2. Crée une branche : `git checkout -b feature/ma-feature`
3. Commit : `git commit -m "feat: ma nouvelle feature"`
4. Push : `git push origin feature/ma-feature`
5. Ouvre une **Pull Request**

---

## 👤 Auteur

**Quincaillerie NC**  
🔗 [github.com/quincaillerie-nc](https://github.com/quincaillerie-nc)

---

*Documentation générée pour quincaillerie-mailer — Quincaillerie NC © 2025*
