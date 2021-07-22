![example workflow](https://github.com/InaraShalfei/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg)

yamdb_final: http://84.201.128.102/admin
### Команда для создания суперпользователя
```
docker-compose exec web python manage.py createsuperuser
```
### Команда для заполнения базы начальными данными
```
docker-compose exec web python manage.py loaddata fixtures.json
