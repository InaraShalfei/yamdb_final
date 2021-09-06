
yamdb_final: http://84.201.128.102/admin

# Проект "Yamdb"

### Описание
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles).

### Команда для создания суперпользователя
```
docker-compose exec web python manage.py createsuperuser
```
### Команда для заполнения базы начальными данными
```
docker-compose exec web python manage.py loaddata fixtures.json
