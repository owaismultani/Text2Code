from .base import *

# Disable Debugging
DEBUG = False

# Allowed Headers
CORS_ALLOW_HEADERS = ["*"]
CORS_ALLOWED_ORIGIN_REGEXES = ["*"]
CORS_ALLOW_ALL_ORIGINS = True

# Allowed Methods
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]