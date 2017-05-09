'''
Jon

histogram_main.py

'''

def open_file(filename, stopFile=None):
    words = []
    stop_words = []

    #Create a list of stop words from the given txt file
    if stopFile != None:
        with open (stopFile,"r") as stop_file:
            for line in stop_file:
                for w in line.split():
                    stop_words.append(w.lower())

    # Create a list of words that does not contain the stop words
    with open(filename, 'r') as fileName:
        for line in fileName:
            for word in line.split():
                if word not in stop_words:
                    words.append(word.lower())
    return words


def get_top_words(histogram):
    # Get the top 10 frequent words
    count_and_word_list = []
    for word, count in histogram.items():
        count_and_word_list.append([count, word])
    count_and_word_list.sort()
    count_and_word_list.reverse()
    first_10_list = count_and_word_list[:10]
    return first_10_list


def normalize(first_10_list):
    # Get the frequency count with the most number of decimal digits
    max_digits_int = first_10_list[0][0]
    max_digits_int_len = len(str(max_digits_int))

    # Find longest word
    max_string = 0
    for item in first_10_list:
        if len(item[1]) > max_string:
            max_string = len(item[1])

    # Calculate the ratio of the length of the stars to display
    longest_star_line = 80 - 13 - 6 - max_string - max_digits_int_len # 80 is max char length, 13 is length for longest word, 6 is length of longest integer digit
    ratio_for_top_line = longest_star_line/max_digits_int
    ratios_list = []
    for i in first_10_list:
        ratio = i[0] * ratio_for_top_line
        ratios_list.append(int(ratio))

    return ratios_list



def build_histogram(ratios_list, first_10_list):
    # Create the number of stars according to frequency
    stars_list = []
    for r in ratios_list:
        stars = '*'*r
        stars_list.append(stars)
    i = 0
    for pair in first_10_list:
        print("%-13s %6d %s" % (pair[1], pair[0], stars_list[i])) # 13 is length for longest word, 6 is length of longest integer digit
        i += 1
