'''
Jon

stretch_goal_b.py

'''

from pyparsing import SkipTo, oneOf, StringEnd, FollowedBy
from urllib.request import urlopen
import sys
import histogram_main
import histogram_string_module_alg

def build_histogram_from_url(input_url):
    url_data = str(urlopen(input_url).read(), "utf-8")

    # Write data from url to a file
    file_write = open("url_file.dat", "w")
    file_write.write(url_data)
    file_write.close()
    return("url_file.dat")


if __name__ == '__main__':
    if len(sys.argv)==2:
        textFile = build_histogram_from_url(sys.argv[1])
        words = histogram_main.open_file(textFile)
    else:
        print("Please enter: python stretch_goal_b.py, URL")

    # Build the histogram
    histogram = histogram_string_module_alg.remove_punctuation(words)
    first_10_list = histogram_main.get_top_words(histogram)
    ratios_list = histogram_main.normalize(first_10_list)
    histogram_main.build_histogram(ratios_list, first_10_list)
