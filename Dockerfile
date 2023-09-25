FROM python:3.11.5-slim-bullseye

WORKDIR /app
RUN mkdir staticfiles

COPY . /app/

# install system dependencies
RUN apt-get update

RUN pip install --upgrade pip

# copy requirements file into the docker app then run pip command
# COPY requirements.txt /app/
RUN pip install -r requirements.txt

# COPY manage.py /app/
RUN python manage.py collectstatic --no-input

#  create gunicorn log directory
RUN mkdir /var/log/gunicorn

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

EXPOSE 8000

ENTRYPOINT [ "gunicorn", "my_portfolio.wsgi"]