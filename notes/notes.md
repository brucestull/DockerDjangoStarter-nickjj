# Notes

## Table of Contents

- [Notes](#notes)
  - [Table of Contents](#table-of-contents)
  - [Directory Structure](#directory-structure)
    - [Project Root](#project-root)
    - [`.github/`](#github)
    - [`assets/`](#assets)
    - [`bin/`](#bin)
    - [`public/`](#public)
    - [`public_collected/`](#public_collected)
    - [`src/`](#src)
    - [`.dockerignore`](#dockerignore)
    - [`.env.example`](#envexample)
    - [`.flake8`](#flake8)
    - [`.gitignore`](#gitignore)
    - [`CHANGELOG.md`](#changelogmd)
    - [`Dockerfile`](#dockerfile)
    - [`LICENSE`](#license)
    - [`README.md`](#readmemd)
    - [`docker-compose.yml`](#docker-composeyml)
    - [`local_things/`](#local_things)
    - [`notes/`](#notes-1)
    - [`pyproject.toml`](#pyprojecttoml)
    - [`requirements-lock.txt`](#requirements-locktxt)
    - [`requirements.txt`](#requirementstxt)
    - [`run/`](#run)

## Change Project Name

`./bin/rename-project doc_django DocDjango`

```bash
(mdn-local-library-tutorial-mine) flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .env.example
        modified:   CHANGELOG.md
        modified:   README.md
        modified:   assets/package.json
        modified:   bin/rename-project
        modified:   notes/notes.md
        modified:   src/config/asgi.py
        modified:   src/config/celery.py
        modified:   src/config/settings.py
        modified:   src/config/urls.py
        modified:   src/config/wsgi.py

no changes added to commit (use "git add" and/or "git commit -a")
(mdn-local-library-tutorial-mine) flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$
```

## Directory Structure

### Project Root

```bash
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$ tree -a -L 1
.
├── .dockerignore
├── .env
├── .env.example
├── .flake8
├── .git
├── .github
├── .gitignore
├── CHANGELOG.md
├── Dockerfile
├── LICENSE
├── README.md
├── assets
├── bin
├── docker-compose.yml
├── local_things
├── notes
├── public
├── public_collected
├── pyproject.toml
├── requirements-lock.txt
├── requirements.txt
├── run
└── src

9 directories, 14 files
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$
```
[back to table of contents](#table-of-contents)

### `.github/`

```bash
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$ tree .github
.github
├── docs
│   └── screenshot.jpg
└── workflows
    └── ci.yml

2 directories, 2 files
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$
```
[back to table of contents](#table-of-contents)

### `assets/`

```bash
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$ tree assets/
assets/
├── css
│   └── app.css
├── esbuild.config.mjs
├── js
│   └── app.js
├── package.json
├── postcss.config.js
├── static
│   ├── 502.html
│   ├── android-chrome-192x192.png
│   ├── android-chrome-512x512.png
│   ├── apple-touch-icon.png
│   ├── browserconfig.xml
│   ├── favicon-16x16.png
│   ├── favicon-32x32.png
│   ├── favicon.ico
│   ├── images
│   │   └── django.png
│   ├── maintenance.html
│   ├── mstile-150x150.png
│   ├── robots.txt
│   ├── safari-pinned-tab.svg
│   └── site.webmanifest
├── tailwind.config.js
└── yarn.lock

4 directories, 21 files
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$
```
[back to table of contents](#table-of-contents)

### `bin/`

```bash
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$ tree bin/
bin/
├── docker-entrypoint-web
├── pip3-install
└── rename-project

0 directories, 3 files
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$
```
[back to table of contents](#table-of-contents)

### `public/`

```bash
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$ tree public
public
├── 502.html
├── android-chrome-192x192.png
├── android-chrome-512x512.png
├── apple-touch-icon.png
├── browserconfig.xml
├── css
│   └── app.css
├── favicon-16x16.png
├── favicon-32x32.png
├── favicon.ico
├── images
│   └── django.png
├── js
│   ├── app.js
│   └── app.js.map
├── maintenance.html
├── mstile-150x150.png
├── robots.txt
├── safari-pinned-tab.svg
└── site.webmanifest

3 directories, 17 files
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$
```
[back to table of contents](#table-of-contents)

### `public_collected/`

```bash
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$ tree public_collected/
public_collected/

0 directories, 0 files
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$
```
[back to table of contents](#table-of-contents)

### `src/`

```bash
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$ tree src/
src/
├── __init__.py
├── config
│   ├── __init__.py
│   ├── asgi.py
│   ├── celery.py
│   ├── gunicorn.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── pages
│   ├── __init__.py
│   ├── apps.py
│   ├── templates
│   │   └── pages
│   │       └── home.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates
│   └── layouts
│       └── index.html
└── up
    ├── __init__.py
    ├── apps.py
    ├── tests.py
    ├── urls.py
    └── views.py

7 directories, 21 files
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$
```
[back to table of contents](#table-of-contents)

### `.dockerignore`

```bash
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$ cat .dockerignore
.git/
.pytest_cache/
__pycache__/
assets/node_modules/
public/
public_collected/

.coverage
.dockerignore
.env*
!.env.example
celerybeat-schedule
docker-compose.override.yml
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$
```
[back to table of contents](#table-of-contents)

### `.env.example`

```bash
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$ cat .env.example
# Default values are optimized for production to avoid having to configure
# much in production.
#
# However it should be easy to get going in development too. If you see an
# uncommented option that means it's either mandatory to set or it's being
# overwritten in development to make your life easier.

# Enable BuildKit by default:
#   https://docs.docker.com/develop/develop-images/build_enhancements
export DOCKER_BUILDKIT=1

# Rather than use the directory name, let's control the name of the project.
export COMPOSE_PROJECT_NAME=docker_django

# In development we want all services to start but in production you don't
# need the asset watchers to run since assets get built into the image.
#
# You can even choose not to run postgres and redis in prod if you plan to use
# managed cloud services. Everything "just works", even optional depends_on!
#export COMPOSE_PROFILES=postgres,redis,web,worker
export COMPOSE_PROFILES=postgres,redis,assets,web,worker

# If you're running native Linux and your uid:gid isn't 1000:1000 you can set
# these to match your values before you build your image. You can check what
# your uid:gid is by running `id` from your terminal.
#export UID=1000
#export GID=1000

# In development avoid writing out bytecode to __pycache__ directories.
#PYTHONDONTWRITEBYTECODE=
export PYTHONDONTWRITEBYTECODE=true

# You should generate a random string of 50+ characters for this value in prod.
# You can generate a secure secret by running: ./run secret
export SECRET_KEY=insecure_key_for_dev

# This should never be set to true in production but it should be enabled in dev.
#export DEBUG=false
export DEBUG=true

# Which Node environment is running? This should be "development" or "production".
#export NODE_ENV=production
export NODE_ENV=development

# A comma separated list of allowed hosts. In production this should be your
# domain name, such as "example.com,www.example.com" or ".example.com" to
# support both example.com and all sub-domains for your domain.
#
# This is being overwritten in development to support multiple Docker dev
# environments where you might be connecting over a local network IP address
# instead of localhost. You should not use "*" in production.
#export ALLOWED_HOSTS=".localhost,127.0.0.1,[::1]"
export ALLOWED_HOSTS="*"

# The bind port for gunicorn.
#
# Be warned that if you change this value you'll need to change 8000 in both
# your Dockerfile and in a few spots in docker-compose.yml due to the nature of
# how this value can be set (Docker Compose doesn't support nested ENV vars).
#export PORT=8000

# How many workers and threads should your app use? WEB_CONCURRENCY defaults
# to the server's CPU count * 2. That is a good starting point. In development
# it's a good idea to use 1 to avoid race conditions when debugging.
#export WEB_CONCURRENCY=
export WEB_CONCURRENCY=1
#export PYTHON_MAX_THREADS=1

# Do you want code reloading to work with the gunicorn app server?
#export WEB_RELOAD=false
export WEB_RELOAD=true

# You'll always want to set POSTGRES_USER and POSTGRES_PASSWORD since the
# postgres Docker image uses them for its default database user and password.
export POSTGRES_USER=docker_django
export POSTGRES_PASSWORD=password
#export POSTGRES_DB=docker_django
#export POSTGRES_HOST=postgres
#export POSTGRES_PORT=5432

# Connection string to Redis. This will be used for the cache back-end and for
# Celery. You can always split up your Redis servers later if needed.
#export REDIS_URL=redis://redis:6379/0

# You can choose between DEBUG, INFO, WARNING, ERROR, CRITICAL or FATAL.
# DEBUG tends to get noisy but it could be useful for troubleshooting.
#export CELERY_LOG_LEVEL=info

# Should Docker restart your containers if they go down in unexpected ways?
#export DOCKER_RESTART_POLICY=unless-stopped
export DOCKER_RESTART_POLICY=no

# What health check test command do you want to run? In development, having it
# curl your web server will result in a lot of log spam, so setting it to
# /bin/true is an easy way to make the health check do basically nothing.
#export DOCKER_WEB_HEALTHCHECK_TEST=curl localhost:8000/up
export DOCKER_WEB_HEALTHCHECK_TEST=/bin/true

# What ip:port should be published back to the Docker host for the app server?
# If you're using Docker Toolbox or a custom VM you can't use 127.0.0.1. This
# is being overwritten in dev to be compatible with more dev environments.
#
# If you have a port conflict because something else is using 8000 then you
# can either stop that process or change 8000 to be something else.
#
# Use the default in production to avoid having gunicorn directly accessible to
# the internet without assistance from a cloud based firewall.
#export DOCKER_WEB_PORT_FORWARD=127.0.0.1:8000
export DOCKER_WEB_PORT_FORWARD=8000

# What volume path should be used? In dev we want to volume mount everything
# so that we can develop our code without rebuilding our Docker images.
#export DOCKER_WEB_VOLUME=./public_collected:/app/public_collected
export DOCKER_WEB_VOLUME=.:/app

# What CPU and memory constraints will be added to your services? When left at
# 0, they will happily use as much as needed.
#export DOCKER_POSTGRES_CPUS=0
#export DOCKER_POSTGRES_MEMORY=0
#export DOCKER_REDIS_CPUS=0
#export DOCKER_REDIS_MEMORY=0
#export DOCKER_WEB_CPUS=0
#export DOCKER_WEB_MEMORY=0
#export DOCKER_WORKER_CPUS=0
#export DOCKER_WORKER_MEMORY=0
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$
```
[back to table of contents](#table-of-contents)

### `.flake8`

```bash
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$ cat .flake8
[flake8]
extend-ignore = E203, W503
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$
```
[back to table of contents](#table-of-contents)

### `CHANGELOG.md`

### `docker-compose.yml`

```bash
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$ cat docker-compose.yml
x-app: &default-app
  build:
    context: "."
    target: "app"
    args:
      - "UID=${UID:-1000}"
      - "GID=${GID:-1000}"
      - "DEBUG=${DEBUG:-false}"
      - "NODE_ENV=${NODE_ENV:-production}"
  depends_on:
    - "postgres"
    - "redis"
  env_file:
    - ".env"
  restart: "${DOCKER_RESTART_POLICY:-unless-stopped}"
  stop_grace_period: "3s"
  tty: true
  volumes:
    - "${DOCKER_WEB_VOLUME:-./public_collected:/app/public_collected}"

x-assets: &default-assets
  build:
    context: "."
    target: "assets"
    args:
      - "UID=${UID:-1000}"
      - "GID=${GID:-1000}"
      - "NODE_ENV=${NODE_ENV:-production}"
  env_file:
    - ".env"
  profiles: ["assets"]
  restart: "${DOCKER_RESTART_POLICY:-unless-stopped}"
  stop_grace_period: "0"
  tty: true
  volumes:
    - ".:/app"

services:
  postgres:
    deploy:
      resources:
        limits:
          cpus: "${DOCKER_POSTGRES_CPUS:-0}"
          memory: "${DOCKER_POSTGRES_MEMORY:-0}"
    environment:
      POSTGRES_USER: "${POSTGRES_USER}"
      POSTGRES_PASSWORD: "${POSTGRES_PASSWORD}"
      # POSTGRES_DB: "${POSTGRES_DB}"
    image: "postgres:15.3-bullseye"
    profiles: ["postgres"]
    restart: "${DOCKER_RESTART_POLICY:-unless-stopped}"
    stop_grace_period: "3s"
    volumes:
      - "postgres:/var/lib/postgresql/data"

  redis:
    deploy:
      resources:
        limits:
          cpus: "${DOCKER_REDIS_CPUS:-0}"
          memory: "${DOCKER_REDIS_MEMORY:-0}"
    image: "redis:7.0.11-bullseye"
    profiles: ["redis"]
    restart: "${DOCKER_RESTART_POLICY:-unless-stopped}"
    stop_grace_period: "3s"
    volumes:
      - "redis:/data"

  web:
    <<: *default-app
    deploy:
      resources:
        limits:
          cpus: "${DOCKER_WEB_CPUS:-0}"
          memory: "${DOCKER_WEB_MEMORY:-0}"
    healthcheck:
      test: "${DOCKER_WEB_HEALTHCHECK_TEST:-curl localhost:8000/up}"
      interval: "60s"
      timeout: "3s"
      start_period: "5s"
      retries: 3
    ports:
      - "${DOCKER_WEB_PORT_FORWARD:-127.0.0.1:8000}:${PORT:-8000}"
    profiles: ["web"]

  worker:
    <<: *default-app
    command: celery -A config worker -l "${CELERY_LOG_LEVEL:-info}"
    entrypoint: []
    deploy:
      resources:
        limits:
          cpus: "${DOCKER_WORKER_CPUS:-0}"
          memory: "${DOCKER_WORKER_MEMORY:-0}"
    profiles: ["worker"]

  js:
    <<: *default-assets
    command: "../run yarn:build:js"

  css:
    <<: *default-assets
    command: "../run yarn:build:css"

volumes:
  postgres: {}
  redis: {}
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$
```
[back to table of contents](#table-of-contents)

### `Dockerfile`

```bash
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$ cat Dockerfile
FROM node:18.15.0-bullseye-slim AS assets
LABEL maintainer="Nick Janetakis <nick.janetakis@gmail.com>"

WORKDIR /app/assets

ARG UID=1000
ARG GID=1000

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean \
  && groupmod -g "${GID}" node && usermod -u "${UID}" -g "${GID}" node \
  && mkdir -p /node_modules && chown node:node -R /node_modules /app

USER node

COPY --chown=node:node assets/package.json assets/*yarn* ./

RUN yarn install && yarn cache clean

ARG NODE_ENV="production"
ENV NODE_ENV="${NODE_ENV}" \
    PATH="${PATH}:/node_modules/.bin" \
    USER="node"

COPY --chown=node:node . ..

RUN if [ "${NODE_ENV}" != "development" ]; then \
  ../run yarn:build:js && ../run yarn:build:css; else mkdir -p /app/public; fi

CMD ["bash"]

###############################################################################

FROM python:3.11.4-slim-bullseye AS app
LABEL maintainer="Nick Janetakis <nick.janetakis@gmail.com>"

WORKDIR /app

ARG UID=1000
ARG GID=1000

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential curl libpq-dev \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean \
  && groupadd -g "${GID}" python \
  && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" python \
  && mkdir -p /public_collected public \
  && chown python:python -R /public_collected /app

USER python

COPY --chown=python:python requirements*.txt ./
COPY --chown=python:python bin/ ./bin

RUN chmod 0755 bin/* && bin/pip3-install

ARG DEBUG="false"
ENV DEBUG="${DEBUG}" \
    PYTHONUNBUFFERED="true" \
    PYTHONPATH="." \
    PATH="${PATH}:/home/python/.local/bin" \
    USER="python"

COPY --chown=python:python --from=assets /app/public /public
COPY --chown=python:python . .

WORKDIR /app/src

RUN if [ "${DEBUG}" = "false" ]; then \
  SECRET_KEY=dummyvalue python3 manage.py collectstatic --no-input; \
    else mkdir -p /app/public_collected; fi

ENTRYPOINT ["/app/bin/docker-entrypoint-web"]

EXPOSE 8000

CMD ["gunicorn", "-c", "python:config.gunicorn", "config.wsgi"]
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$
```
[back to table of contents](#table-of-contents)

### `pyproject.toml`

```bash
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$ cat pyproject.toml
[tool.black]
line-length = 79

[tool.isort]
profile = "black"
line_length = 79
force_single_line = true
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$
```
[back to table of contents](#table-of-contents)

### `requirements.txt`

```bash
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$ cat requirements.txt
Django==4.2.2
gunicorn==20.1.0
whitenoise==6.4.0
django-debug-toolbar==4.1.0

psycopg==3.1.9

redis==4.5.5
celery==5.3.0

flake8==6.0.0
isort==5.12.0
black==23.3.0
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$
```
[back to table of contents](#table-of-contents)

### `run`

```bash
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$ cat run
#!/usr/bin/env bash

set -o errexit
set -o pipefail

DC="${DC:-exec}"

# If we're running in CI we need to disable TTY allocation for docker compose
# commands that enable it by default, such as exec and run.
TTY=""
if [[ ! -t 1 ]]; then
  TTY="-T"
fi

# -----------------------------------------------------------------------------
# Helper functions start with _ and aren't listed in this script's help menu.
# -----------------------------------------------------------------------------

function _dc {
  docker compose "${DC}" ${TTY} "${@}"
}

function _build_run_down {
  docker compose build
  docker compose run ${TTY} "${@}"
  docker compose down
}

# -----------------------------------------------------------------------------

function cmd {
  # Run any command you want in the web container
  _dc web "${@}"
}

function manage {
  # Run any manage.py commands

  # We need to collectstatic before we run our tests.
  if [ "${1-''}" == "test" ]; then
    cmd python3 manage.py collectstatic --no-input
  fi

  cmd python3 manage.py "${@}"
}

function lint:dockerfile {
  # Lint Dockerfile
  docker container run --rm -i \
    hadolint/hadolint hadolint --ignore DL3008 -t style "${@}" - < Dockerfile
}

function lint {
  # Lint Python code
  cmd flake8 "${@}"
}

function format:imports {
  # Sort Python imports
  cmd isort . "${@}"
}

function format {
  # Format Python code
  cmd black . "${@}"
}

function quality {
  # Perform all code quality commands together
  format:imports
  format
  lint
}

function secret {
  # Generate a random secret that can be used for your SECRET_KEY and more
  cmd python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
}

function shell {
  # Start a shell session in the web container
  cmd bash "${@}"
}

function psql {
  # Connect to PostgreSQL
  # shellcheck disable=SC1091
  . .env
 _dc postgres psql -U "${POSTGRES_USER}" "${@}"
}

function redis-cli {
  # Connect to Redis
  _dc redis redis-cli "${@}"
}

function pip3:install {
  # Install pip3 dependencies and write lock file
  _build_run_down web bash -c "cd .. && bin/pip3-install"
}

function pip3:outdated {
  # List any installed packages that are outdated
  cmd pip3 list --outdated
}

function yarn:install {
  # Install yarn dependencies and write lock file
  _build_run_down js yarn install
}

function yarn:outdated {
  # List any installed packages that are outdated
  _dc js yarn outdated
}

function yarn:build:js {
  # Build JS assets, this is meant to be run from within the assets container
  mkdir -p ../public/js
  node esbuild.config.mjs
}

function yarn:build:css {
  # Build CSS assets, this is meant to be run from within the assets container
  local args=()

  if [ "${NODE_ENV:-}" == "production" ]; then
    args=(--minify)
  else
    args=(--watch)
  fi

  mkdir -p ../public/css
  DEBUG=0 tailwindcss --postcss -i css/app.css -o ../public/css/app.css "${args[@]}"
}

function clean {
  # Remove cache and other machine generates files
  rm -rf public/*.* public/admin public/js public/css public/images public/fonts \
    public_collected/*.* public_collected/admin public_collected/js \
    public_collected/css public_collected/images public_collected/fonts \
    .pytest_cache/ .coverage celerybeat-schedule

  touch public/.keep public_collected/.keep
}

function ci:install-deps {
  # Install Continuous Integration (CI) dependencies
  sudo apt-get install -y curl shellcheck
  sudo curl \
    -L https://raw.githubusercontent.com/nickjj/wait-until/v0.2.0/wait-until \
    -o /usr/local/bin/wait-until && sudo chmod +x /usr/local/bin/wait-until
}

function ci:test {
  # Execute Continuous Integration (CI) pipeline
  #
  # It's expected that your CI environment has these tools available:
  #   - https://github.com/koalaman/shellcheck
  #   - https://github.com/nickjj/wait-until
  shellcheck run bin/*
  lint:dockerfile "${@}"

  cp --no-clobber .env.example .env

  docker compose build
  docker compose up -d

  # shellcheck disable=SC1091
  . .env
  wait-until "docker compose exec -T \
    -e PGPASSWORD=${POSTGRES_PASSWORD} postgres \
    psql -U ${POSTGRES_USER} ${POSTGRES_USER} -c 'SELECT 1'"

  docker compose logs

  lint "${@}"
  format:imports --check
  format --check
  manage migrate
  manage test
}

function help {
  printf "%s <task> [args]\n\nTasks:\n" "${0}"

  compgen -A function | grep -v "^_" | cat -n

  printf "\nExtended help:\n  Each task has comments for general usage\n"
}

# This idea is heavily inspired by: https://github.com/adriancooney/Taskfile
TIMEFORMAT=$'\nTask completed in %3lR'
time "${@:-help}"
flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$
```
[back to table of contents](#table-of-contents)


[back to table of contents](#table-of-contents)
