# pasalpedia

## Clone Repo

```bash
    git clone git@github.com:ardwiinoo/pasalpedia.git
```

## Enter Directory

```bash
    cd ./pasalpedia
```

## Install Deps

Prerequisite:

- Python; version: ^3.x

- NodeJs; version: ^12.x

```bash
    pip install -r requirements.txt
```

```bash
    npm install
```

## Setup Creds

1. Copy .env.example; change to `.env`
2. Fill in the required credentials

## Setup Migrations

```bash
    # init flask-migrate
    flask db init -d app/database/migrations
```

```bash
    # example create new users table
    flask db migrate -m "Create users table" -d app/database/migrations
```

```bash
    # migrate up migrations
    flask db upgrade -d app/database/migrations
```
## Run Project

Terminal 1

```bash
    npm run buildcss
```

Terminal 2

```bash
    python main.py
```
