# Página Compras Públicas Transparentes

Implements a Django-based app that helps visualizing and exploring public tenders in Chile.

## Secret key setting

Django requires a secret key in order to start. This key must be kept secret and can be set through the environment variable `DJANGO_SECRET_KEY`:
```
export DJANGO_SECRET_KEY=12345678901234567890123456789012345678901234567890
```

The following python script can be used to generate an appropiate key:
```
from django.utils.crypto import get_random_string
chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
print(get_random_string(50, chars))
```

## Database setting

The following environmental variables define the database settings required by django:
* `DJANGO_DB`: Database name
* `DJANGO_USER`: User name
* `DJANGO_PASS`: Password
* `DJANGO_HOST`: Host
* `DJANGO_PORT`: Port
