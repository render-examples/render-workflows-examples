# OPTIONAL
#
# If you select the Docker runtime when creating your workflow service,
# Render builds your project based on this Dockerfile instead of running
# on Render's native Python runtime.

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
