# Methods

In this section we discuss the methods that shall be used in our project. There are three main models that shall be built and compared. These are:

1. A Neural Collaborative Filtering model
2. A Content Based Filtering model
3. A Hybrid model that combines the above two models

***
## Neural Collaborative Filtering 

- uses neural network to learn the latent factors of users and items
- abbreviated as NCF
- uses a deep learning approach to collaborative filtering

Neural Collaborative Filtering (NCF) is a deep learning approach to collaborative filtering. The algorithm for NCF is as follows:

1. 
2. 
3. 
4. 
5. 

The model is trained using a binary cross-entropy loss function. The model is trained using the Adam optimizer with a learning rate of 0.001. The model is trained for 100 epochs with a batch size of 256. The model is implemented using the Keras library.

***
##  Content Based Filtering

- uses the features of the items to make recommendations
- abbreviated as CBF

Content based filtering is a method of making recommendations based on the similarity between items based on their features. The algorithm for content based filtering is as follows:

1. 
2. 
3. 
4. 
5. 

***
## Hybrid Model

- combines the above two models
- abbreviated as HMF

The hybrid model combines the above two models. The algorithm for the hybrid model is as follows:

1. 
2. 
3. 
4. 
5. 

# Summary 

So essentially the idea is to build a hybrid model that combines the above two models. We shall evaluate the performance of the hybrid model and compare it to the performance of the individual models.
What makes this project different to other recommender systems is the inclusion of text features. We shall evaluate the performance of the hybrid model with and without text data incorporated into the model. We shall also create sentiment analysis features from the text data and evaluate the performance of the hybrid model with and without these features.


 We shall also compare the performance of the hybrid model with and without text data incorporated into the model.