# Code and Notebooks for Masters Dissertation

The sequence/ordering of the notebooks is given below. 

1. [Data Loading]()

- load the data from the various sources
    - we have **review data** from users and **metadata** from the products
    - the review data is downloaded and loaded as separate product categories. 
    - all metadata is loaded in as one file

- merge the data into a single dataframe

- save the dataframe as a file for further use


2. [Data Cleaning]()

- using the loaded and merged dataframe, clean the data
- see the data types, ensure its correct
- check for missing values
- check for duplicates
- check for outliers 
- save the cleaned dataframe as a file for further use

3. [Data Exploration]()

- using the cleaned dataframe, explore the data
- see the distribution of the data
- see the correlation between the data
- see the distribution of the data over time
- see the distribution of the data over the product categories, users, products etc.
- save the cleaned dataframe as a file for further use

4. [Text and Sentiment Analysis]()

- using the cleaned dataframe, perform text and sentiment analysis
- see the distribution of the text length
- see the distribution of the sentiment

5. [Data Preprocessing]()

- using the cleaned dataframe, perform data preprocessing
- prepare data for modelling
- save the cleaned dataframe as a file for further use

6. [Modelling - Collaborative Filtering RecSys]()

- using the cleaned dataframe, perform modelling
- conduct neural collaborative filtering

7. [Modelling - Content Based RecSys]()

- using the cleaned dataframe, perform modelling
- conduct content based filtering

8. [Modelling - Hybrid RecSys]()

- using the cleaned dataframe, perform modelling
- conduct hybrid filtering

9. [Modelling - Benchmark Models]()

- using the cleaned dataframe, perform modelling
- conduct benchmark models
    - neural collaborative filtering
    - content based filtering
    - non-negative matrix factorization
    - collaborative filtering
    - random recommender


10. [Evaluation]()

- using the cleaned dataframe, perform evaluation
- evaluate the models
