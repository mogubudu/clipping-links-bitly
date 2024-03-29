# Обрезка ссылок с помощью Битли

С помощью данной программы можно в консоли просто преобразовать ссылку в сокращенную. Или посчитать сумму кликов по сокращенной ссылке, которая ранее была создана в Bitly . Для этого используется python и API сервиса Bitly.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

После того как установили все зависимости — можно запускать скрипт. 
Для этого нужно перейти в директорию где лежит файл и запустить его следующим образом:
```
python main.py [[your link]]
```
Скрипт принимает ссылки как с указанием протокола, так и без него. Ссылка, которую нужно сократить указывается после названия скрипта.
Например, 
```bash
$ python main.py dvmn.org
```
```bash
$ python main.py https://devman.org
```

В результате работы команд выше — мы получим сокращенную ссылку.

Если ввести уже сокращенную ссылку, то мы получим сумму кликов по ней за весь период.
```bash
$ python main.py bit.ly/2O9b7HB
```
Здесь в ответ мы получим сумму кликов за весь период по сокращенной ссылке.

### Цель проекта

Упростить работу с сокращением ссылок и подсчетом кликов по ним.

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
