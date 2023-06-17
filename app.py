from PyPDF2 import PdfReader
import re

reader = PdfReader("2012.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

new_text = re.compile(r'^\d{3} [A-Z].*')

for line in text.split('\n'):
    if new_text.match(line):
        print(line)
