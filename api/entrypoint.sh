#!/bin/sh

python3.7 /app/manager.py db init

python3.7 /app/manager.py db migrate --message 'initial database migration'
python3.7 /app/manager.py db upgrade

python3.7 /app/manager.py run