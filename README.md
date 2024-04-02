# Masters Dissertation
### Pavan Singh, MSc Advanced Analytics
#### University of Cape Town

<table>
  <tr>
    <td>
      <img src="/img/uct.png" width="150" height="150">
    </td>
    <td>
      <img src="/img/stats.jpeg" width="150" height="150">
    </td>
</table>

# Topic

**A Review-Aware Multi-Modal Recommender System with Neural Collaborative Filtering**

We essentially build a multi-modal recommender system which leverages neural collaborative filtering approach. We take the text and ratings data from amazon products reviews data set.  We evaluate our model and compare it to other baseline models such as other Matrix Factorization methods and/or Memory-based methods. We compare performance of the model with and without text data incorporated into model as well as the review sentiment. 


# Data and Resources

This repository contains all the Python code used to generate and build the recommender models. It also includes notebooks for the data loading, preprocessing, feature engineering, and data exploration. The actual data used in this thesis is not included in the repository due to its size, however, we provide the scripts to load, preprocess and clean the dataset. 

The data used in this thesis is the Amazon Product Reviews dataset. The dataset can be found at the link: [here](https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/). The dataset is available in multiple categories and can be downloaded in JSON format. We chose to download and use the "5-core" datasets for each category available on the page. Cumulatively (summing up across all categories), there are just over 75 million reviews. 



# Writing

The dissertation is written in LaTeX. We have 6 chapters, each in a different Latex file. The main file is titled `main.text`. The bibliography is in the file `main.bib`. The figures used in the dissertation are in the `Figures` folder.