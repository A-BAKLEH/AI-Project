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
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

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

# Task 2.3.1 (NB)

corpusPrompt = np.array(prompt_trainingData)
corpusSentiment = np.array(sentiment_trainingData)
corpusEmotion = np.array(emotions_trainingData)

Xprompt = vectorizer.fit_transform(corpusPrompt)
ySentiment = corpusSentiment
yEmotion = corpusEmotion
# print(ySentiment.toarray())

classifier = MultinomialNB()
modelNB_sentiment = classifier.fit(Xprompt, ySentiment)
modelNB_emotions = classifier.fit(Xprompt,yEmotion)

prompt_testData = vectorizer.transform(np.array(prompt_testingData))

predict_sentiment = modelNB_sentiment.predict(prompt_testData)
predict_emotion = modelNB_emotions.predict(prompt_testData)

# print(predict_emotion)
# print(emotions_testingData)


# Task 2.3.2 (DT)

dtc = tree.DecisionTreeClassifier()
modelTree_sentiment = dtc.fit(Xprompt,ySentiment)
modelTree_emotion = dtc.fit(Xprompt,yEmotion)

treePredict_sentiment = modelTree_sentiment.predict(prompt_testData)
treePredict_emotion = modelTree_emotion.predict(prompt_testData)

# print(treePredict_sentiment)
# print(sentiment_testingData)

# Task 2.3.3 (MLP) --> not accurate

mlp_sentiment = MLPClassifier(max_iter=1)
mlp_emotion = MLPClassifier(max_iter=1)
modelMLP_sentiment = mlp_sentiment.fit(Xprompt,ySentiment)
modelMLP_emotion = mlp_emotion.fit(Xprompt,yEmotion)

mlpPredict_sentiment = modelMLP_sentiment.predict(prompt_testData)
mlpPredict_emotion = modelMLP_emotion.predict(prompt_testData)

# print(mlpPredict_emotion)
# print(mlpPredict_sentiment)
# print(emotions_testingData)

# Task 2.3.4 (TOP MNB) --> Not accurate Warning because of alpha value = 0 in parameters

gridTopMNB_sentiment = GridSearchCV(classifier, parametersNB)
gridTopMNB_emotion = GridSearchCV(classifier, parametersNB)

modelTopMNB_sentiment = gridTopMNB_sentiment.fit(Xprompt, ySentiment)
modelTopMNB_emotion = gridTopMNB_emotion.fit(Xprompt, yEmotion)

predictTopMNB_sentiment = modelTopMNB_sentiment.predict(prompt_testData)
predictTopMNB_emotion = modelTopMNB_emotion.predict(prompt_testData)

# print(predictTopMNB_sentiment)
# print(predictTopMNB_emotion)
# print(emotions_testingData)
# print(sentiment_testingData)

# Task 2.3.5 (TOP DT) --> Not accurate and takes a lot of time 7aywan

gridTopDT_sentiment = GridSearchCV(dtc, parametersDT)
gridTopDT_emotion = GridSearchCV(dtc, parametersDT)

modelTopDT_sentiment = gridTopDT_sentiment.fit(Xprompt, ySentiment)
modelTopDT_emotion = gridTopDT_emotion.fit(Xprompt, yEmotion)

predictTopDT_sentiment = modelTopDT_sentiment.predict(prompt_testData)
predictTopDT_emotion = modelTopDT_emotion.predict(prompt_testData)

#print(predictTopDT_sentiment)
# print(predictTopDT_emotion)
# print(emotions_testingData)
#print(sentiment_testingData)

# Task 2.3.6 (TOP MLP)

gridTopMLP_sentiment = GridSearchCV(mlp_sentiment, parametersMLP)
gridTopMLP_emotion = GridSearchCV(mlp_emotion, parametersMLP)

modelTopMLP_sentiment = gridTopMLP_sentiment.fit(Xprompt, ySentiment)
modelTopMLP_emotion = gridTopMLP_emotion.fit(Xprompt, yEmotion)

predictTopMLP_sentiment = modelTopMLP_sentiment.predict(prompt_testData)
predictTopMLP_emotion = modelTopMLP_emotion.predict(prompt_testData)

#print(predictTopMLP_sentiment)
#print(predictTopMLP_emotion)
#print(emotions_testingData)
#print(sentiment_testingData)

# Task 2.4 (Metrics)
f = open("performance.txt","a")
f.write(str(classifier)+"\n"+str(classification_report(emotions_testingData,predict_emotion))+"\n"+str(confusion_matrix(emotions_testingData,predict_emotion))+"\n\n")
f.write(str(dtc)+"\n"+str(classification_report(emotions_testingData,treePredict_emotion))+"\n"+str(confusion_matrix(emotions_testingData,treePredict_emotion))+"\n\n")
f.write(str(mlp_emotion)+"\n"+str(classification_report(emotions_testingData,mlpPredict_emotion))+"\n"+str(confusion_matrix(emotions_testingData,mlpPredict_emotion))+"\n\n")
f.write(str(gridTopMNB_emotion)+"\n"+str(classification_report(emotions_testingData,predictTopMNB_emotion))+"\n"+str(confusion_matrix(emotions_testingData,predictTopMNB_emotion))+"\n\n")
f.write(str(gridTopDT_emotion)+"\n"+str(classification_report(emotions_testingData,predictTopDT_emotion))+"\n"+str(confusion_matrix(emotions_testingData,predictTopDT_emotion))+"\n\n")
f.write(str(gridTopMLP_emotion)+"\n"+str(classification_report(emotions_testingData,predictTopMLP_emotion))+"\n"+str(confusion_matrix(emotions_testingData,predictTopMLP_emotion))+"\n\n")
f.close()

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

# 2.5 (Naive-Bayes)
corpusPrompt1 = np.array(prompt_trainingData1)
corpusSentiment1 = np.array(sentiment_trainingData1)
corpusEmotion1 = np.array(emotions_trainingData1)

Xprompt1 = vectorizer.fit_transform(corpusPrompt1)
ySentiment1 = corpusSentiment1
yEmotion1 = corpusEmotion1

classifier1 = MultinomialNB()
modelNB_sentiment1 = classifier1.fit(Xprompt1, ySentiment1)
modelNB_emotions1 = classifier1.fit(Xprompt1,yEmotion1)

prompt_testData1 = vectorizer.transform(np.array(prompt_testingData1))
predict_sentiment1 = modelNB_sentiment1.predict(prompt_testData1)
predict_emotion1 = modelNB_emotions1.predict(prompt_testData1)

# print(predict_emotion1)
# print(emotions_testingData1)

# 2.5 (DT)
dtc1 = tree.DecisionTreeClassifier()
modelTree_sentiment1 = dtc1.fit(Xprompt1,ySentiment1)
modelTree_emotion1 = dtc1.fit(Xprompt1,yEmotion1)

treePredict_sentiment1 = modelTree_sentiment1.predict(prompt_testData1)
treePredict_emotion1 = modelTree_emotion1.predict(prompt_testData1)

# print(treePredict_sentiment1)
# print(sentiment_testingData1)


# Task 2.5 (MLP) --> not accurate
mlp_sentiment1 = MLPClassifier(max_iter=1)
mlp_emotion1 = MLPClassifier(max_iter=1)
modelMLP_sentiment1 = mlp_sentiment1.fit(Xprompt1,ySentiment1)
modelMLP_emotion1 = mlp_emotion1.fit(Xprompt1,yEmotion1)

mlpPredict_sentiment1 = modelMLP_sentiment1.predict(prompt_testData1)
mlpPredict_emotion1 = modelMLP_emotion1.predict(prompt_testData1)

# print(mlpPredict_emotion1)
# print(mlpPredict_sentiment1)
# print(emotions_testingData1)

# Task 2.5 (TOP MNB) --> Not accurate Warning because of alpha value = 0 in parameters

gridTopMNB_sentiment1 = GridSearchCV(classifier, parametersNB)
gridTopMNB_emotion1 = GridSearchCV(classifier1, parametersNB)

modelTopMNB_sentiment1 = gridTopMNB_sentiment1.fit(Xprompt, ySentiment)
modelTopMNB_emotion1 = gridTopMNB_emotion1.fit(Xprompt1, yEmotion1)

predictTopMNB_sentiment1 = modelTopMNB_sentiment1.predict(prompt_testData)
predictTopMNB_emotion1 = modelTopMNB_emotion1.predict(prompt_testData1)

# print(predictTopMNB_sentiment1)
# print(predictTopMNB_emotion1)
# print(emotions_testingData1)
# print(sentiment_testingData1)
#
# Task 2.5 (TOP DT) --> Not accurate and takes a lot of time 7aywan
#
gridTopDT_sentiment1 = GridSearchCV(dtc1, parametersDT)
gridTopDT_emotion1 = GridSearchCV(dtc1, parametersDT)

modelTopDT_sentiment1 = gridTopDT_sentiment1.fit(Xprompt, ySentiment)
modelTopDT_emotion1 = gridTopDT_emotion1.fit(Xprompt1, yEmotion1)

predictTopDT_sentiment1 = modelTopDT_sentiment1.predict(prompt_testData)
predictTopDT_emotion1 = modelTopDT_emotion1.predict(prompt_testData1)

# print(predictTopDT_sentiment1)
# print(predictTopDT_emotion1)
# print(emotions_testingData1)
# print(sentiment_testingData1)

# Task 2.5 (TOP MLP)

gridTopMLP_sentiment1 = GridSearchCV(mlp_sentiment1, parametersMLP)
gridTopMLP_emotion1 = GridSearchCV(mlp_emotion1, parametersMLP)

modelTopMLP_sentiment1 = gridTopMLP_sentiment1.fit(Xprompt1, ySentiment1)
modelTopMLP_emotion1 = gridTopMLP_emotion1.fit(Xprompt1, yEmotion1)

predictTopMLP_sentiment1 = modelTopMLP_sentiment1.predict(prompt_testData1)
predictTopMLP_emotion1 = modelTopMLP_emotion1.predict(prompt_testData1)

# print(predictTopMLP_sentiment1)
# print(predictTopMLP_emotion1)
# print(emotions_testingData1)
# print(sentiment_testingData1)

# Gathering metrics for task 2.5
f1 = open("performance1.txt","a")
f1.write(str(classifier1)+"\n"+str(classification_report(emotions_testingData1,predict_emotion1))+"\n"+str(confusion_matrix(emotions_testingData1,predict_emotion1))+"\n\n")
f1.write(str(dtc1)+"\n"+str(classification_report(emotions_testingData1,treePredict_emotion1))+"\n"+str(confusion_matrix(emotions_testingData1,treePredict_emotion1))+"\n\n")
f1.write(str(mlp_emotion1)+"\n"+str(classification_report(emotions_testingData1,mlpPredict_emotion1))+"\n"+str(confusion_matrix(emotions_testingData1,mlpPredict_emotion1))+"\n\n")
f1.write(str(gridTopMNB_emotion1)+"\n"+str(classification_report(emotions_testingData1,predictTopMNB_emotion1))+"\n"+str(confusion_matrix(emotions_testingData1,predictTopMNB_emotion1))+"\n\n")
f1.write(str(gridTopDT_emotion1)+"\n"+str(classification_report(emotions_testingData1,predictTopDT_emotion1))+"\n"+str(confusion_matrix(emotions_testingData1,predictTopDT_emotion1))+"\n\n")
f1.write(str(gridTopMLP_emotion1)+"\n"+str(classification_report(emotions_testingData1,predictTopMLP_emotion1))+"\n"+str(confusion_matrix(emotions_testingData1,predictTopMLP_emotion1))+"\n\n")
f1.close()
