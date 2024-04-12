# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE text2code.settings.production

# Set the working directory in the container
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copy the start.sh script into the container at /usr/src/app
COPY start.sh /usr/src/app/start.sh

# Make sure the script is executable
RUN chmod +x /usr/src/app/start.sh

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the script when the container launches
CMD ["/usr/src/app/start.sh"]
