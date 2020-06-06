# authentication

1. Create .envs files:
```sh
mkdir .envs
mkdir .envs/.local
touch .envs/.local/.backend
```

2. Add this in .backend
```sh
DEBUG=True
```

3. Run `init.sh` in the project root:
```sh
sh init.sh up
```

4. To make migrations:
```sh
sh init.sh "run --rm app-auth python manage.py makemigrations"
```

4. Run migrations:
```sh
sh init.sh "run --rm app-auth python manage.py migrate"

or 

sh init.sh "run --rm app-auth python manage.py migrate"
```

5. Create superuser:
```sh
sh init.sh "run --rm app-auth python manage.py createsuperuser"
```

6. Go to `http:localhost:8000/admin` and update profile, change the role number to `120`