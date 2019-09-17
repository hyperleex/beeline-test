# Beeline Python Developer

## Задача

Необходимо реализовать несколько моделей для регистрации пользователей 
на мероприятия, подключить к ним стандартную админку и реализовать простое api.

## Модели

- [x] Пользователи (стандартные джанго)
- [x] Мероприятия (включают название, текст и дату)
- [x] Регистрации связывающие пользователей и мероприятия

## Админка (стандартная джанго)

- [x] Возможность смотреть, удалять и добавлять новые мероприятия.
- [x] Возможность смотреть, удалять и добавлять новых пользователей в мероприятия.

## API DRF

- [x] Вывод списка мероприятий, в этом списке должно быть отмечено есть ли 
зарегистрированные пользователи на данное мероприятие или нет.

- [x] Детальный вывод по конкретному мероприятию, в нем должны быть отображены 
все зарегистрированные на мероприятие пользователи.

- [x] Регистрация на мероприятие, возможность авторизованному пользователю 
зарегистрироваться на мероприятие.

## Желательно

- [x] Приложение должно работать в docker-контейнере и запускаться через docker-compose, 
os можно выбрать любую, но предпочтительней alpine, версия python не ниже 3.6, 
django не ниже 2.2.

- [x] Добавить покрытие кода тестами.