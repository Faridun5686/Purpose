# Python image
FROM python:3.12-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Workdir
WORKDIR /app

# Paketlarni nusxalash va o'rnatish
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Loyihani nusxalash
COPY . /app/

# Static fayllarni yig'ish
RUN python manage.py collectstatic --noinput

# Django serverni ishga tushirish (production)
CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]