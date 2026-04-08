# Проект: Сегментация клиентов онлайн магазина подарков

## Оглавление  
[1. Описание проекта](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_6/README.md#Описание-проекта)  
[2. Фазы проекта](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_6/README.md#Фазы-проекта)  
[3. Краткая информация о данных](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_6/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_6/README.md#Этапы-работы-над-проектом)  
[5. Результат](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_6/README.md#Результат)    
[6. Выводы](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_6/README.md#Выводы) 


### Описание проекта    
**Бизнес-задача**: произвести сегментацию существующих клиентов, проинтерпретировать эти сегменты и определить стратегию взаимодействия с ними.

**Техническая задача**: построить модель кластеризации клиентов на основе их покупательской способности, частоты заказов и срока давности последней покупки, определить профиль каждого из кластеров.



[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_6/README.md#Оглавление)


### Основные цели проекта:

1. Произвести предобработку исходного набора данных о транзакциях.
2. Провести разведывательный анализ данных и выявить основные закономерности.
3. Сформировать набор данных о характеристиках каждого из уникальных клиентов.
4. Построить несколько моделей машинного обучения, решающих задачу кластеризации клиентов, определить количество кластеров и проинтерпретировать их.
5. Спроектировать процесс предсказания категории интересов клиента и протестировать вашу модель на новых клиентах.


[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_6/README.md#Оглавление)

### Краткая информация о данных
Исходный датасет находится по ссылке https://lms-cdn.skillfactory.ru/assets/courseware/v1/468638e49cb9e7d4b4dfdc296c1c778e/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block/pj6_data.zip

Признаки, описывающие каждую транзакцию:

InvoiceNo — номер счёта-фактуры (уникальный номинальный шестизначный номер, присваиваемый каждой транзакции; буква 'C' в начале кода указывает на отмену транзакции);
StockCode — код товара (уникальное пятизначное целое число, присваиваемое каждому отдельному товару);
Description — название товара;
Quantity — количество каждого товара за транзакцию;
InvoiceDate — дата и время выставления счёта/проведения транзакции;
UnitPrice — цена за единицу товара в фунтах стерлингов;
CustomerID — идентификатор клиента (уникальный пятизначный номер, однозначно присваиваемый каждому клиенту);
Country — название страны, в которой проживает клиент.

  
[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_6/README.md#Оглавление)


### Работы над проектом  
Работы осуществлялись посредством Инструментария библиотек и объектов:
pandas, numpy, matplotlib.pyplot, mpl_toolkits.mplot3d, re, sklearn.preprocessing, sklearn.pipeline, sklearn.decomposition, sklearn.cluster, sklearn.mixture, sklearn.metrics, plotly.graph_objs, plotly.express, lotly.subplots, warnings.

[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_6/README.md#Оглавление)


### Результаты:  
На исходных данных после анализа, очистки, добавления новых признаков была производена кластеризации. На ее основе приозведены сегментация и интерпретация сегментов клиентов на предмет фокуса для дальнейшего стимулирования. 
Используя Radar Chart была произведена отрисовка кластеров.

[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_6/README.md#Оглавление)


### Выводы:  
Набор и последовательность действий, использованные для реализации проекта, готовы для практического применения (в поле) в E-commerce секторе.

[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/MATH%2BML/Project_6/README.md#Оглавление)
