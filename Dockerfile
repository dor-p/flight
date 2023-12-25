# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV RUNNING_IN_DOCKER yes

# Set the working directory inside the container
WORKDIR /varcard-be

# Install system dependencies and cleanup in the same step to reduce image size
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev build-essential python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip

# Install Python dependencies
COPY requirements.txt /varcard-be/
RUN pip install -r requirements.txt

# Copy the app directory contents into the container
COPY app /varcard-be/app

# Use a non-root user to run our application
RUN useradd -m myuser
USER myuser

# Specify the command to run on container start
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
