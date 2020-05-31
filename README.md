# VidaPlaform

Architecture for VidaPlatform with microservices


## Environments

Create `.envs` and `db` folder:
```sh
mkdir .envs
mkdir db
mkdir db/backups
mkdir db/data
```

Create `.envs` files:
```sh
touch .common
touch .postgresql
```

Content of `.common` file:
```sh
JWT_SECRET=SECRET_KEY
```

Content of `.postgres` file:
```sh
POSTGRES_USER=platform_user
POSTGRES_PASSWORD=platform_pass
POSTGRES_DB=platform_db
PGDATA=/var/lib/postgresql/data/pgdata
POSTGRES_PORT=5432
POSTGRES_HOST=postgres-db
```