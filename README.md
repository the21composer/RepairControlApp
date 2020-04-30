# MathemAtoms CASEIN: Программа умного управления ТОИР
*  Многопользовательский Web-интерфейс для системы технического обслуживания и ремонта производства
*  Реализовано с помощью: Python, Flask, MongoDB, HTML5, Bootstrap, JQuery
* Разработчики: Александр Облизанов, Константин Мосин [MathemAtoms]

#### Требования: 

*  Установленная MondoDB

#### Запуск:

*  Убедиться, что mongodb запущена по адресу `localhost:27017`
*  [Windows] Запустить скрипт `setup.bat`
*  [Linux] Запустить скрипт `setup.sh` (предварительно сделать файл исполняемым командой `chmod +x setup.sh`)
*  Перейти на страницу `127.0.0.1:5000/`

#### Авторизация:
Демонстрационный вариант приложения предусматривает следующие данные для входа:

| **Пользователь** | **Логин** | **Пароль** |
| ------------ | ----- | ------ |
| Ремонтный работник | worker | 1 |
| Начальник участка | site_manager | 1 |
| Начальник рем. службы | repair_manager | 1 |
| Начальник цеха | foreman | 1 |
| Администратор | admin | 1 |

#### Возможности пользователей:

**Ремонтный работник**
*  Просмотр планируемых ремонтов (срок, тип, описание, оборудование)
*  Изменение состояния ремонта (не активен, в процессе, выполнен)

**Начальник участка**
*  Просмотр состояния оборудования (модель, история ошибок, отказов, обслуживания)
*  Просмотр оценки необходимости ремонта, осуществление предиктивного обслуживания
*  Создание заявок на ремонт конкретного оборудования (тип и описание)

**Начальник ремонтной службы**
*  Просмотр заявок на ремонт оборудования от начальника участка
*  Планирование ремонта (указание крайнейго срока выполнения)
*  Просмотр состояния выполнения ремонта
*  Подтверждение выполнения ремонта

**Администратор**
* Загрузка файлов с данными об оборудовании/ошибках/отказах/сервисном обслуживании

#### Структура файлов:
*  webform - папка приложения
    * scripts - папка для скриптов установки
        * setup.bat - скрипт первоначальной установки приложения (windows)
        * setup.sh - скрипт первоначальной установки приложения (linux)
        * run.bat - скрипт для повторного запуска приложения (windows)
        * run.sh - скрипт для повторного запуска приложения (linux)
        
    * src - папка исходного кода программы
        * static - папка JS, CSS библиотек, изображений
        * templates - папка HTML страниц
    
    * data - папка с файлами данных для загрузки в БД
