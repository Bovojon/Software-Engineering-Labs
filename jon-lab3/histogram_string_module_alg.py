'''
Jon

histogram_string_module_alg.py

'''

import sys
from string import punctuation
import histogram_main
import time


def remove_punctuation(words):
    # Initialize an empty Python dict
    histogram = {}
    words_new = []
    for mixed in words:
        # Get rid of internal punctuation
        word = mixed.strip(punctuation)
        histogram[word] = histogram.get(word, 0) + 1        # Add word as key to dictionary and its frequency as the dict value.
    return histogram

# Unit testing:
if __name__ == '__main__':
    if len(sys.argv)==3:
        words = histogram_main.open_file(str(sys.argv[1]), str(sys.argv[2]))
    elif len(sys.argv)==2:
        words = histogram_main.open_file(str(sys.argv[1]))
    else:
        print("Please enter: python histogram_string_module_alg.py, filename.txt, [stop_file.txt]")

    # Calculate time taken to remove punctuation
    start_time = time.time()
    histogram = remove_punctuation(words)
    end_time = time.time()
    total_time = end_time - start_time

    print("\n")
    print("Time taken to remove punctuation: ")
    print(total_time)
    print("\n")

    # Build the histogram
    first_10_list = histogram_main.get_top_words(histogram)
    ratios_list = histogram_main.normalize(first_10_list)
    histogram_main.build_histogram(ratios_list, first_10_list)
