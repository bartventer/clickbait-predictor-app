# End-to-End Machine Learning Flask React App

* NLP is used to standardize the user input, and a Multinomial Naive Bayes Classifier is then used to predict whether an artcile is clickbait or not. See the [jupyter notebook](machineLearning/clickbait.ipynb) for steps followed to build and save the model, which is loaded in the Flask backend server and API.
* The back-end is developed in Python and Flask, and delivers a few API endpoints upon the request from the front-end.
* The front-end is developed with React.
* The Application is hosted on Heroku, with Continuous Integration via Github.

# Functionaility

* A User can enter the name of an article, which will then return a predicted result together with a generated image for good measure.
