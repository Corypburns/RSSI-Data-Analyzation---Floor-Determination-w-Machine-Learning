# <ins>DATASET DOWNLOAD</ins>
https://archive.ics.uci.edu/dataset/310/ujiindoorloc


# <ins>MODELS USED</ins>
The inital testing done with this process is done through the use of three distinct models. One being Naive Bayes, another being XGBoost, and finally, K Nearest Neighbor. These models act differently amongst one another and behave in its own way; no one model is the same as the other, at least in these examples. Naive Bayes acts as a probability-based model, XGBoost is a decision tree-based model, and KNN (shorthand for K Nearest Neighbor) acts as a proximity-based model that takes the distance from an unlabeled point and compares its RSSI strengths to its *k* neighbor's RSSI strength and compares them to determine the floor (an example of this is when *k* = 2. The neighbors already know the floor value, and the unlabeled point's strengths are compared to those two closest RSSI strengths, which determines the floor the device was accessed on).

# <ins>CODE DESIGN</ins>
Each .py file is designed in such a way where there are two main methods. A test, and a train method. These methods do exactly what it sounds like they do, test and train. Training allows the model to train on 100% of the data rather than dividing the dataset into a train/test split through Sklearn's train-test-split library. Once trained, the trained model is saved through a process called a Joblib; this ensures that the model and all its parameters are saved to a file that the test method can access later. Upon testing, the Joblib file is fetched from the directory and utilized to complete the testing process in which each prediction from the model will generate a percentage known as a confidence rating that determines its exact confidence on the decision it made. This idea is spread across all of the model files, and utilizes scikitlearn's various libraries as well as Pandas, a data processing library that can read CSV files and select specific data entries.

# <ins>REPLICATING THE RESULTS</ins>
If you are interested in trying this out for yourself, you may do so by all means! I will walk you through how you can get results either with the same dataset, or an entirely different one all together. To start, make sure you have all the libraries as defined in the code files installed. Once the requirements are met, you can either download the dataset from this description, or find an entirely new one, as stated above. For the same dataset, you don't need to change anything unless you aim to get better results than I have achieved (this involves tweaking the hyperparameters). For a different dataset, I recommend using Kaggle as it is a great source for machine learning datasets.

# <ins>USING A DIFFERENT DATASET</ins>
Here are some things that need to be changed to make the model work with your specified dataset. You need to change the *X* variable as well as the *y* variable, as *X* pertains to the columns, or feature groups, while *y* pertains to the value that the model is trying to predict. Change these values as you see fit in relation to the dataset that you are using; this will **NOT** work if the values are not the same as your desired dataset the declaration *y = df["FLOOR"]*, for example, refers to the column "FLOOR" within the ujindoorloc dataset, the column that the model is predicting; we make separate variables because if *X* <ins>also</ins> contained "FLOOR", then the model would get perfect results because it knows the answer to what it is trying to predict already. In other words, that would make this process pointless.

# <ins>MY RESULTS</ins>
The results obtained are as follows:

**XGBoost - ** 88.30% <br></br>
**K Nearest Neighbor - ** 74.17%
**Naive Bayes - ** 44.37%

These can **DEFINITELY** be improved upon through various hyperparameter tweaks and changes.
