# Notes 02

## Table of Contents

- [Running Commands in the Container](#running-commands-in-the-docker-container)
- [Building, Running, Testing, and Stopping the Docker Container](#building-running-testing-and-stopping-the-docker-container)
- [Getting a List of Docker Containers, Images, and Volumes](#getting-a-list-of-docker-containers-images-and-volumes)
- [Inspecting the Docker Volumes](#inspecting-the-docker-volumes)

## Building, Running, Testing, and Stopping the Docker Container

1. `docker compose up --build`:

    ```bash
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$ docker compose up --build
    [+] Running 21/21
    ✔ postgres 13 layers [⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿]      0B/0B      Pulled                                                                                                                                          11.3s 
    ✔ 1d5252f66ea9 Pull complete                                                                                                                                                                        3.4s 
    ✔ 024ad9bec3dc Pull complete                                                                                                                                                                        2.1s 
    ✔ 5fd873abf5f6 Pull complete                                                                                                                                                                        2.5s 
    ✔ ffe9a34510c5 Pull complete                                                                                                                                                                        2.7s 
    ✔ 66791212fee3 Pull complete                                                                                                                                                                        3.6s 
    ✔ d6c53d590081 Pull complete                                                                                                                                                                        3.5s 
    ✔ dc1d320348fe Pull complete                                                                                                                                                                        3.7s 
    ✔ 287863565429 Pull complete                                                                                                                                                                        3.8s 
    ✔ 1cd0c71c4f10 Pull complete                                                                                                                                                                        6.9s 
    ✔ 537879435ed0 Pull complete                                                                                                                                                                        4.0s 
    ✔ b78b89244e3d Pull complete                                                                                                                                                                        4.2s 
    ✔ c5376b574c7a Pull complete                                                                                                                                                                        4.5s 
    ✔ 4fd142e0edec Pull complete                                                                                                                                                                        4.6s 
    ✔ redis 6 layers [⣿⣿⣿⣿⣿⣿]      0B/0B      Pulled                                                                                                                                                      5.6s 
    ✔ 759700526b78 Pull complete                                                                                                                                                                        1.8s 
    ✔ eb5c5a6a60f0 Pull complete                                                                                                                                                                        0.4s 
    ✔ 12e7d88aa422 Pull complete                                                                                                                                                                        0.5s 
    ✔ 8f4ed3de3123 Pull complete                                                                                                                                                                        1.8s 
    ✔ 0705c505f99b Pull complete                                                                                                                                                                        1.2s 
    ✔ d943febfd435 Pull complete                                                                                                                                                                        1.9s 
    [+] Building 2.6s (39/54)                                                                                                                                                                    docker:default
    => [css internal] load build definition from Dockerfile                                                                                                                                               0.0s
    => => transferring dockerfile: 2.20kB                                                                                                                                                                 0.0s
    => [css internal] load .dockerignore                                                                                                                                                                  0.0s
    => => transferring context: 216B                                                                                                                                                                      0.0s
    => [web internal] load build definition from Dockerfile                                                                                                                                               0.0s
    => => transferring dockerfile: 2.20kB                                                                                                                                                                 0.0s
    => [web internal] load .dockerignore                                                                                                                                                                  0.0s
    => => transferring context: 216B                                                                                                                                                                      0.0s
    => [js internal] load build definition from Dockerfile                                                                                                                                                0.0s
    => => transferring dockerfile: 2.20kB                                                                                                                                                                 0.0s
    => [js internal] load .dockerignore                                                                                                                                                                   0.0s
    => => transferring context: 216B                                                                                                                                                                      0.0s
    => [css internal] load metadata for docker.io/library/node:18.15.0-bullseye-slim                                                                                                                      0.5s
    => [worker internal] load metadata for docker.io/library/python:3.11.4-slim-bullseye                                                                                                                  0.9s
    => [worker internal] load .dockerignore                                                                                                                                                               0.0s
    => => transferring context: 216B                                                                                                                                                                      0.0s
    => [worker internal] load build definition from Dockerfile                                                                                                                                            0.0s
    => => transferring dockerfile: 2.20kB                                                                                                                                                                 0.0s
    => [web assets 1/7] FROM docker.io/library/node:18.15.0-bullseye-slim@sha256:639e94182196dccc83a45224a10d2a3cb4139c0e3d05194b64d6587ce2919e8c                                                         0.0s
    => [css internal] load build context                                                                                                                                                                  0.0s
    => => transferring context: 59.39kB                                                                                                                                                                   0.0s
    => [js internal] load build context                                                                                                                                                                   0.0s
    => => transferring context: 59.39kB                                                                                                                                                                   0.0s
    => CACHED [web assets 2/7] WORKDIR /app/assets                                                                                                                                                        0.0s
    => CACHED [web assets 3/7] RUN apt-get update   && apt-get install -y --no-install-recommends build-essential   && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man   && apt-get clean   &&  0.0s
    => CACHED [js assets 4/7] COPY --chown=node:node assets/package.json assets/*yarn* ./                                                                                                                 0.0s
    => CACHED [js assets 5/7] RUN yarn install && yarn cache clean                                                                                                                                        0.0s
    => [js assets 6/7] COPY --chown=node:node . ..                                                                                                                                                        0.8s
    => [worker internal] load build context                                                                                                                                                               0.1s
    => => transferring context: 59.39kB                                                                                                                                                                   0.0s
    => [web app  1/10] FROM docker.io/library/python:3.11.4-slim-bullseye@sha256:40319d0a897896e746edf877783ef39685d44e90e1e6de8d964d0382df0d4952                                                         0.0s
    => [web internal] load build context                                                                                                                                                                  0.1s
    => => transferring context: 59.39kB                                                                                                                                                                   0.0s
    => [js assets 7/7] RUN if [ "development" != "development" ]; then   ../run yarn:build:js && ../run yarn:build:css; else mkdir -p /app/public; fi                                                     0.4s
    => [css] exporting to image                                                                                                                                                                           0.1s
    => => exporting layers                                                                                                                                                                                0.1s
    => => writing image sha256:e54d3a92169d41c31a7b5ac3d80dcc0f83ca5c6550ea588cde54cd8ba2b5da4a                                                                                                           0.0s
    => => naming to docker.io/library/d_django_starter-css                                                                                                                                                0.0s
    => [js] exporting to image                                                                                                                                                                            0.1s
    => => exporting layers                                                                                                                                                                                0.0s
    => => writing image sha256:4adc138ddd479c15f417ad8ed1503ed3187d3c8b0a2c7ef02fa438154d96f20f                                                                                                           0.0s
    => => naming to docker.io/library/d_django_starter-js                                                                                                                                                 0.0s
    => CACHED [web app  2/10] WORKDIR /app                                                                                                                                                                0.0s
    => CACHED [web app  3/10] RUN apt-get update   && apt-get install -y --no-install-recommends build-essential curl libpq-dev   && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man   && apt-  0.0s
    => CACHED [web app  4/10] COPY --chown=python:python requirements*.txt ./                                                                                                                             0.0s
    => CACHED [web app  5/10] COPY --chown=python:python bin/ ./bin                                                                                                                                       0.0s
    => CACHED [web app  6/10] RUN chmod 0755 bin/* && bin/pip3-install                                                                                                                                    0.0s
    => CACHED [web assets 4/7] COPY --chown=node:node assets/package.json assets/*yarn* ./                                                                                                                0.0s
    => CACHED [web assets 5/7] RUN yarn install && yarn cache clean                                                                                                                                       0.0s
    => CACHED [web assets 6/7] COPY --chown=node:node . ..                                                                                                                                                0.0s
    => CACHED [web assets 7/7] RUN if [ "development" != "development" ]; then   ../run yarn:build:js && ../run yarn:build:css; else mkdir -p /app/public; fi                                             0.0s
    => CACHED [web app  7/10] COPY --chown=python:python --from=assets /app/public /public                                                                                                                0.0s
    => [web app  8/10] COPY --chown=python:python . .                                                                                                                                                     0.2s
    => [web app  9/10] WORKDIR /app/src                                                                                                                                                                   0.0s
    => [web app 10/10] RUN if [ "true" = "false" ]; then   SECRET_KEY=dummyvalue python3 manage.py collectstatic --no-input;     else mkdir -p /app/public_collected; fi                                  0.4s
    => [worker] exporting to image                                                                                                                                                                        0.1s
    => => exporting layers                                                                                                                                                                                0.1s
    => => writing image sha256:86cb2df224cf520ba6b5947e1f76e3750b6592f74dba3ed005d4f1ff01ee56b8                                                                                                           0.0s
    => => naming to docker.io/library/d_django_starter-worker                                                                                                                                             0.0s
    => [web] exporting to image                                                                                                                                                                           0.1s
    => => exporting layers                                                                                                                                                                                0.1s
    => => writing image sha256:531f7db14f242934ae3c0a2bdddcacf75bc0f766182dbe3b6fe0bfd5d49db478                                                                                                           0.0s
    => => naming to docker.io/library/d_django_starter-web                                                                                                                                                0.0s
    [+] Running 9/9
    ✔ Network d_django_starter_default       Created                                                                                                                                                      0.2s 
    ✔ Volume "d_django_starter_redis"        Created                                                                                                                                                      0.0s 
    ✔ Volume "d_django_starter_postgres"     Created                                                                                                                                                      0.0s 
    ✔ Container d_django_starter-postgres-1  Created                                                                                                                                                      0.1s 
    ✔ Container d_django_starter-js-1        Created                                                                                                                                                      0.1s 
    ✔ Container d_django_starter-css-1       Created                                                                                                                                                      0.1s 
    ✔ Container d_django_starter-redis-1     Created                                                                                                                                                      0.1s 
    ✔ Container d_django_starter-worker-1    Created                                                                                                                                                      0.1s 
    ✔ Container d_django_starter-web-1       Created                                                                                                                                                      0.1s 
    Attaching to d_django_starter-css-1, d_django_starter-js-1, d_django_starter-postgres-1, d_django_starter-redis-1, d_django_starter-web-1, d_django_starter-worker-1
    d_django_starter-redis-1     | 1:C 30 Sep 2023 07:49:24.052 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
    d_django_starter-redis-1     | 1:C 30 Sep 2023 07:49:24.052 # Redis version=7.0.11, bits=64, commit=00000000, modified=0, pid=1, just started
    d_django_starter-redis-1     | 1:C 30 Sep 2023 07:49:24.052 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
    d_django_starter-redis-1     | 1:M 30 Sep 2023 07:49:24.053 * monotonic clock: POSIX clock_gettime
    d_django_starter-redis-1     | 1:M 30 Sep 2023 07:49:24.053 * Running mode=standalone, port=6379.
    d_django_starter-redis-1     | 1:M 30 Sep 2023 07:49:24.053 # Server initialized
    d_django_starter-redis-1     | 1:M 30 Sep 2023 07:49:24.053 # WARNING Memory overcommit must be enabled! Without it, a background save or replication may fail under low memory condition. Being disabled, it can can also cause failures without low memory condition, see https://github.com/jemalloc/jemalloc/issues/1328. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
    d_django_starter-redis-1     | 1:M 30 Sep 2023 07:49:24.053 * Ready to accept connections
    d_django_starter-postgres-1  | The files belonging to this database system will be owned by user "postgres".
    d_django_starter-postgres-1  | This user must also own the server process.
    d_django_starter-postgres-1  | 
    d_django_starter-postgres-1  | The database cluster will be initialized with locale "en_US.utf8".
    d_django_starter-postgres-1  | The default database encoding has accordingly been set to "UTF8".
    d_django_starter-postgres-1  | The default text search configuration will be set to "english".
    d_django_starter-postgres-1  | 
    d_django_starter-postgres-1  | Data page checksums are disabled.
    d_django_starter-postgres-1  | 
    d_django_starter-postgres-1  | fixing permissions on existing directory /var/lib/postgresql/data ... ok
    d_django_starter-postgres-1  | creating subdirectories ... ok
    d_django_starter-postgres-1  | selecting dynamic shared memory implementation ... posix
    d_django_starter-postgres-1  | selecting default max_connections ... 100
    d_django_starter-postgres-1  | selecting default shared_buffers ... 128MB
    d_django_starter-postgres-1  | selecting default time zone ... Etc/UTC
    d_django_starter-postgres-1  | creating configuration files ... ok
    d_django_starter-js-1        | [watch] build finished, watching for changes...
    d_django_starter-postgres-1  | running bootstrap script ... ok
    d_django_starter-postgres-1  | performing post-bootstrap initialization ... ok
    d_django_starter-css-1       | Browserslist: caniuse-lite is outdated. Please run:
    d_django_starter-css-1       |   npx update-browserslist-db@latest
    d_django_starter-css-1       |   Why you should do it regularly: https://github.com/browserslist/update-db#readme
    d_django_starter-css-1       | 
    d_django_starter-css-1       | Rebuilding...
    d_django_starter-css-1       | 
    d_django_starter-css-1       | Done in 266ms.
    d_django_starter-postgres-1  | syncing data to disk ... ok
    d_django_starter-postgres-1  | 
    d_django_starter-postgres-1  | 
    d_django_starter-postgres-1  | Success. You can now start the database server using:
    d_django_starter-postgres-1  | 
    d_django_starter-postgres-1  |     pg_ctl -D /var/lib/postgresql/data -l logfile start
    d_django_starter-postgres-1  | 
    d_django_starter-postgres-1  | initdb: warning: enabling "trust" authentication for local connections
    d_django_starter-postgres-1  | initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.
    d_django_starter-postgres-1  | waiting for server to start....2023-09-30 07:49:25.307 UTC [48] LOG:  starting PostgreSQL 15.3 (Debian 15.3-1.pgdg110+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit
    d_django_starter-postgres-1  | 2023-09-30 07:49:25.309 UTC [48] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
    d_django_starter-postgres-1  | 2023-09-30 07:49:25.315 UTC [51] LOG:  database system was shut down at 2023-09-30 07:49:24 UTC
    d_django_starter-postgres-1  | 2023-09-30 07:49:25.319 UTC [48] LOG:  database system is ready to accept connections
    d_django_starter-postgres-1  |  done
    d_django_starter-postgres-1  | server started
    d_django_starter-postgres-1  | CREATE DATABASE
    d_django_starter-postgres-1  | 
    d_django_starter-postgres-1  | 
    d_django_starter-postgres-1  | /usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*
    d_django_starter-postgres-1  | 
    d_django_starter-postgres-1  | 2023-09-30 07:49:25.484 UTC [48] LOG:  received fast shutdown request
    d_django_starter-postgres-1  | waiting for server to shut down....2023-09-30 07:49:25.486 UTC [48] LOG:  aborting any active transactions
    d_django_starter-postgres-1  | 2023-09-30 07:49:25.487 UTC [48] LOG:  background worker "logical replication launcher" (PID 54) exited with exit code 1
    d_django_starter-postgres-1  | 2023-09-30 07:49:25.487 UTC [49] LOG:  shutting down
    d_django_starter-postgres-1  | 2023-09-30 07:49:25.489 UTC [49] LOG:  checkpoint starting: shutdown immediate
    d_django_starter-postgres-1  | 2023-09-30 07:49:25.568 UTC [49] LOG:  checkpoint complete: wrote 918 buffers (5.6%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.015 s, sync=0.054 s, total=0.081 s; sync files=250, longest=0.003 s, average=0.001 s; distance=4217 kB, estimate=4217 kB
    d_django_starter-postgres-1  | 2023-09-30 07:49:25.571 UTC [48] LOG:  database system is shut down
    d_django_starter-postgres-1  |  done
    d_django_starter-postgres-1  | server stopped
    d_django_starter-postgres-1  | 
    d_django_starter-postgres-1  | PostgreSQL init process complete; ready for start up.
    d_django_starter-postgres-1  | 
    d_django_starter-postgres-1  | 2023-09-30 07:49:25.600 UTC [1] LOG:  starting PostgreSQL 15.3 (Debian 15.3-1.pgdg110+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit
    d_django_starter-postgres-1  | 2023-09-30 07:49:25.600 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
    d_django_starter-postgres-1  | 2023-09-30 07:49:25.600 UTC [1] LOG:  listening on IPv6 address "::", port 5432
    d_django_starter-postgres-1  | 2023-09-30 07:49:25.604 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
    d_django_starter-postgres-1  | 2023-09-30 07:49:25.609 UTC [64] LOG:  database system was shut down at 2023-09-30 07:49:25 UTC
    d_django_starter-postgres-1  | 2023-09-30 07:49:25.613 UTC [1] LOG:  database system is ready to accept connections
    d_django_starter-web-1       | [2023-09-30 07:49:25 +0000] [1] [INFO] Starting gunicorn 20.1.0
    d_django_starter-web-1       | [2023-09-30 07:49:25 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
    d_django_starter-web-1       | [2023-09-30 07:49:25 +0000] [1] [INFO] Using worker: sync
    d_django_starter-web-1       | [2023-09-30 07:49:25 +0000] [8] [INFO] Booting worker with pid: 8
    d_django_starter-worker-1    |  
    d_django_starter-worker-1    |  -------------- celery@6324db6e8415 v5.3.0 (emerald-rush)
    d_django_starter-worker-1    | --- ***** ----- 
    d_django_starter-worker-1    | -- ******* ---- Linux-5.15.90.1-microsoft-standard-WSL2-x86_64-with-glibc2.31 2023-09-30 03:49:26
    d_django_starter-worker-1    | - *** --- * --- 
    d_django_starter-worker-1    | - ** ---------- [config]
    d_django_starter-worker-1    | - ** ---------- .> app:         d_django_starter:0x7f99d15f7690
    d_django_starter-worker-1    | - ** ---------- .> transport:   redis://redis:6379/0
    d_django_starter-worker-1    | - ** ---------- .> results:     redis://redis:6379/0
    d_django_starter-worker-1    | - *** --- * --- .> concurrency: 8 (prefork)
    d_django_starter-worker-1    | -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
    d_django_starter-worker-1    | --- ***** ----- 
    d_django_starter-worker-1    |  -------------- [queues]
    d_django_starter-worker-1    |                 .> celery           exchange=celery(direct) key=celery
    d_django_starter-worker-1    |                 
    d_django_starter-worker-1    | 
    d_django_starter-worker-1    | [tasks]
    d_django_starter-worker-1    | 
    d_django_starter-worker-1    | 
    d_django_starter-worker-1    | [2023-09-30 03:49:26,938: WARNING/MainProcess] /home/python/.local/lib/python3.11/site-packages/celery/worker/consumer/consumer.py:498: CPendingDeprecationWarning: The broker_connection_retry configuration setting will no longer determine
    d_django_starter-worker-1    | whether broker connection retries are made during startup in Celery 6.0 and above.
    d_django_starter-worker-1    | If you wish to retain the existing behavior for retrying connections on startup,
    d_django_starter-worker-1    | you should set broker_connection_retry_on_startup to True.
    d_django_starter-worker-1    |   warnings.warn(
    d_django_starter-worker-1    | 
    d_django_starter-worker-1    | [2023-09-30 03:49:26,948: INFO/MainProcess] Connected to redis://redis:6379/0
    d_django_starter-worker-1    | [2023-09-30 03:49:26,949: WARNING/MainProcess] /home/python/.local/lib/python3.11/site-packages/celery/worker/consumer/consumer.py:498: CPendingDeprecationWarning: The broker_connection_retry configuration setting will no longer determine
    d_django_starter-worker-1    | whether broker connection retries are made during startup in Celery 6.0 and above.
    d_django_starter-worker-1    | If you wish to retain the existing behavior for retrying connections on startup,
    d_django_starter-worker-1    | you should set broker_connection_retry_on_startup to True.
    d_django_starter-worker-1    |   warnings.warn(
    d_django_starter-worker-1    | 
    d_django_starter-worker-1    | [2023-09-30 03:49:26,952: INFO/MainProcess] mingle: searching for neighbors
    d_django_starter-worker-1    | [2023-09-30 03:49:27,960: INFO/MainProcess] mingle: all alone
    d_django_starter-worker-1    | [2023-09-30 03:49:27,969: INFO/MainProcess] celery@6324db6e8415 ready.
    ```

1. `./run manage migrate`:

    ```bash
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$ ./run manage migrate
    Operations to perform:
    Apply all migrations: accounts, admin, auth, contenttypes, sessions
    Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0001_initial... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying auth.0009_alter_user_last_name_max_length... OK
    Applying auth.0010_alter_group_name_max_length... OK
    Applying auth.0011_update_proxy_permissions... OK
    Applying auth.0012_alter_user_first_name_max_length... OK
    Applying accounts.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying admin.0003_logentry_add_action_flag_choices... OK
    Applying sessions.0001_initial... OK

    Task completed in 0m1.674s
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$
    ```

1. `./run manage createsuperuser --email FlynntKnapp@email.app --username FlynntKnapp`:

    ```bash
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$ ./run manage createsuperuser --email FlynntKnapp@email.app --username FlynntKnapp
    Password: 
    Password (again): 
    Superuser created successfully.

    Task completed in 0m7.178s
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$
    ```

1. `docker compose down --remove-orphans`:

    ```bash
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$ docker compose down --remove-orphans
    [+] Running 7/7
    ✔ Container d_django_starter-css-1       Removed                                                                                                               0.6s 
    ✔ Container d_django_starter-web-1       Removed                                                                                                               0.8s 
    ✔ Container d_django_starter-worker-1    Removed                                                                                                               2.3s 
    ✔ Container d_django_starter-js-1        Removed                                                                                                               0.4s 
    ✔ Container d_django_starter-postgres-1  Removed                                                                                                               0.5s 
    ✔ Container d_django_starter-redis-1     Removed                                                                                                               0.7s 
    ✔ Network d_django_starter_default       Removed                                                                                                               0.3s 
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$
    ```

1. `docker compose up`:

    ```bash
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$ docker compose up
    [+] Running 7/7
    ✔ Network d_django_starter_default       Created                                                                                                                              0.0s 
    ✔ Container d_django_starter-css-1       Created                                                                                                                              0.1s 
    ✔ Container d_django_starter-js-1        Created                                                                                                                              0.1s 
    ✔ Container d_django_starter-redis-1     Created                                                                                                                              0.1s 
    ✔ Container d_django_starter-postgres-1  Created                                                                                                                              0.1s 
    ✔ Container d_django_starter-web-1       Created                                                                                                                              0.1s 
    ✔ Container d_django_starter-worker-1    Created                                                                                                                              0.1s 
    Attaching to d_django_starter-css-1, d_django_starter-js-1, d_django_starter-postgres-1, d_django_starter-redis-1, d_django_starter-web-1, d_django_starter-worker-1
    d_django_starter-postgres-1  | 
    d_django_starter-postgres-1  | PostgreSQL Database directory appears to contain a database; Skipping initialization
    d_django_starter-postgres-1  | 
    d_django_starter-js-1        | [watch] build finished, watching for changes...
    d_django_starter-redis-1     | 1:C 30 Sep 2023 08:22:15.215 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
    d_django_starter-redis-1     | 1:C 30 Sep 2023 08:22:15.215 # Redis version=7.0.11, bits=64, commit=00000000, modified=0, pid=1, just started
    d_django_starter-redis-1     | 1:C 30 Sep 2023 08:22:15.215 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
    d_django_starter-redis-1     | 1:M 30 Sep 2023 08:22:15.216 * monotonic clock: POSIX clock_gettime
    d_django_starter-redis-1     | 1:M 30 Sep 2023 08:22:15.218 * Running mode=standalone, port=6379.
    d_django_starter-redis-1     | 1:M 30 Sep 2023 08:22:15.218 # Server initialized
    d_django_starter-redis-1     | 1:M 30 Sep 2023 08:22:15.218 # WARNING Memory overcommit must be enabled! Without it, a background save or replication may fail under low memory condition. Being disabled, it can can also cause failures without low memory condition, see https://github.com/jemalloc/jemalloc/issues/1328. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
    d_django_starter-redis-1     | 1:M 30 Sep 2023 08:22:15.219 * Loading RDB produced by version 7.0.11
    d_django_starter-redis-1     | 1:M 30 Sep 2023 08:22:15.219 * RDB age 138 seconds
    d_django_starter-redis-1     | 1:M 30 Sep 2023 08:22:15.219 * RDB memory usage when created 1.18 Mb
    d_django_starter-redis-1     | 1:M 30 Sep 2023 08:22:15.219 * Done loading RDB, keys loaded: 1, keys expired: 0.
    d_django_starter-redis-1     | 1:M 30 Sep 2023 08:22:15.219 * DB loaded from disk: 0.001 seconds
    d_django_starter-redis-1     | 1:M 30 Sep 2023 08:22:15.219 * Ready to accept connections
    d_django_starter-postgres-1  | 2023-09-30 08:22:15.295 UTC [1] LOG:  starting PostgreSQL 15.3 (Debian 15.3-1.pgdg110+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit
    d_django_starter-postgres-1  | 2023-09-30 08:22:15.296 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
    d_django_starter-postgres-1  | 2023-09-30 08:22:15.296 UTC [1] LOG:  listening on IPv6 address "::", port 5432
    d_django_starter-postgres-1  | 2023-09-30 08:22:15.299 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
    d_django_starter-postgres-1  | 2023-09-30 08:22:15.305 UTC [30] LOG:  database system was shut down at 2023-09-30 08:19:57 UTC
    d_django_starter-postgres-1  | 2023-09-30 08:22:15.317 UTC [1] LOG:  database system is ready to accept connections
    d_django_starter-css-1       | Browserslist: caniuse-lite is outdated. Please run:
    d_django_starter-css-1       |   npx update-browserslist-db@latest
    d_django_starter-css-1       |   Why you should do it regularly: https://github.com/browserslist/update-db#readme
    d_django_starter-css-1       | 
    d_django_starter-css-1       | Rebuilding...
    d_django_starter-css-1       | 
    d_django_starter-css-1       | Done in 213ms.
    d_django_starter-web-1       | [2023-09-30 08:22:16 +0000] [1] [INFO] Starting gunicorn 20.1.0
    d_django_starter-web-1       | [2023-09-30 08:22:16 +0000] [1] [INFO] Listening at: http://0.0.0.0:8000 (1)
    d_django_starter-web-1       | [2023-09-30 08:22:16 +0000] [1] [INFO] Using worker: sync
    d_django_starter-web-1       | [2023-09-30 08:22:16 +0000] [9] [INFO] Booting worker with pid: 9
    d_django_starter-worker-1    |  
    d_django_starter-worker-1    |  -------------- celery@d4411ceb7942 v5.3.0 (emerald-rush)
    d_django_starter-worker-1    | --- ***** ----- 
    d_django_starter-worker-1    | -- ******* ---- Linux-5.15.90.1-microsoft-standard-WSL2-x86_64-with-glibc2.31 2023-09-30 04:22:17
    d_django_starter-worker-1    | - *** --- * --- 
    d_django_starter-worker-1    | - ** ---------- [config]
    d_django_starter-worker-1    | - ** ---------- .> app:         d_django_starter:0x7fdd166ab650
    d_django_starter-worker-1    | - ** ---------- .> transport:   redis://redis:6379/0
    d_django_starter-worker-1    | - ** ---------- .> results:     redis://redis:6379/0
    d_django_starter-worker-1    | - *** --- * --- .> concurrency: 8 (prefork)
    d_django_starter-worker-1    | -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
    d_django_starter-worker-1    | --- ***** ----- 
    d_django_starter-worker-1    |  -------------- [queues]
    d_django_starter-worker-1    |                 .> celery           exchange=celery(direct) key=celery
    d_django_starter-worker-1    |                 
    d_django_starter-worker-1    | 
    d_django_starter-worker-1    | [tasks]
    d_django_starter-worker-1    | 
    d_django_starter-worker-1    | 
    d_django_starter-worker-1    | [2023-09-30 04:22:17,642: WARNING/MainProcess] /home/python/.local/lib/python3.11/site-packages/celery/worker/consumer/consumer.py:498: CPendingDeprecationWarning: The broker_connection_retry configuration setting will no longer determine
    d_django_starter-worker-1    | whether broker connection retries are made during startup in Celery 6.0 and above.
    d_django_starter-worker-1    | If you wish to retain the existing behavior for retrying connections on startup,
    d_django_starter-worker-1    | you should set broker_connection_retry_on_startup to True.
    d_django_starter-worker-1    |   warnings.warn(
    d_django_starter-worker-1    | 
    d_django_starter-worker-1    | [2023-09-30 04:22:17,651: INFO/MainProcess] Connected to redis://redis:6379/0
    d_django_starter-worker-1    | [2023-09-30 04:22:17,652: WARNING/MainProcess] /home/python/.local/lib/python3.11/site-packages/celery/worker/consumer/consumer.py:498: CPendingDeprecationWarning: The broker_connection_retry configuration setting will no longer determine
    d_django_starter-worker-1    | whether broker connection retries are made during startup in Celery 6.0 and above.
    d_django_starter-worker-1    | If you wish to retain the existing behavior for retrying connections on startup,
    d_django_starter-worker-1    | you should set broker_connection_retry_on_startup to True.
    d_django_starter-worker-1    |   warnings.warn(
    d_django_starter-worker-1    | 
    d_django_starter-worker-1    | [2023-09-30 04:22:17,655: INFO/MainProcess] mingle: searching for neighbors
    d_django_starter-worker-1    | [2023-09-30 04:22:18,666: INFO/MainProcess] mingle: all alone
    d_django_starter-worker-1    | [2023-09-30 04:22:18,697: INFO/MainProcess] celery@d4411ceb7942 ready.
    ```

- `./run quality`:

    ```bash
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$ ./run quality
    All done! ✨ 🍰 ✨
    32 files left unchanged.

    Task completed in 0m1.867s
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$
    ```

- `./run manage test`:

    ```bash
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$ ./run manage test

    149 static files copied to '/public_collected', 427 post-processed.
    Found 40 test(s).
    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    ........................................
    ----------------------------------------------------------------------
    Ran 40 tests in 2.641s

    OK
    Destroying test database for alias 'default'...

    Task completed in 0m5.971s
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$
    ```

## Running Commands in the Docker Container

- `docker compose exec web coverage run manage.py test`:

    ```bash
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$ docker compose exec web coverage run manage.py test
    Found 40 test(s).
    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    ........................................
    ----------------------------------------------------------------------
    Ran 40 tests in 3.553s

    OK
    Destroying test database for alias 'default'...
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$
    ```

- `docker compose exec web coverage report`:

    ```bash
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$ docker compose exec web coverage report
    Name                                  Stmts   Miss  Cover
    ---------------------------------------------------------
    __init__.py                               0      0   100%
    accounts/__init__.py                      0      0   100%
    accounts/admin.py                        17      0   100%
    accounts/apps.py                          4      0   100%
    accounts/forms.py                        11      0   100%
    accounts/migrations/0001_initial.py       9      0   100%
    accounts/migrations/__init__.py           0      0   100%
    accounts/models.py                        6      0   100%
    accounts/tests/__init__.py                0      0   100%
    accounts/tests/test_admin.py             46      0   100%
    accounts/tests/test_models.py            28      0   100%
    accounts/tests/test_views.py            132      0   100%
    accounts/urls.py                          7      0   100%
    accounts/views.py                        52      0   100%
    config/__init__.py                        2      0   100%
    config/celery.py                          6      0   100%
    config/settings.py                       40      0   100%
    config/urls.py                            4      0   100%
    manage.py                                12      2    83%
    pages/__init__.py                         0      0   100%
    pages/apps.py                             3      0   100%
    pages/tests.py                            5      0   100%
    pages/urls.py                             3      0   100%
    pages/views.py                            7      0   100%
    up/__init__.py                            0      0   100%
    up/tests.py                               8      0   100%
    up/urls.py                                3      0   100%
    up/views.py                              11      0   100%
    ---------------------------------------------------------
    TOTAL                                   416      2    99%
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$
    ```

- `docker compose exec web pip list`:

    ```bash
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$ docker compose exec web pip list
    Package              Version
    -------------------- -------
    amqp                 5.1.1
    asgiref              3.7.2
    billiard             4.1.0
    black                23.3.0
    celery               5.3.0
    click                8.1.6
    click-didyoumean     0.3.0
    click-plugins        1.1.1
    click-repl           0.3.0
    coverage             7.3.0
    Django               4.2.3
    django-debug-toolbar 4.1.0
    docutils             0.20.1
    flake8               6.0.0
    gunicorn             20.1.0
    isort                5.12.0
    kombu                5.3.1
    mccabe               0.7.0
    mypy-extensions      1.0.0
    packaging            23.1
    pathspec             0.11.2
    pip                  23.1.2
    platformdirs         3.10.0
    prompt-toolkit       3.0.39
    psycopg              3.1.9
    pycodestyle          2.10.0
    pyflakes             3.0.1
    python-dateutil      2.8.2
    redis                4.5.5
    setuptools           65.5.1
    six                  1.16.0
    sqlparse             0.4.4
    typing_extensions    4.7.1
    tzdata               2023.3
    vine                 5.0.0
    wcwidth              0.2.6
    wheel                0.41.1
    whitenoise           6.4.0

    [notice] A new release of pip is available: 23.1.2 -> 23.2.1
    [notice] To update, run: pip install --upgrade pip
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$
    ```

## Getting a List of Docker Containers, Images, and Volumes

- `docker ps`:

    ```bash
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$ docker ps
    CONTAINER ID   IMAGE                     COMMAND                  CREATED         STATUS                   PORTS                    NAMES
    d4411ceb7942   d_django_starter-worker   "celery -A config wo…"   3 minutes ago   Up 3 minutes             8000/tcp                 d_django_starter-worker-1
    bac56ee0e0f4   d_django_starter-web      "/app/bin/docker-ent…"   3 minutes ago   Up 3 minutes (healthy)   0.0.0.0:8000->8000/tcp   d_django_starter-web-1
    21d3d19e1cfd   redis:7.0.11-bullseye     "docker-entrypoint.s…"   3 minutes ago   Up 3 minutes             6379/tcp                 d_django_starter-redis-1
    6c42fe786d15   d_django_starter-js       "docker-entrypoint.s…"   3 minutes ago   Up 3 minutes                                      d_django_starter-js-1
    364fe079e114   d_django_starter-css      "docker-entrypoint.s…"   3 minutes ago   Up 3 minutes                                      d_django_starter-css-1
    f314c550ccfc   postgres:15.3-bullseye    "docker-entrypoint.s…"   3 minutes ago   Up 3 minutes             5432/tcp                 d_django_starter-postgres-1
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$
    ```

- `docker ps -a`:

    ```bash
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$ docker ps -a
    CONTAINER ID   IMAGE                     COMMAND                  CREATED         STATUS                   PORTS                    NAMES
    d4411ceb7942   d_django_starter-worker   "celery -A config wo…"   4 minutes ago   Up 4 minutes             8000/tcp                 d_django_starter-worker-1
    bac56ee0e0f4   d_django_starter-web      "/app/bin/docker-ent…"   4 minutes ago   Up 4 minutes (healthy)   0.0.0.0:8000->8000/tcp   d_django_starter-web-1
    21d3d19e1cfd   redis:7.0.11-bullseye     "docker-entrypoint.s…"   4 minutes ago   Up 4 minutes             6379/tcp                 d_django_starter-redis-1
    6c42fe786d15   d_django_starter-js       "docker-entrypoint.s…"   4 minutes ago   Up 4 minutes                                      d_django_starter-js-1
    364fe079e114   d_django_starter-css      "docker-entrypoint.s…"   4 minutes ago   Up 4 minutes                                      d_django_starter-css-1
    f314c550ccfc   postgres:15.3-bullseye    "docker-entrypoint.s…"   4 minutes ago   Up 4 minutes             5432/tcp                 d_django_starter-postgres-1
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$
    ```

- `docker images`:

    ```bash
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$ docker images
    REPOSITORY                TAG               IMAGE ID       CREATED          SIZE
    d_django_starter-js       latest            4adc138ddd47   38 minutes ago   536MB
    d_django_starter-css      latest            e54d3a92169d   38 minutes ago   536MB
    d_django_starter-worker   latest            86cb2df224cf   38 minutes ago   443MB
    d_django_starter-web      latest            531f7db14f24   38 minutes ago   443MB
    postgres                  15.3-bullseye     7a6b3f65d388   2 months ago     379MB
    redis                     7.0.11-bullseye   9316221abf0d   3 months ago     117MB
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$
    ```

- `docker volume ls`:

    ```bash
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$ docker volume ls
    DRIVER    VOLUME NAME
    local     d_django_starter_postgres
    local     d_django_starter_redis
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$
    ```

## Inspecting the Docker Volumes

- `docker volume inspect d_django_starter_postgres`:

    ```bash
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$ docker volume inspect d_django_starter_postgres
    [
        {
            "CreatedAt": "2023-09-30T07:49:23Z",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "d_django_starter",
                "com.docker.compose.version": "2.21.0",
                "com.docker.compose.volume": "postgres"
            },
            "Mountpoint": "/var/lib/docker/volumes/d_django_starter_postgres/_data",
            "Name": "d_django_starter_postgres",
            "Options": null,
            "Scope": "local"
        }
    ]
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$
    ```

- `docker volume inspect d_django_starter_redis`:

    ```bash
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$ docker volume inspect d_django_starter_redis
    [
        {
            "CreatedAt": "2023-09-30T07:49:23Z",
            "Driver": "local",
            "Labels": {
                "com.docker.compose.project": "d_django_starter",
                "com.docker.compose.version": "2.21.0",
                "com.docker.compose.volume": "redis"
            },
            "Mountpoint": "/var/lib/docker/volumes/d_django_starter_redis/_data",
            "Name": "d_django_starter_redis",
            "Options": null,
            "Scope": "local"
        }
    ]
    flynntknapp@DELL-GAME-DESK:~/Programming/DockerDjangoStarter-nickjj$
    ```
