# Code and Notebooks for Masters Dissertation

The sequence/ordering of the notebooks is given below. 

1. [Data Loading]()

- load the data from the various sources
    - the review data is downloaded and loaded as separate product categories. 
- merge the data into a single dataframe
- save the dataframe as a file for further use

2. [Data Cleaning]()

- using the loaded and merged dataframe, clean the data
- see the data types, ensure its correct
- check for missing values
- check for duplicates
- check for outliers 
- save the cleaned dataframe as a file for further use

3. [Sentiment Analysis]()

- using the cleaned dataframe from (2), perform sentiment analysis
- see the distribution of the sentiment

4. [Data Exploration]()

- using the cleaned dataframe from (3), explore the data
- see the distribution of the data
- see the correlation between the data
- see the distribution of the data over time
- see the distribution of the data over the product categories, users, products etc.
- save the cleaned dataframe as a file for further use

5. [Modelling - IBCF]()

- using the cleaned dataframe from (3), perform modelling
- conduct IBCF
- evaluate models

6. [Modelling - UBCF]()

- using the cleaned dataframe from (3), perform modelling
- conduct UBCF
- evaluate models

7. [Modelling - NMF]()

- using the cleaned dataframe from (3), perform modelling
- conduct NMF
- evaluate models

8. [Modelling - NCF]()

- using the cleaned dataframe from (3), perform modelling
- conduct NCF
- evaluate models