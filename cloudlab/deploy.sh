#!/bin/bash
echo "Starting deployment..."

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate

echo "Deployment complete!"

