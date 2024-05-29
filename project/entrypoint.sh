#!/bin/bash

# Configuration des flags d'erreurs pour bash
set -o errexit
set -o pipefail
set -o nounset

# Execution of the /start file received in parameter
python manage.py migrate
# python manage.py collectstatic --noinput --clear
exec "$@"