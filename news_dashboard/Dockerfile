# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

RUN pip install -r requirements.txt

# Collect static files
EXPOSE 8000
# Make port 8000 available to the world outside this container
RUN ls
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py runserver

# Define the command to run on container start
