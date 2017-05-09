'''
Jon

stretch_goal_a.py

'''

import sys
import histogram_main
import time

def remove_punctuation(words):
    # Initialize an empty Python dict
    histogram = {}
    punctuation_marks = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
    for mixed in words:
        # Manually check for internal punctuation
        if mixed[0] in punctuation_marks or mixed[-1] in punctuation_marks:
            word = "".join(w for w in mixed if w not in punctuation_marks)
        else:
            word = mixed
        histogram[word] = histogram.get(word, 0) + 1
    return histogram



if __name__ == '__main__':
    if len(sys.argv)==3:
        words = histogram_main.open_file(str(sys.argv[1]), str(sys.argv[2]))
    elif len(sys.argv)==2:
        words = histogram_main.open_file(str(sys.argv[1]))
    else:
        print("Please enter: python stretch_goal_a.py, filename.txt, [stop_file.txt]")

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
