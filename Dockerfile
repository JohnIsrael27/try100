# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# install dependencies if you have requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY app/ ./app

# set env
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app/app.py    

# expose port used by your app
EXPOSE 5000

# run (adjust if you use gunicorn or other)
CMD ["python", "app/app.py"]
