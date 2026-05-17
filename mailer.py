# -*- coding: utf-8 -*-
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

load_dotenv()

SMTP_HOST     = os.getenv("SMTP_HOST", "smtp.hostinger.com")
SMTP_PORT     = int(os.getenv("SMTP_PORT", 465))
SMTP_USER     = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_FROM     = os.getenv("SMTP_FROM_EMAIL")
SMTP_NAME     = os.getenv("SMTP_FROM_NAME", "Analyses Commercial")
MAIL_SUPPORT  = os.getenv("SMTP_USER")

def envoyer_email(destinataire, sujet, corps, html=False, chemin_piece_jointe=None):
    try:
        msg = MIMEMultipart("mixed")
        msg["Subject"] = sujet
        msg["From"]    = f"{SMTP_NAME} <{SMTP_FROM}>"
        msg["To"]      = destinataire

        type_corps = "html" if html else "plain"
        msg.attach(MIMEText(corps, type_corps, "utf-8"))

        if chemin_piece_jointe and os.path.exists(chemin_piece_jointe):
            with open(chemin_piece_jointe, "rb") as f:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(f.read())
            encoders.encode_base64(part)
            nom_fichier = os.path.basename(chemin_piece_jointe)
            part.add_header("Content-Disposition", f"attachment; filename={nom_fichier}")
            msg.attach(part)

        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_FROM, destinataire, msg.as_string())

        print(f"OK email envoye vers {destinataire}")
        return True

    except Exception as e:
        print(f"ERREUR : {e}")
        return False


def envoyer_debug(sujet, message):
    return envoyer_email(
        destinataire=MAIL_SUPPORT,
        sujet=f"[DEBUG] {sujet}",
        corps=message
    )


def envoyer_rapport(destinataire, sujet, corps, chemin_fichier=None):
    return envoyer_email(
        destinataire=destinataire,
        sujet=sujet,
        corps=corps,
        html=True,
        chemin_piece_jointe=chemin_fichier
    )
