# Data Science Portfolio

Repository containing data science projects for self-learning.

More information about me: [LinkedIn](https://www.linkedin.com/in/den-ahinski/)

## Projects

### Disaster Tweets Detection (+ simple deployment via Flask)
**Tags: NLP, feature-engineering, logistic-regression, naive-bayes, random-forest, SVM, ensembling, flask, deployment**

* Data: Dataset from [Kaggle competition](https://www.kaggle.com/c/nlp-getting-started).

* [Notebook with research and models building](https://github.com/ahinski/portfolio/blob/main/disaster_tweets.ipynb)

* [Repo with deploy app](https://github.com/ahinski/TweetDetection)

  **Goal:** Create a model that will predict whether tweet is about real disaster or not 
  
  **What's inside:**
  
    * Data preparation
    
    * Feature engineering using NLP techniques
    
    * 4 models (LogReg, RF, NaiveBayes, SVM) and ensemble from LogReg and NB models
    
    * Model for analyzing a single tweet
    
   **Result:** Top 35% on [Kaggle](https://www.kaggle.com/denisahinski/competitions) with F1 = 0.80937

### Predict Sales
**Tags: time-series, EDA, keras, LSTM, GRU, LightGBM, feature engineering, ensembling**

* Data: Predict Future Sales from [Kaggle competition](https://www.kaggle.com/c/competitive-data-science-predict-future-sales).

* [Notebook](https://github.com/ahinski/portfolio/blob/main/predict_sales.ipynb)

  **Goal:** Predict sales in future month for shop and item pairs using data provided by 1C
  
  **What's inside:** Exploratory data analysis and 4 models: 
  
    * GRU and LSTM models using 12 months before the target month
    
    * Feature engineering
    
    * LightGBM Regressor with meta-features
    
    * Ensemble from 3 models
    
   **Result:** Top 44% on [Kaggle](https://www.kaggle.com/denisahinski/competitions) with RMSE = 0.99982

### Movie Recommendation
**Tags: collaborative-filtering, Pearson-similarity, movieLens**

* Data: MovieLens from [here](https://www.kaggle.com/grouplens/movielens-20m-dataset)

* [Notebook](https://github.com/ahinski/portfolio/blob/main/movie_recommendation.ipynb)

  **Goal:** Create a collaborative filtering recommendation system that will recommend similar movies for the one user liked and movies based on his ratings.

  **What's inside:** Research on collaborative filtering, 2 prototypes of recommender-functions based on Pearson correlation and their evaluation
  
  **Result:** Evaluated prototype of recommender system
