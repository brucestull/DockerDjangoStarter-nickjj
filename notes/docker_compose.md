# Docker Compose

## Table of Contents

- [Project/App Name Commands](#projectapp-name-commands)
    - [DEV Project/App Name Commands](#dev-projectapp-name-commands)
    - [PROD Project/App Name Commands](#prod-projectapp-name-commands)
- [`docker-compose.yml` Commands](#docker-composeyml-commands)
    - [DEV `docker-compose.yml` Commands](#dev-docker-composeyml-commands)
    - [PROD `docker-compose.prod.yml` Commands](#prod-docker-composeprodyml-commands)
- [Simple `start` and `stop` Commands](#simple-start-and-stop-commands)
- [Misc Commands](#misc-commands)
- [Database Creation Commands](#database-creation-commands)
- [Database Access Commands](#database-access-commands)
- [Docker Compose Commands](#docker-compose-commands)

## Project/App Name Commands

### Django Migrations

### DEV Project/App Name Commands

1. `docker compose -p dds_cu_dev -f docker-compose.yml up -d --build`
    * `docker compose -p dds_cu_dev -f docker-compose.yml up -d --build --remove-orphans`
1. (OPTIONAL) `docker compose -p dds_cu_dev -f docker-compose.yml exec web_dev python manage.py makemigrations`
1. `docker compose -p dds_cu_dev -f docker-compose.yml exec web_dev python manage.py migrate --noinput`
1. `docker compose -p dds_cu_dev -f docker-compose.yml exec web_dev python manage.py createsuperuser --email FlynntKnapp@email.app --username FlynntKnapp_dev`
1. `docker compose -p dds_cu_dev -f docker-compose.yml stop`
    * Alt command to stop containers and remove volumes:
        * `docker compose -p dds_cu_dev -f docker-compose.yml down -v`
1. `docker compose -p dds_cu_dev -f docker-compose.yml start`

[Back to Top](#docker-compose)

### PROD Project/App Name Commands

1. `docker compose -p dds_cu_prod -f docker-compose.prod.yml up -d --build`
    * `docker compose -p dds_cu_prod -f docker-compose.prod.yml up -d --build --remove-orphans`
1. `docker compose -p dds_cu_prod -f docker-compose.prod.yml exec web_prod python manage.py migrate --noinput`
1. `docker compose -p dds_cu_prod -f docker-compose.prod.yml exec web_prod python manage.py createsuperuser --email FlynntKnapp@email.app --username FlynntKnapp_prod`
1. `docker-compose -p dds_cu_prod -f docker-compose.prod.yml exec web_prod python manage.py collectstatic --no-input --clear`
* `docker compose -p dds_cu_prod -f docker-compose.prod.yml stop`
    * Alt command to stop containers and remove volumes:
        * `docker compose -p dds_cu_prod -f docker-compose.prod.yml down -v`
1. `docker compose -p dds_cu_prod -f docker-compose.prod.yml start`

[Back to Top](#docker-compose)

## `docker-compose.yml` Commands

### DEV `docker-compose.yml` Commands

1. `docker compose -f docker-compose.yml up -d --build`
    * `docker compose -f docker-compose.yml up -d --build --remove-orphans`
1. `docker-compose -f docker-compose.yml exec web_dev python manage.py migrate --noinput`
1. `docker compose exec web_dev python manage.py createsuperuser --email FlynntKnapp@email.app --username FlynntKnapp_dev`
1. `docker compose -f docker-compose.yml stop`
    * `docker compose -f docker-compose.yml down -v`
1. `docker compose -f docker-compose.yml start`

[Back to Top](#docker-compose)

### PROD `docker-compose.prod.yml` Commands

1. `docker compose -f docker-compose.prod.yml up -d --build`
    * `docker compose -f docker-compose.prod.yml up -d --build --remove-orphans`
1. `docker-compose -f docker-compose.prod.yml exec web_prod python manage.py migrate --noinput`
1. `docker compose exec web_prod python manage.py createsuperuser --email FlynntKnapp@email.app --username FlynntKnapp_prod`
1. `docker-compose -f docker-compose.prod.yml exec web_prod python manage.py collectstatic --no-input --clear`
1. `docker compose -f docker-compose.prod.yml stop`
    * Alt command to stop containers and remove volumes:
        * `docker compose -f docker-compose.prod.yml down -v`
1. `docker compose -f docker-compose.prod.yml start`

[Back to Top](#docker-compose)

## Simple `start` and `stop` Commands


* `docker compose -f docker-compose.prod.yml stop`
* `docker compose -f docker-compose.prod.yml start`

## Misc Commands

* `cp .env.dev.example .env.dev`
* `docker compose -f docker-compose.yml up -d --build`
* `docker compose -f docker-compose.prod.yml up -d --build`

* `docker compose exec web python manage.py migrate --noinput`
* `docker compose exec web python manage.py createsuperuser --email FlynntKnapp@email.app --username FlynntKnapp`

* <http://localhost:8000/admin/>
* `docker compose -f docker-compose.yml down -v`
* `docker compose -f docker-compose.prod.yml down -v`


* `docker compose -f docker-compose.yml up -d --build`
* `docker compose -f docker-compose.yml down -v`

[Back to Top](#docker-compose)

## Database Creation Commands

* `docker compose exec web python manage.py flush --no-input`
* `docker compose exec web python manage.py migrate`
* `docker compose exec web python manage.py createsuperuser --email FlynntKnapp@email.app --username FlynntKnapp`

[Back to Top](#docker-compose)

## Database Access Commands

* `docker compose exec db psql --username=docker_django_starter_dev_db_user --dbname=docker_django_starter_dev_db`
* `\l`
* `\c docker_django_starter_dev_db`
* `\dt`
* `\q`
* `docker volume inspect dockerdjangostarter-customuser_postgres_data`

[Back to Top](#docker-compose)

## Docker Compose Commands

* `docker compose ps`

[Back to Top](#docker-compose)
