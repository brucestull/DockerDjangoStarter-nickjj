# Commands and Links

* `./run manage createsuperuser --email FlynntKnapp@email.app --username FlynntKnapp`
* `./run manage createsuperuser --email KnotStaff@email.app --username KnotStaff`

## Rename Project (Current Name: `d_django_starter`)

* `./bin/rename-project d_django_starter DDjangoStarter`

    flynnt@DELL-GAME-DESK:~/Programming/nickjj-docker-django-example$ ./bin/rename-project d_django_starter DDjangoStarter
    When renaming your project you'll need to re-create a new database.

    This can easily be done with Docker, but before this script does it
    please agree that it's ok for this script to delete your current
    project's database(s) by removing any associated Docker volumes.

    Run docker compose down -v (y/n)? y

    --------------------------------------------------------
    [+] Running 2/0
    ✔ Volume doc_django_postgres  Removed                                                                                                                               0.0s 
    ✔ Volume doc_django_redis     Removed                                                                                                                               0.0s 
    --------------------------------------------------------

    --------------------------------------------------------
    Your project has been renamed successfully!
    --------------------------------------------------------

    Do you want to init a new local git repo (y/n)? n

    We're done here. Everything worked!

    If you're happy with your new project's name you can delete this
    script by running: rm bin/rename-project

    Or you can keep it around in case you decide to change your project's
    name later on after developing it for a bit. You can re-run this
    script as many times as you want until you're happy.

    Check out the rest of the README on GitHub to wrap things up:

    https://github.com/nickjj/docker-django-example#start-and-setup-the-project
    flynnt@DELL-GAME-DESK:~/Programming/nickjj-docker-django-example$ git diff
    diff --git a/.env.example b/.env.example
    index 8f391db..f900240 100644
    --- a/.env.example
    +++ b/.env.example
    @@ -10,7 +10,7 @@
    export DOCKER_BUILDKIT=1
    
    # Rather than use the directory name, let's control the name of the project.
    -export COMPOSE_PROJECT_NAME=doc_django
    +export COMPOSE_PROJECT_NAME=d_django_starter
    
    # In development we want all services to start but in production you don't
    # need the asset watchers to run since assets get built into the image.
    @@ -72,9 +72,9 @@ export WEB_RELOAD=true
    
    # You'll always want to set POSTGRES_USER and POSTGRES_PASSWORD since the
    # postgres Docker image uses them for its default database user and password.
    -export POSTGRES_USER=doc_django
    +export POSTGRES_USER=d_django_starter
    export POSTGRES_PASSWORD=password
    -#export POSTGRES_DB=doc_django
    +#export POSTGRES_DB=d_django_starter
    #export POSTGRES_HOST=postgres
    #export POSTGRES_PORT=5432
    
    diff --git a/CHANGELOG.md b/CHANGELOG.md
    index e7b195b..73d8f55 100644
    --- a/CHANGELOG.md
    +++ b/CHANGELOG.md
    @@ -282,7 +282,7 @@ Changelog](https://keepachangelog.com/en/1.0.0/).
    
    ### Changed
    
    -- Rename `src/doc_django/` directory to `src/config/` to be more portable
    +- Rename `src/d_django_starter/` directory to `src/config/` to be more portable
    - Replace `APP_NAME` in `run` script with `POSTGRES_USER` for connecting to psql
    - Avoid using multi-line imports with commas or parenthesis
    - Update Python from `3.9.2` to `3.9.5`
    diff --git a/README.md b/README.md
    index 7179c4a..890397f 100644
    --- a/README.md
    +++ b/README.md
    @@ -139,8 +139,8 @@ these commands for PowerShell if you want.
    #### Clone this repo anywhere you want and move into the directory:
    
    ```sh
    -git clone https://github.com/nickjj/docker-django-example doc_django
    -cd doc_django
    +git clone https://github.com/nickjj/docker-django-example d_django_starter
    +cd d_django_starter
    
    # Optionally checkout a specific tag, such as: git checkout 0.10.0
    ```
    @@ -265,9 +265,9 @@ able to run `run` instead of `./run`.*
    
    ## Running a script to automate renaming the project
    
    -The app is named `doc_django` right now but chances are your app will be a different
    +The app is named `d_django_starter` right now but chances are your app will be a different
    name. Since the app is already created we'll need to do a find / replace on a
    -few variants of the string "doc_django" and update a few Docker related resources.
    +few variants of the string "d_django_starter" and update a few Docker related resources.
    
    And by we I mean I created a zero dependency shell script that does all of the
    heavy lifting for you. All you have to do is run the script below.
    diff --git a/assets/package.json b/assets/package.json
    index c3b4527..e8c4f7e 100644
    --- a/assets/package.json
    +++ b/assets/package.json
    @@ -1,5 +1,5 @@
    {
    -  "name": "doc_django",
    +  "name": "d_django_starter",
    "private": true,
    "dependencies": {
        "autoprefixer": "10.4.14",
    diff --git a/bin/rename-project b/bin/rename-project
    index f2ff231..5673a19 100755
    --- a/bin/rename-project
    +++ b/bin/rename-project
    @@ -5,8 +5,8 @@ set -eo pipefail
    APP_NAME="${1}"
    MODULE_NAME="${2}"
    
    -FIND_APP_NAME="doc_django"
    -FIND_MODULE_NAME="DocDjango"
    +FIND_APP_NAME="d_django_starter"
    +FIND_MODULE_NAME="DDjangoStarter"
    FIND_FRAMEWORK="django"
    
    if [ -z "${APP_NAME}" ] || [ -z "${MODULE_NAME}" ]; then
    diff --git a/notes/commands_and_links.md b/notes/commands_and_links.md
    index 4385551..87dd6ba 100644
    --- a/notes/commands_and_links.md
    +++ b/notes/commands_and_links.md
    @@ -1,4 +1,8 @@
    # Commands and Links
    
    -`./run manage createsuperuser --email FlynntKnapp@email.app --username FlynntKnapp`
    -`./run manage createsuperuser --email KnotStaff@email.app --username KnotStaff`
    +* `./run manage createsuperuser --email FlynntKnapp@email.app --username FlynntKnapp`
    +* `./run manage createsuperuser --email KnotStaff@email.app --username KnotStaff`
    +
    +## Rename Project (Current Name: `d_django_starter`)
    +
    +* `./bin/rename-project d_django_starter DDjangoStarter`
    diff --git a/notes/notes.md b/notes/notes.md
    index 43744a5..c20fe51 100644
    --- a/notes/notes.md
    +++ b/notes/notes.md
    @@ -30,7 +30,7 @@
    
    ## Change Project Name
    
    -`./bin/rename-project doc_django DocDjango`
    +`./bin/rename-project d_django_starter DDjangoStarter`
    
    ```bash
    (mdn-local-library-tutorial-mine) flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$ git status
    @@ -56,11 +56,11 @@ no changes added to commit (use "git add" and/or "git commit -a")
    (mdn-local-library-tutorial-mine) flynnt@DELL-GAMING:~/Programming/nickjj-docker-django-example$
    ```
    
    -* Search for `doc_django`
    +* Search for `d_django_starter`
    
    ![image](https://github.com/brucestull/nickjj-docker-django-example/assets/47562501/0c30a413-818d-413c-a9bf-89f10681673c)
    
    -* Search for `DocDjango`
    +* Search for `DDjangoStarter`
    
    ![image](https://github.com/brucestull/nickjj-docker-django-example/assets/47562501/93c994f8-ea7f-4892-aa47-2fec35be1272)
    
    diff --git a/src/config/asgi.py b/src/config/asgi.py
    index 19b5496..7f5c262 100644
    --- a/src/config/asgi.py
    +++ b/src/config/asgi.py
    @@ -1,5 +1,5 @@
    """
    -ASGI config for doc_django project.
    +ASGI config for d_django_starter project.
    
    It exposes the ASGI callable as a module-level variable named `application`.
    
    diff --git a/src/config/celery.py b/src/config/celery.py
    index 2b24d50..c6b29f1 100644
    --- a/src/config/celery.py
    +++ b/src/config/celery.py
    @@ -4,6 +4,6 @@ from celery import Celery
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    
    -app = Celery("doc_django")
    +app = Celery("d_django_starter")
    app.config_from_object("django.conf:settings", namespace="CELERY")
    app.autodiscover_tasks()
    diff --git a/src/config/settings.py b/src/config/settings.py
    index f79f6e4..1d3c8b2 100644
    --- a/src/config/settings.py
    +++ b/src/config/settings.py
    @@ -1,5 +1,5 @@
    """
    -Django settings for doc_django project.
    +Django settings for d_django_starter project.
    
    Generated by 'django-admin startproject' using Django 4.2.
    
    @@ -83,8 +83,8 @@ WSGI_APPLICATION = "config.wsgi.application"
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
    -        "NAME": os.getenv("POSTGRES_DB", "doc_django"),
    -        "USER": os.getenv("POSTGRES_USER", "doc_django"),
    +        "NAME": os.getenv("POSTGRES_DB", "d_django_starter"),
    +        "USER": os.getenv("POSTGRES_USER", "d_django_starter"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD", "password"),
            "HOST": os.getenv("POSTGRES_HOST", "postgres"),
            "PORT": os.getenv("POSTGRES_PORT", "5432"),
    diff --git a/src/config/urls.py b/src/config/urls.py
    index 513185c..3f69dc8 100644
    --- a/src/config/urls.py
    +++ b/src/config/urls.py
    @@ -1,5 +1,5 @@
    """
    -URL configuration for doc_django project.
    +URL configuration for d_django_starter project.
    
    The `urlpatterns` list routes URLs to views. For more information please see:
        https://docs.djangoproject.com/en/4.2/topics/http/urls/
    diff --git a/src/config/wsgi.py b/src/config/wsgi.py
    index 8e1f4b7..cf4bedc 100644
    --- a/src/config/wsgi.py
    +++ b/src/config/wsgi.py
    @@ -1,5 +1,5 @@
    """
    -WSGI config for doc_django project.
    +WSGI config for d_django_starter project.
    
    It exposes the WSGI callable as a module-level variable named ``application``.
    
    flynnt@DELL-GAME-DESK:~/Programming/nickjj-docker-django-example$
