#!/bin/bash

# Django setting
export DJANGO_SETTINGS_MODULE='text2code.settings.production'

poetry run python -m uvicorn text2code.asgi:application --host 0.0.0.0 --port 8000