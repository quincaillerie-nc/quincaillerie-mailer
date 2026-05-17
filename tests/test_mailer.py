import sys
sys.path.insert(0, '.')
from mailer import envoyer_email, envoyer_debug

def test_debug():
    result = envoyer_debug("test sujet", "test body")
    assert result is not None
    print("OK - envoyer_debug fonctionne")

if __name__ == "__main__":
    test_debug()
