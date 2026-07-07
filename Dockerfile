# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 7860

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

# Copy project
COPY . /app/

# Create a non-root user
RUN useradd -m myuser

# Grant permissions to the non-root user
RUN chown -R myuser:myuser /app

# Switch to the non-root user
USER myuser

# Run collectstatic
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 7860

# Start the application
CMD python manage.py migrate && gunicorn --bind 0.0.0.0:7860 config.wsgi:application
