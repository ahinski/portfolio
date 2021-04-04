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
   
### A/B test analysis
**Tags: a/b, visualization, retention rate, mobile game, chi-square**

* Data: Mobile game data from [Kaggle](https://www.kaggle.com/yufengsui/mobile-games-ab-testing)

* [Notebook](https://github.com/ahinski/portfolio/blob/main/ab_test.ipynb)

**Goal:** Analyze a/b testing results. Check if changing level gate (at which a player whould be asked to pay to play) will increase retention rate.

**Results:** It's statistically significant that changing level gates increased retention rate.
