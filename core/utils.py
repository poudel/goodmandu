import string
import secrets
from django.utils.text import slugify as original_slugify
from django.utils import timezone
from core.stop_words import STOP_WORDS


def tz_today():
    return timezone.localtime(timezone.now()).date()


def slugify(text):
    texts = [t for t in text.split(" ") if t.lower() not in STOP_WORDS]
    return original_slugify(" ".join(texts))


def get_random_string(length=25, uppercase=True, lowercase=True, numeric=True):
    seed = []
    if uppercase:
        seed.append(string.ascii_uppercase)

    if lowercase:
        seed.append(string.ascii_lowercase)

    if numeric:
        seed.append(string.digits)
    alphabet = "".join(seed)
    return ''.join(secrets.choice(alphabet) for i in range(length))
