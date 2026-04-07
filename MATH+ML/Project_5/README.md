# Проект: Анализ резюме из HeadHunter

## Оглавление  
[1. Описание проекта](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_5/README.md#Описание-проекта)  
[2. Фазы проекта](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_5/README.md#Фазы-проекта)  
[3. Краткая информация о данных](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_5/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_5/README.md#Этапы-работы-над-проектом)  
[5. Результат](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_5/README.md#Результат)    
[6. Выводы](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_5/README.md#Выводы) 


### Описание проекта    
**Бизнес-задача**: построить модель, которая будет предсказывать общую продолжительность поездки такси в Нью-Йорке.

**Техническая задача**: построить модель машинного обучения, которая на основе предложенных характеристик клиента будет предсказывать числовой признак - время поездки такси. То есть решить задачу регрессии.



[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_5/README.md#Оглавление)


### Основные цели проекта:

1. Сформировать набор данных на основе нескольких источников информации
2. Спроектировать новые признаки с помощью Feature Engineering и выявить наиболее значимые при построении модели
3. Исследовать предоставленные данные и выявить закономерности
4. Построить несколько моделей и выбрать из них наилучшую по заданной метрике
5. Спроектировать процесс предсказания времени длительности поездки для новых данных

[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_5/README.md#Оглавление)

### Краткая информация о данных
Исходный датасет находится по ссылке https://drive.google.com/file/d/1X_EJEfERiXki0SKtbnCL9JDv49Go14lF/view?usp=sharing

Данные о клиенте и таксопарке:
id — уникальный идентификатор поездки;
vendor_id — уникальный идентификатор поставщика услуг (таксопарка), связанного с записью поездки.

Временные характеристики:
pickup_datetime — дата и время, когда был включён счётчик поездки;
dropoff_datetime — дата и время, когда счётчик был отключён.

Географическая информация:
pickup_longitude — долгота, на которой был включён счётчик;
pickup_latitude — широта, на которой был включён счётчик;
dropoff_longitude — долгота, на которой счётчик был отключён;
dropoff_latitude — широта, на которой счётчик был отключён.

Прочие признаки:
passenger_count — количество пассажиров в транспортном средстве (введённое водителем значение);
store_and_fwd_flag — флаг, который указывает, сохранилась ли запись о поездке в памяти транспортного средства перед отправкой поставщику (Y — хранить и пересылать, N — не хранить и не пересылать поездку).

Целевой признак:
trip_duration — продолжительность поездки в секундах.

  
[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_5/README.md#Оглавление)


### Работы над проектом  
Работы осуществлялись посредством Инструментария библиотек и объектов:
pandas, numpy, matplotlib.pyplot, seaborn, scipy, sklearn, xgboost, warnings.

[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_5/README.md#Оглавление)


### Результаты:  
На исходных данных после анализа, очистки, добавления новых признаков была построена модель предсказания время поездки в такси. Модель добавлена на Kaggle. 

[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_5/README.md#Оглавление)


### Выводы:  
Рейтинг в референсных значениях.

[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_5/README.md#Оглавление)
