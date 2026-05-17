# Module Mailer

Module d'envoi d'emails via SMTP SSL pour le projet Quincaillerie.

## Description

Ce module gere l'envoi d'emails depuis le serveur ou en local.
Il utilise un serveur SMTP Hostinger avec chiffrement SSL sur le port 465.
La configuration est chargee depuis un fichier .env a la racine du projet.

## Fonctions disponibles

### envoyer_email(destinataire, sujet, corps, html=False)
Envoie un email a un destinataire.
- destinataire : adresse email cible (str)
- sujet        : objet du mail (str)
- corps        : contenu du mail (str)
- html         : True si le corps est en HTML, False pour texte brut
- retourne     : True si succes, False si erreur

### envoyer_debug(sujet, message)
Envoie un email de supervision au support.
Prefixe automatiquement le sujet avec [DEBUG].
- sujet   : objet du mail (str)
- message : contenu (str)
- retourne : True si succes, False si erreur

## Configuration .env requise

SMTP_HOST=smtp.hostinger.com
SMTP_PORT=465
SMTP_USER=support@robot-nc.com
SMTP_PASSWORD=ton_mot_de_passe
SMTP_FROM_EMAIL=support@robot-nc.com
SMTP_FROM_NAME=Analyses Commercial

## Exemple d'utilisation

from modules.mailer import envoyer_email, envoyer_debug

envoyer_email("client@example.com", "Facture", "Votre facture est disponible")
envoyer_debug("Erreur critique", "Le script X a plante a 03h00")

## Dependances

- python-dotenv
- smtplib (standard Python)
- email (standard Python)

## Auteur

Projet Quincaillerie NC
