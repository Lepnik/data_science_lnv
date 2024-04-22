# EDA Project: model creation to predict hotel rating.

## Contents  
[1. Project discription](https://github.com/Lepnik/data_science_lnv/blob/main/EDA%20Project/README.md#Project-discription)  
[2. Projec phases](https://github.com/Lepnik/data_science_lnv/blob/main/EDA%20Project/README.md#Projec-phases)  
[3. Data information](https://github.com/Lepnik/data_science_lnv/blob/main/EDA%20Project/README.md#Data-information)  
[4. Getting to know the data](https://github.com/Lepnik/data_science_lnv/blob/main/EDA%20Project/README.md#Getting-to-know-the-data)  
[5. Data cleaning&filling and new features creation](https://github.com/Lepnik/data_science_lnv/blob/main/EDA%20Project/README.md#Data-cleaning&filling-and-new-features-creation)  
[6. Preporation for ML](https://github.com/Lepnik/data_science_lnv/blob/main/EDA%20Project/README.md#Preporation-for-ML)    
[6. ML execution](https://github.com/Lepnik/data_science_lnv/blob/main/EDA%20Project/README.md#ML-execution)  
[7. Model testing and results submiting](https://github.com/Lepnik/data_science_lnv/blob/main/EDA%20Project/README.md#Model-testing-and-results-submiting)  
[8. Conclusions](https://github.com/Lepnik/data_science_lnv/blob/main/EDA%20Project/README.md#Conclusions)


### Project discription.    
The model should predict the hotel rating according to the Booking website based on the data available in the dataset. The intelligence analysis skills we've learned will help improve the model.

:arrow_up:[to contents](https://github.com/Lepnik/data_science_lnv/blob/main/EDA%20Project/README.md#Contents)


### Projec phases.
1. Getting to know the data;

2. Data cleaning&filling and new features creation;

3. Features encoding;

4. Preporation for ML;

5. ML execution;

6. Model testing and results submiting.


:arrow_up:[to contents](https://github.com/Lepnik/data_science_lnv/blob/main/EDA%20Project/README.md#Contents)

### Data information.
#### Raw data:
/kaggle/input/sf-booking/hotels_train.csv includes dataframe for train part.  
/kaggle/input/sf-booking/hotels_test.csv includes dataframe for test part.  
/kaggle/input/sf-booking/submission.csv includes sample of sabmition file.  

#### Features discription:
hotel_address — hotel address;  
review_date — the date when reviewer placed review;  
average_score — hatel average score, based on last comment thru last year;  
hotel_name — hotel name;  
reviewer_nationality — reviewer nationality;  
negative_review — negative review, which was given by reviewer;  
review_total_negative_word_counts — quantity of words in the negative review;  
positive_review — positive review, which was given by reviewer;  
review_total_positive_word_counts — quantity of words in the positive review;  
reviewer_score — reviewer score based on reviewer's own experience;  
total_number_of_reviews_reviewer_has_given — total number of reviews given by reviewer;  
total_number_of_reviews — total number of certain reviews for each hotel;  
tags — tags which were left by reviewer;  
days_since_review — days number between review date and clearance date;  
additional_number_of_scoring — number of score without any details in pos\neg review;  
lat — latitude (hotel coordinates);  
lng — longetude(hotel coordinates).  

#### Used libraries:
numpy, pandas, os, sklearn, matplotlib, seaborn, geopy, re, category_encoders, warnings, iso3166.
  
:arrow_up:[to contents](https://github.com/Lepnik/data_science_lnv/blob/main/EDA%20Project/README.md#Contents)


### Getting to know the data.  
It was released by built-in methods info, head, nunique, value_counts.

:arrow_up:[to contents](https://github.com/Lepnik/data_science_lnv/blob/main/EDA%20Project/README.md#Contents)


### Data cleaning&filling and new features creation.
Filling skiped latitude and longitude cells thru the geopy.  
New features "country, review_dayofweek, review_month, review_year, room, night, people, trip, assignment' creation.  
Sifting and recounting words in positive and negative reviews.  
Delition of reviews without any comment in positive and negative reviews.  
Optimization of rewiewer nationality feature.   
Non object features encoding.  
Correlation analisys for numeric features.  

:arrow_up:[to contents](https://github.com/Lepnik/data_science_lnv/blob/main/EDA%20Project/README.md#Contents)


### Preporation for ML.
Delition of object features. 
Spliting dataframe into train and test parts.

:arrow_up:[to contents](https://github.com/Lepnik/data_science_lnv/blob/main/EDA%20Project/README.md#Contents)

### ML execution.
ML execution thru the RandomForestRegressor.  
MAPE metric reached with 0.13293852513328527 score.

:arrow_up:[to contents](https://github.com/Lepnik/data_science_lnv/blob/main/EDA%20Project/README.md#Contents)


### Conclusions:  
ML model is successful and could be used for defining hotels with suspicious rating. But also could be improved.

:arrow_up:[to contents](https://github.com/Lepnik/data_science_lnv/blob/main/EDA%20Projec/README.md#Contents)