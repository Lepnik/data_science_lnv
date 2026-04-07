# Проект: Анализ резюме из HeadHunter

## Оглавление  
[1. Описание проекта](https://github.com/Lepnik/data_science_lnv/blob/main/EDA_Project/README.md#Описание-проекта)  
[2. Фазы проекта](https://github.com/Lepnik/data_science_lnv/blob/main/EDA_Project/README.md#Фазы-проекта)  
[3. Краткая информация о данных](https://github.com/Lepnik/data_science_lnv/blob/main/EDA_Project/README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](https://github.com/Lepnik/data_science_lnv/blob/main/EDA_Project/README.md#Этапы-работы-над-проектом)  
[5. Результат](https://github.com/Lepnik/data_science_lnv/blob/main/EDA_Project/README.md#Результат)    
[6. Выводы](https://github.com/Lepnik/data_science_lnv/blob/main/EDA_Project/README.md#Выводы) 


### Описание проекта    
**Бизнес-задача**: построение модели, которая предсказывает рейтинг отеля.

**Техническая задача**: очистка данных, проектирование признаков и разведывательный анализ данных.




[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/EDA_Project/README.md#Оглавление)


### Основные цели проекта:

    ✔️ создать модель, основанную на алгоритмах машинного обучения;

    ✔️ принять участие в соревновании на Kaggle;

    ✔️ понять, как правильно «подготовить» данные, чтобы модель работала лучше.


[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/EDA_Project/README.md#Оглавление)

### Краткая информация о данных
Исходный датасет находится по ссылке https://drive.google.com/file/d/1Qj0iYEbD64eVAaaBylJeIi3qvMzxf2C_/view?usp=sharing

Признаки датасета:
hotel_address — адрес отеля;
review_date — дата, когда рецензент разместил соответствующий отзыв;
average_score — средний балл отеля, рассчитанный на основе последнего комментария за последний год;
hotel_name — название отеля;
reviewer_nationality — страна рецензента;
negative_review — отрицательный отзыв, который рецензент дал отелю;
review_total_negative_word_counts — общее количество слов в отрицательном отзыв;
positive_review — положительный отзыв, который рецензент дал отелю;
review_total_positive_word_counts — общее количество слов в положительном отзыве.
reviewer_score — оценка, которую рецензент поставил отелю на основе своего опыта;
total_number_of_reviews_reviewer_has_given — количество отзывов, которые рецензенты дали в прошлом;
total_number_of_reviews — общее количество действительных отзывов об отеле;
tags — теги, которые рецензент дал отелю;
days_since_review — количество дней между датой проверки и датой очистки;
additional_number_of_scoring — есть также некоторые гости, которые просто поставили оценку сервису, но не оставили отзыв. Это число указывает, сколько там действительных оценок без проверки.
lat — географическая широта отеля;
lng — географическая долгота отеля.
  
[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/EDA_Project/README.md#Оглавление)


### Работы над проектом  
Работы осуществлялись посредством Инструментария библиотек и объектов:
pandas, sklearn.ensemble,sklearn.model_selection, sklearn.metrics, sklearn.ensemble.

[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/EDA_Project/README.md#Оглавление)


### Результаты:  
Набор и порядок использования шагов в проекте позволили достичь релевантного значения Mean Absolute Percentage Error (MAPE) для модели прогназирования.

[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/EDA_Project/README.md#Оглавление)


### Выводы:  
Набор и последовательность действий, использованные для реализации проекта, готовы для практического применения - участия в соревнованиях на Kaggle.

[к оглавлению](https://github.com/Lepnik/data_science_lnv/blob/main/EDA_Project/README.md#Оглавление)
