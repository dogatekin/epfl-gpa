import pdftotext
import re
import sys

# Load transcript
with open(sys.argv[1], "rb") as f:
    pdf = pdftotext.PDF(f)

# Read all the text into one string
content = "\n".join(pdf)

# Find the lines with course grades
results = re.findall(r'[a-z A-Z]+\d+.\d+ +(\d[.\d+]*) +(\d+) +\d+', content)

# Calculate GPA
total_points = total_credits = 0
for grade, credit in results:
    grade = float(grade)
    credit = float(credit)

    total_points += grade * credit
    total_credits += credit

# Print GPA to 2 decimal places
print('GPA: {:0.2f} / 6.00'.format(total_points / total_credits))