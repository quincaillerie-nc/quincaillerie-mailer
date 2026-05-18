# -*- coding: utf-8 -*-
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from dotenv import load_dotenv

# Charge le .env depuis le même dossier que mailer.py
load_dotenv(Path(__file__).parent / ".env")

SMTP_HOST     = os.getenv("SMTP_HOST",      "smtp.hostinger.com")
SMTP_PORT     = int(os.getenv("SMTP_PORT",  "465"))
SMTP_USER     = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_FROM     = os.getenv("SMTP_FROM_EMAIL")
SMTP_NAME     = os.getenv("SMTP_FROM_NAME", "Analyses Commercial")
MAIL_SUPPORT  = os.getenv("SMTP_USER")


def _to_list(value) -> list:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    return list(value)


def _attacher_fichier(msg: MIMEMultipart, chemin: str) -> None:
    path = Path(chemin)
    if not path.exists():
        print(f"[MAILER] ⚠️  Pièce jointe introuvable : {chemin}")
        return
    with open(path, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={path.name}")
    msg.attach(part)


def envoyer_email(
    destinataire,
    sujet: str,
    corps: str,
    html: bool = False,
    texte_fallback: str = None,
    cc=None,
    bcc=None,
    chemin_piece_jointe=None
) -> bool:
    try:
        dest_list = _to_list(destinataire)
        cc_list   = _to_list(cc)
        bcc_list  = _to_list(bcc)
        pj_list   = _to_list(chemin_piece_jointe)

        msg = MIMEMultipart("mixed")
        msg["Subject"] = sujet
        msg["From"]    = f"{SMTP_NAME} <{SMTP_FROM}>"
        msg["To"]      = ", ".join(dest_list)
        if cc_list:
            msg["Cc"] = ", ".join(cc_list)

        if html and texte_fallback:
            alt = MIMEMultipart("alternative")
            alt.attach(MIMEText(texte_fallback, "plain", "utf-8"))
            alt.attach(MIMEText(corps,          "html",  "utf-8"))
            msg.attach(alt)
        else:
            type_corps = "html" if html else "plain"
            msg.attach(MIMEText(corps, type_corps, "utf-8"))

        for pj in pj_list:
            _attacher_fichier(msg, pj)

        tous = dest_list + cc_list + bcc_list

        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_FROM, tous, msg.as_string())

        print(f"[MAILER] ✅ Email envoyé → {', '.join(dest_list)}")
        return True

    except Exception as e:
        print(f"[MAILER] ❌ Erreur envoi : {e}")
        return False


def envoyer_debug(sujet: str, message: str) -> bool:
    return envoyer_email(
        destinataire=MAIL_SUPPORT,
        sujet=f"[DEBUG] {sujet}",
        corps=message
    )


def envoyer_rapport(
    destinataire,
    sujet: str,
    corps: str,
    chemin_fichier=None
) -> bool:
    return envoyer_email(
        destinataire=destinataire,
        sujet=sujet,
        corps=corps,
        html=True,
        chemin_piece_jointe=chemin_fichier
    )