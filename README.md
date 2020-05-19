#### API
 Method | Path | Body  | Specification
--- | --- | --- | --- 
 POST |/dictionary | ```Команда принимает на вход POST в виде json с параметрами key, value ({"key": "mail.ru", "value": "target"}) ``` | Запись значения по ключу. Если ключ уже существует, то *409*. Если какой-либо из параметров отсутствует в запросе, или есть лишние параметры, то *400*.
PUT |  /dictionary/<‘key’> |  | Изменение значения по ключу: Запрос аналогичен POST, только если ключ не найден, то *404*.
GET | /dictionary/<‘key’> |  | Получение значения по ключу.Команда принимает на вход один параметр key и отдает значение по ключу из словаря.Если ключ не найден, то *404*. 
DELETE | /dictionary/<‘key’> | | Удаление значения по ключу.Если ключ не найден, то все равно отвечаем *200*.


##### Пример данных для работы команды:
```
  data = {
     ‘key’: ‘test_key’,
     ‘value’: 'My name is Flask Server',
   }  
```   
   

 ##### Формат ответа:
 ```
   {
   "result": "Hello World!",
   "time": "2015-06-18 21:00"
   }
   ```
   Где result - значение из словаря, time - текущее время ответа.
   В случае удаления result должен быть null.

#### Чек-лист для API
##### Метод POST:
- [x] Запись значения по ключу -> (code: 200)
- [x] Запись значения по ключу, который уже существует -> (code:409)
- [x] Запрос, количество параметров которого больше чем нужно -> (code:400)
- [x] Запрос, параметры которого не *key* или *value* -> (code:400)

##### Метод PUT:
- [x] Изменение значения по ключу -> (code:200)
- [x] Изменение значения по ключу, который *не* существует -> (code:404)
- [x] Запрос, количество параметров которого больше чем нужно -> (code:400)
- [x] Запрос, параметры которого не *key* или *value* -> (code:400)

##### Метод GET:
- [x] Отдача  значения по ключу -> (code:200)
- [x] Запрос на отдачу по ключу, которого нет -> (code:404)

##### Метод DELETE:
- [x] Удаление по ключу -> (code:200)
- [x] Удаление по ключу, которого нет -> (code:200)
