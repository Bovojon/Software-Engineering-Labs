'''
Jon

stretch_goal_c.py
WARNING - Code below does not run on terminal. Please run code below on Jupyter - explained in README.md

'''

import sys
import histogram_main
import histogram_string_module_alg
import matplotlib.pyplot as plt
import collections
%matplotlib inline


def draw_graph(freq_and_word):
    # Name axes and give title
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(r'$\mathrm{Histogram\ of\ the\ 10\ most\ common\ words} $')

    # Create new dictionary to contain top 10 frequent words
    dictionary = {}
    for pair in freq_and_word:
        dictionary[pair[1]] = pair[0]

    # Create histogram with matplotlib using the dictionary
    plt.bar(range(len(dictionary)), dictionary.values(), align='center')
    plt.xticks(range(len(dictionary)), dictionary.keys(), rotation=25)
    plt.show(block=True)
    plt.show()




if __name__ == '__main__':
    # Build the histogram based on file critique-of-reason.txt
    words = histogram_main.open_file('critique-of-reason.txt')
    histogram = histogram_string_module_alg.remove_punctuation(words)
    first_10_list = histogram_main.get_top_words(histogram)
    draw_graph(first_10_list)
