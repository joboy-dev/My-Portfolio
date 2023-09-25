FROM python:3.11.5-slim-bullseye

WORKDIR /app
RUN mkdir staticfiles

# install system dependencies
RUN apt-get update

RUN pip install --upgrade pip

COPY requirements.txt /app/
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input

COPY . /app/

#  create gunicorn log directory
RUN mkdir /var/log/gunicorn

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

EXPOSE 8000

ENTRYPOINT [ "gunicorn", "my_portfolio.wsgi"]