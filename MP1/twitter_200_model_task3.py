import gensim.models
import numpy as np
import json
from nltk.tokenize import word_tokenize
import gensim.downloader as api
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neural_network import MLPClassifier

data_list = json.load(open('goemotions.json', 'r'))

parametersMLP = {
    'activation': ('identity', 'logistic', 'tanh', 'relu'),
    'solver': ('sgd', 'adam'),
    'hidden_layer_sizes': [(30, 50), (10, 10, 10)],
    'max_iter': [1]
}

arrayData = np.array(data_list)
training_data, testing_data = train_test_split(arrayData, test_size=0.2, random_state=75)

promptArrayTraining = []
promptArrayTesting = []

emotionTraining = []
emotionTesting = []

sentimentTraining = []
sentimentTesting = []

tokenizedModelTraining = []
tokenizedModelTesting = []

for x in training_data:
    promptArrayTraining.append(x[0])
    emotionTraining.append(x[1])
    sentimentTraining.append(x[2])

for x in testing_data:
    promptArrayTesting.append(x[0])
    emotionTesting.append(x[1])
    sentimentTesting.append(x[2])

for x in promptArrayTraining:
    tokenizedModelTraining.append(word_tokenize(x))

for x in promptArrayTesting:
    tokenizedModelTesting.append(word_tokenize(x))

corpusSentiment = np.array(sentimentTraining)
corpusEmotion = np.array(emotionTraining)

# Task 3.8 (Return Best Performing Model)
# Loading glove wiki gigaword
dataset = api.load('glove-twitter-200')

tempWord = []
tempPhrase = []
embeddingOfPosts = []

# Task 3.2 (Number of tokens in the training set)
def token_num():
    print(len(tokenizedModelTraining))

# Task 3.3 (Average of the embeddings)
def avg_embdings():
    tempPhrase = []
    for x in tokenizedModelTraining:
         tempWord1 = [word for word in x if word in dataset.key_to_index]
         for x in tempWord1:
           tempPhrase.append(np.mean(dataset[x], axis=0))

         embeddingOfPosts.append(tempPhrase)
         tempPhrase = []

    print(len(embeddingOfPosts))
    print(embeddingOfPosts)

# Task 3.4 (Overall hits)
def overall_hits ():
    hitRatePercentageTraining = []
    hitRatePercentageTesting = []
    for x in tokenizedModelTraining:
        tempWord1 = [word for word in x if word in dataset.key_to_index]
        hitRatePercentageTraining.append((len(tempWord1)/len(x))*100)
    for x in tokenizedModelTesting:
        tempWord1 = [word for word in x if word in dataset.key_to_index]
        hitRatePercentageTesting.append((len(tempWord1)/len(x))*100)

    print(hitRatePercentageTraining, hitRatePercentageTesting)

# Menu Selection
def menu(choice = None):
    print("************Welcome to Task-3 AI Classifier Demo**************")
    while choice != -1:
        choice = int(input("""
              1: Display tokens Number in training set
              2: Average embedding words of a post
              3: Overall hit rates

              Please enter your classifier choice: """))
        if choice == 1:
            token_num()
        elif choice == 2:
            avg_embdings()
        elif choice == 3:
            overall_hits()
        else:
            print("You must only select a number from 1 to 14, so please try again")
            choice = int(input("Please re-enter your choice: "))
# Start the Menu
menu()