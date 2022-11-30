<h2> List of students working on the project:</h2>

| Full Names    |  Github Usernames | StudentID |
| ------------- | ------------- | ------------- |
| Omar Mahmoud   |[@OmarHesham123](https://github.com/OmarHesham123)| 40158127 |
| Athanas Bakleh    |[@A-BAKLEH](https://github.com/A-BAKLEH)| 40093110 |
| Mohammad Aamir Parekh   |[@Ap2603](https://github.com/Ap2603)| 40136289 |

<h2> URL to the repository (private):</h2>
https://github.com/OmarHesham123/COMP472Project

<h2> How to run </h2>
TASK1.py:  
The file contains the extraction of the Reddit Posts as well as both labels. You will be shown a menu that asks you to select a number between 1-3 in order to identify whether emotion or sentiment counts to be generated into a PDF.

| Number   | Counts |
| - | ------------- |
| 1 | Emotions Count |
| 2 | Sentiment Count |
| 3 | Exit |


TASK2.py:  
You will be shown a menu that asks you to select a number between 1-12 in order to identify which classifier you wish to run with what percentage of split between the training and test sets. Numbers 1-6 will run the classifier with 80% of the data as the training set and 20% as the testing set, while numbers 7-12 will run the classifiers with 60% of the data as the training set and 40% of the data as the testing set. The numbers will represent the following:  

| Number   | Classifier |
| - | ------------- |
| 1 / 7 | BASE-MNB |
| 2 / 8 | BASE-DT |
| 3 / 9 | BASE-MLP |
| 4 / 10 | TOP-MNB |
| 5 / 11 | TOP-DT |
| 6 / 12 | TOP-MLP |  
  
 If you input any other number, the program will output an error and ask you to re-enter a valid input.
 
 
Metrics_task2.py: <br>
This file produces a confusion matrix with accuracy, precision, and recall numbers for both original set of splits as well as part 2.5 which has different splits and sizes of training sets. This could be done by running the code and it will automatically generate both metrics in performance and performance1 text files respectively.

TASK 3.py:  <br>
You will be shown a menu that asks you to select a number between 1-3 in order to show which feature to implement in the Word2Vec embeddings. Numbers 1-3 represents each feature which includes display tokens number in training set, average embedding words of a post, and the overall hit rates. However, both MLP parts appeared to have some issues while implementing them, so they are not displayed in the menu (3.5, 3.6, and 3.7). The numbers will represent the following:  

| Number   | Classifier |
| - | ------------- |
| 1 | Display tokens Number in training set |
| 2 | Average embedding words of a post |
| 3 | Overall hit rates |
   
If you input any other number, the program will output an error and ask you to re-enter a valid input.

Gigaword_300_model_task3.py:  <br>
This file is part 3.8 inside task3, so by choosing gigaword_300_model as our first pretrained embedding models, there will be also a number menu between 1-3, same as of Task3, in order to show which feature to implement in the Word2Vec embeddings concerning to this model specifically. Both MLP parts are also not implemented due to certain issues in their functions. 

Twitter_200_model_task3.py:  <br>
This file is part 3.8 inside task3, so by choosing twitter_200_model as our second pretrained embedding models, there will be also a number menu between 1-3, same as of Task3, in order to show which feature to implement in the Word2Vec embeddings concerning to this model specifically. Both MLP parts are also not implemented due to certain issues in their functions. 
