'''
Jon

histogram_manual_alpha_alg.py

'''

import sys
import histogram_main
import time


def remove_punctuation(words):
    # Initialize an empty Python dict
    histogram = {}

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for mixed_word in words:
        # Manually check if mixed_word has any internal punctuation
        if mixed_word[0] in letters and mixed_word[-1] in letters:
            word = mixed_word
        else:
            word = "".join(w for w in mixed_word if w in letters)
        histogram[word] = histogram.get(word, 0) + 1
    return histogram


if __name__ == '__main__':
    if len(sys.argv)==3:
        words = histogram_main.open_file(str(sys.argv[1]), str(sys.argv[2]))
    elif len(sys.argv)==2:
        words = histogram_main.open_file(str(sys.argv[1]))
    else:
        print("Please enter: python histogram_manual_alpha_alg.py, filename.txt, [stop_file.txt]")

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
