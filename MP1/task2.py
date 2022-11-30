import sys
import numpy
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import json
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV

# Task 2.1
# Printing the whole array (without dots)
numpy.set_printoptions(threshold=sys.maxsize)
data_list = json.load(open('goemotions.json', 'r'))

parametersNB = {
    'alpha': (0.5, 0, 2, 1, 2.5, 1.5)
}
parametersDT = {
    'criterion': ["gini"],
    'max_depth': (10, 20),
    'min_samples_split': (2, 3, 4)
}
parametersMLP = {
    'activation': ('identity', 'logistic', 'tanh', 'relu'),
    'solver': ('sgd', 'adam'),
    'hidden_layer_sizes': [(30, 50), (10, 10, 10)],
    'max_iter': [1]
}
# convert the list into 2D Array
arrayData = np.array(data_list)
promptArray = []

# Separate prompt from Emo. & Sent.
for x in arrayData:
    promptArray.append(x[0])

# Get the total words count
corpus = np.array(promptArray)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

# print(vectorizer.get_feature_names_out())
# print()
# print("Total word vocabulary: ", len(vectorizer.get_feature_names_out()))
# print()
##################################################################################

# Task 2.2
training_data, testing_data = train_test_split(arrayData, test_size=0.2, random_state=75)

# print(f"No. of training examples: {training_data.shape[0]}")
# print(f"No. of testing examples: {testing_data.shape[0]}")

##################################################################################

# Task 2.3
prompt_trainingData = []
sentiment_trainingData = []
emotions_trainingData = []

prompt_testingData = []
sentiment_testingData = []
emotions_testingData = []

for x in training_data:
    prompt_trainingData.append(x[0])
    sentiment_trainingData.append(x[2])
    emotions_trainingData.append(x[1])

for x in testing_data:
    prompt_testingData.append(x[0])
    sentiment_testingData.append(x[2])
    emotions_testingData.append(x[1])

# print(prompt_trainingData)
# print(sentiment_trainingData)
# print(emotions_trainingData)

### Initialization of Classifiers Parameters ###
# Create a NumPy array objects
corpusPrompt = np.array(prompt_trainingData)
corpusSentiment = np.array(sentiment_trainingData)
corpusEmotion = np.array(emotions_trainingData)
#
Xprompt = vectorizer.fit_transform(corpusPrompt)
ySentiment = corpusSentiment
yEmotion = corpusEmotion
prompt_testData = vectorizer.transform(np.array(prompt_testingData))

# MNB Classifier
classifier = MultinomialNB()

# DT Classifier
dtc = tree.DecisionTreeClassifier()


# # MLP Classifier
mlp_sentiment = MLPClassifier(max_iter=1)
mlp_emotion = MLPClassifier(max_iter=1)


# Task 2.3.1 (MNB)
def base_MNB():
    # modelNB_sentiment = classifier.fit(Xprompt, ySentiment)
    modelNB_emotions = classifier.fit(Xprompt, yEmotion)

    # predict_sentiment = modelNB_sentiment.predict(prompt_testData)
    predict_emotion = modelNB_emotions.predict(prompt_testData)

    print(predict_emotion)
    # print(emotions_testingData)


# Task 2.3.2 (DT)

def base_DT():
    modelTree_sentiment = dtc.fit(Xprompt, ySentiment)
    modelTree_emotion = dtc.fit(Xprompt, yEmotion)

    treePredict_sentiment = modelTree_sentiment.predict(prompt_testData)
    treePredict_emotion = modelTree_emotion.predict(prompt_testData)

    print(treePredict_emotion)
    print(treePredict_sentiment)
    print(sentiment_testingData)

# Task 2.3.3 (MLP) --> not accurate

def base_MLP():

    modelMLP_sentiment = mlp_sentiment.fit(Xprompt, ySentiment)
    modelMLP_emotion = mlp_emotion.fit(Xprompt, yEmotion)

    mlpPredict_sentiment = modelMLP_sentiment.predict(prompt_testData)
    mlpPredict_emotion = modelMLP_emotion.predict(prompt_testData)

    print(mlpPredict_emotion)
    print(mlpPredict_sentiment)
    print(emotions_testingData)


# Task 2.3.4 (TOP MNB) --> Not accurate Warning because of alpha value = 0 in parameters

def top_MNB():
    gridTopMNB_sentiment = GridSearchCV(classifier, parametersNB)
    gridTopMNB_emotion = GridSearchCV(classifier, parametersNB)

    modelTopMNB_sentiment = gridTopMNB_sentiment.fit(Xprompt, ySentiment)
    modelTopMNB_emotion = gridTopMNB_emotion.fit(Xprompt, yEmotion)

    predictTopMNB_sentiment = modelTopMNB_sentiment.predict(prompt_testData)
    predictTopMNB_emotion = modelTopMNB_emotion.predict(prompt_testData)

    print(predictTopMNB_sentiment)
    print(predictTopMNB_emotion)
    print(emotions_testingData)
    print(sentiment_testingData)


# Task 2.3.5 (TOP DT) --> Not accurate and takes a lot of time 7aywan

def top_DT():
    gridTopDT_sentiment = GridSearchCV(dtc, parametersDT)
    gridTopDT_emotion = GridSearchCV(dtc, parametersDT)

    modelTopDT_sentiment = gridTopDT_sentiment.fit(Xprompt, ySentiment)
    modelTopDT_emotion = gridTopDT_emotion.fit(Xprompt, yEmotion)

    predictTopDT_sentiment = modelTopDT_sentiment.predict(prompt_testData)
    predictTopDT_emotion = modelTopDT_emotion.predict(prompt_testData)

    print(predictTopDT_sentiment)
    print(predictTopDT_emotion)
    print(emotions_testingData)
    print(sentiment_testingData)


# Task 2.3.6 (TOP MLP)

def top_MLP():
    gridTopMLP_sentiment = GridSearchCV(mlp_sentiment, parametersMLP)
    gridTopMLP_emotion = GridSearchCV(mlp_emotion, parametersMLP)

    modelTopMLP_sentiment = gridTopMLP_sentiment.fit(Xprompt, ySentiment)
    modelTopMLP_emotion = gridTopMLP_emotion.fit(Xprompt, yEmotion)

    predictTopMLP_sentiment = modelTopMLP_sentiment.predict(prompt_testData)
    predictTopMLP_emotion = modelTopMLP_emotion.predict(prompt_testData)

    print(predictTopMLP_sentiment)
    print(predictTopMLP_emotion)
    print(emotions_testingData)
    print(sentiment_testingData)


##################################################################################

# Task 2.5 (Different Splits)
training_data1, testing_data1 = train_test_split(arrayData, test_size=0.4, random_state=75)
prompt_trainingData1 = []
sentiment_trainingData1 = []
emotions_trainingData1 = []

prompt_testingData1 = []
sentiment_testingData1 = []
emotions_testingData1 = []

for x in training_data1:
    prompt_trainingData1.append(x[0])
    sentiment_trainingData1.append(x[2])
    emotions_trainingData1.append(x[1])

for x in testing_data1:
    prompt_testingData1.append(x[0])
    sentiment_testingData1.append(x[2])
    emotions_testingData1.append(x[1])

### Initialization of Classifiers Parameters ###
# Create a NumPy array objects
corpusPrompt1 = np.array(prompt_trainingData1)
corpusSentiment1 = np.array(sentiment_trainingData1)
corpusEmotion1 = np.array(emotions_trainingData1)
Xprompt1 = vectorizer.fit_transform(corpusPrompt1)
ySentiment1 = corpusSentiment1
yEmotion1 = corpusEmotion1
prompt_testData1 = vectorizer.transform(np.array(prompt_testingData1))

# MNB Classifier
classifier1 = MultinomialNB()

# DT Classifier
dtc1 = tree.DecisionTreeClassifier()

# MLP Classifier
mlp_sentiment1 = MLPClassifier(max_iter=1)
mlp_emotion1 = MLPClassifier(max_iter=1)


# 2.5 (Naive-Bayes)
def base_MNB1():
    modelNB_sentiment1 = classifier1.fit(Xprompt1, ySentiment1)
    modelNB_emotions1 = classifier1.fit(Xprompt1, yEmotion1)

    predict_sentiment1 = modelNB_sentiment1.predict(prompt_testData1)
    predict_emotion1 = modelNB_emotions1.predict(prompt_testData1)

    print(predict_emotion1)
    print(predict_sentiment1)
    print(emotions_testingData1)

# 2.5 (DT)
def base_DT1():
    modelTree_sentiment1 = dtc1.fit(Xprompt1, ySentiment1)
    modelTree_emotion1 = dtc1.fit(Xprompt1, yEmotion1)

    treePredict_sentiment1 = modelTree_sentiment1.predict(prompt_testData1)
    treePredict_emotion1 = modelTree_emotion1.predict(prompt_testData1)

    print(treePredict_sentiment1)
    print(treePredict_emotion1)
    print(sentiment_testingData1)


# Task 2.5 (MLP)

def base_MLP1():
    modelMLP_sentiment1 = mlp_sentiment1.fit(Xprompt1, ySentiment1)
    modelMLP_emotion1 = mlp_emotion1.fit(Xprompt1, yEmotion1)

    mlpPredict_sentiment1 = modelMLP_sentiment1.predict(prompt_testData1)
    mlpPredict_emotion1 = modelMLP_emotion1.predict(prompt_testData1)

    print(mlpPredict_emotion1)
    print(mlpPredict_sentiment1)
    print(emotions_testingData1)


# Task 2.5 (TOP MNB)

def top_MNB1():
    gridTopMNB_sentiment1 = GridSearchCV(classifier, parametersNB)
    gridTopMNB_emotion1 = GridSearchCV(classifier1, parametersNB)

    modelTopMNB_sentiment1 = gridTopMNB_sentiment1.fit(Xprompt, ySentiment)
    modelTopMNB_emotion1 = gridTopMNB_emotion1.fit(Xprompt1, yEmotion1)

    predictTopMNB_sentiment1 = modelTopMNB_sentiment1.predict(prompt_testData)
    predictTopMNB_emotion1 = modelTopMNB_emotion1.predict(prompt_testData1)

    print(predictTopMNB_sentiment1)
    print(predictTopMNB_emotion1)
    print(emotions_testingData1)
    print(sentiment_testingData1)


# Task 2.5 (TOP DT)

def top_DT1():
    gridTopDT_sentiment1 = GridSearchCV(dtc1, parametersDT)
    gridTopDT_emotion1 = GridSearchCV(dtc1, parametersDT)

    modelTopDT_sentiment1 = gridTopDT_sentiment1.fit(Xprompt, ySentiment)
    modelTopDT_emotion1 = gridTopDT_emotion1.fit(Xprompt1, yEmotion1)

    predictTopDT_sentiment1 = modelTopDT_sentiment1.predict(prompt_testData)
    predictTopDT_emotion1 = modelTopDT_emotion1.predict(prompt_testData1)

    print(predictTopDT_sentiment1)
    print(predictTopDT_emotion1)
    print(emotions_testingData1)
    print(sentiment_testingData1)


# Task 2.5 (TOP MLP)

def top_MLP1():
    gridTopMLP_sentiment1 = GridSearchCV(mlp_sentiment1, parametersMLP)
    gridTopMLP_emotion1 = GridSearchCV(mlp_emotion1, parametersMLP)

    modelTopMLP_sentiment1 = gridTopMLP_sentiment1.fit(Xprompt1, ySentiment1)
    modelTopMLP_emotion1 = gridTopMLP_emotion1.fit(Xprompt1, yEmotion1)

    predictTopMLP_sentiment1 = modelTopMLP_sentiment1.predict(prompt_testData1)
    predictTopMLP_emotion1 = modelTopMLP_emotion1.predict(prompt_testData1)

    print(predictTopMLP_sentiment1)
    print(predictTopMLP_emotion1)
    print(emotions_testingData1)
    print(sentiment_testingData1)

# Menu Selection
def menu(choice = None):
    print("************Welcome to Task-2 AI Classifier Demo**************")
    while choice != -1:
        choice = int(input("""
              1: Base-MNB
              2: Base-DT
              3: Base-MLP
              4: Top-MNB
              5: Top-DT
              6: Top-MLP
              For Different Splits, please choose an option:
              7: Base-MNB
              8: Base-DT
              9: Base-MLP
              10: Top-MNB
              11: Top-DT
              12: Top-MLP
              13: Exit

              Please enter your classifier choice: """))
        if choice == 1:
            base_MNB()
        elif choice == 2:
            base_DT()
        elif choice == 3:
            base_MLP()
        elif choice == 4:
            top_MNB()
        elif choice == 5:
            top_DT()
        elif choice == 6:
            top_MLP()
        elif choice == 7:
            base_MNB1()
        elif choice == 8:
            base_DT1()
        elif choice == 9:
            base_MLP1()
        elif choice == 10:
            top_MNB1()
        elif choice == 11:
            top_DT1()
        elif choice == 12:
            top_MLP1()
        elif choice == 13:
            sys.exit()
        else:
            print("You must only select a number from 1 to 13, so please try again")
            choice = int(input("Please re-enter your choice: "))
# Start the Menu
menu()
