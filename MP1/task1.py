import sys

import matplotlib.pyplot as plt
from collections import Counter
import json

# Load the data from Json file
data_list = json.load(open('goemotions.json','r'))

# Scaling the output graph
plt.rcParams["figure.autolayout"] = True
plt.rcParams['xtick.labelsize'] = 4.3

# Specifying each category to be selected from Json file
def emo_count():
    emotion_count = Counter(elem[1] for elem in data_list)
    # Iterator of tuples for each category
    ind, freq = zip(*emotion_count.most_common())
    # Plotting the graph
    plt.bar(ind, freq)
    # Save the graph in a pdf file formate
    plt.savefig('emation_count.pdf')
    plt.show()
    
def sent_count():
    sentiment_count = Counter(elem[2] for elem in data_list)
    # Iterator of tuples for each category
    ind, freq = zip(*sentiment_count.most_common())
    # Plotting the graph
    plt.bar(ind, freq)
    # Save the graph in a pdf file formate
    plt.savefig('sentiment_count.pdf')
    # Showing the plotted graph
    plt.show()

# Menu Selection
def menu(choice = None):
    print("************Welcome to Task-1 AI Classifier Demo**************")
    while choice != -1:
        choice = int(input("""
              1: Emotions Count
              2: Sentiment Count
              3: Exit

              Please enter your classifier choice: """))
        if choice == 1:
            emo_count()
        elif choice == 2:
            sent_count()
        elif choice == 3:
            sys.exit()
        else:
            print("You must only select a number from 1 to 3, so please try again")
            choice = int(input("Please re-enter your choice: "))
# Start the Menu
menu()
