# EPFL GPA Calculator

As far as I can tell, your GPA is not reported anywhere on EPFL's online student information platform. To calculate it, you have to download your "Statement of Results" as a PDF and manually calculate your GPA by multiplying each course's grade with its credits, adding them up, and dividing the result to the total number of credits.

Because this annoys me so much, here is a simple script that does it automatically.


## Dependencies

[pdftotext](https://github.com/jalan/pdftotext)


## Usage

1. Download the ```calculate.py``` script.
2. Download your statement of results from IS-Academia.
3. Run the script and give the path to the results as an argument.

Example:
```bash
python calculate.py /Users/dogatekin/Downloads/transcript.pdf
```


## Q&A

1. Are you sure this works correctly?

No. The script relies on a PDF library that is not mine and also on my admittedly limited knowledge of regular expressions. Double check the result if you are putting your GPA on an important document (or better yet, improve my code and make it more robust). I deny all responsibility if you blindly trust this hacky script and it backfires horribly.

It seems to work fine on my transcript, though :)

2. Was it really worth it to write a script for something you have to do only once per semester and that takes less than 5 minutes each time?

Yes.
