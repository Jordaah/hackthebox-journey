#!/bin/bash

echo "FLASK_SECRET_KEY=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)" > /app/backend/.env
echo "ALIENT_USERNAME=zaphod_beeblebrox" >> /app/backend/.env
echo "ALIENT_PASSWORD=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)" >> /app/backend/.env

/usr/bin/supervisord -c /etc/supervisord.conf