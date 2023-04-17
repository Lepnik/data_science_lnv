# Проект: Анализ резюме из HeadHunter

## Оглавление  
[1. Описание проекта](https://github.com/Lepnik/data_science_lnv/blob/main/HH%20Project%202/README.md#Описание-проекта)  
[2. Фазы проекта](https://github.com/Lepnik/data_science_lnv/blob/main/HH%20Project%202/README.md#Фазы-проекта)  
[3. Краткая информация о данных](https://github.com/Lepnik/data_science_lnv/blob/main/HH%20Project%202/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/Lepnik/data_science_lnv/blob/main/HH%20Project%202/README.md#Этапы-работы-над-проектом)  
[5. Результат](https://github.com/Lepnik/data_science_lnv/blob/main/HH%20Project%202/README.md#Результат)    
[6. Выводы](https://github.com/Lepnik/data_science_lnv/blob/main/HH%20Project%202/README.md#Выводы) 


### Описание проекта    
Cоздание модели машинного обучения, которая будет рекомендовать вакансии клиентам агентства, претендующим на позицию Data Scientist. Изначально необходимо понять, что из себя представляют данные и насколько они соответствуют целям проекта.

:arrow_up:[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/HH%20Project%202/README.md#Оглавление)


### Фазы проекта
1. знакомство с данными;

2. предварительный анализ данных;

3. детальный анализ вакансий;

4. анализ работодателей;

5. предметный анализ.


:arrow_up:[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/HH%20Project%202/README.md#Оглавление)

### Краткая информация о данных
Все необходимые таблицы находятся в схеме public базы данных project_sql. (http://sql.skillfactory.ru:3000/auth/login?redirect=%2Fquestion%2Fnotebook%23eyJjcmVhdGlvblR5cGUiOiJjdXN0b21fcXVlc3Rpb24iLCJkYXRhc2V0X3F1ZXJ5Ijp7ImRhdGFiYXNlIjpudWxsLCJxdWVyeSI6eyJzb3VyY2UtdGFibGUiOm51bGx9LCJ0eXBlIjoicXVlcnkifSwiZGlzcGxheSI6InRhYmxlIiwidmlzdWFsaXphdGlvbl9zZXR0aW5ncyI6e319)

VACANCIES датасет хранит в себе данные по вакансиям. 
AREAS датасет хранит код города и его название. 
EMPLOYERS справочник со списком работодателей.
INDUSTRIES справочник вариантов сфер деятельности работодателей.
EMPLOYERS_INDUSTRIES таблица для организации связи между работодателями и сферами их деятельности.

  
:arrow_up:[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/HH%20Project%202/README.md#Оглавление)


### Работы над проектом  
Работы осуществлялись посредством базовых команд и агрегатных функций postgresql.

:arrow_up:[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/HH%20Project%202/README.md#Оглавление)


### Результаты:  
Сформированы 22 основных и 2 дополнительных запроса SQL, которые дают развернутое представление о спектре вакансий на ХХ.ру для ИТ направления. (https://github.com/Lepnik/data_science_lnv/tree/main/HH%20Project/graphs)

:arrow_up:[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/HH%20Project%202/README.md#Оглавление)


### Выводы:  
Обработанный датасет готов для машинного обучения

:arrow_up:[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/HH%20Project%202/README.md#Оглавление)
