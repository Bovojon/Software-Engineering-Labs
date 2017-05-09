# Description of Files

* `histogram_main.py` contains the reused code to build the histograms. All the algorithms share this code as the only area they differ in is in removing the punctuation marks.

* `histogram_string_module_alg.py` contains Algorithm 1 - using string module. To run it, type into the command line:
`python histogram_string_module_alg.py, filename.txt, [stop_file.txt]`

* `histogram_manual_alpha_alg.py` contains Algorithm 2 - using manually checking for alphabets. To run it, type into the command line:
`python histogram_manual_alpha_alg.py, filename.txt, [stop_file.txt]`

* `stretch_goal_a.py` contains Algorithm 3 - using manually checking for punctuation. To run it, type into the command line:
`python stretch_goal_a.py, filename.txt, [stop_file.txt]`

* `stretch_goal_b.py` - The program works only with URL links that are encoded in UTF-8. Under the scope of this project I believe that that is sufficient. To run it, type into the command line:
`python stretch_goal_b.py, URL`

* `stretch_goal_c.py` - The code for `stretch_goal_c` works perfectly well in a new Python 3 notebook on Jupyter. The new notebook has to be opened in the same folder as this project and the text file `critique-of-reason.txt` has to already be downloaded in the folder. Under the scope of this project I was only able to test it as described.



>> Notes:
* I made sure to carefully name all my variables and functions so that I could minimize the use of comments. Hence I believe that I have added sufficient comments in all my files.
* The only aspect of my code that I was able to appropriately test under the scope of this lab was the timing, and because it did not take much lines of code, I included it into the appropriate files.
* There is some code repeated but under the time scope of this project I was not able to moduralize it.
