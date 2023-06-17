import pdfplumber as pdfP
import re 


with pdfP.open('2012.pdf') as pdf:
    page = pdf.pages[0]
    text = page.extract_text()

# VARIABLES
preguntas = []
respuestas = []

# PREGUNTAS
preguntas_re = re.compile(r'^\d{1}..*')
for line in text.split('\n'):
    if preguntas_re.match(line):
        print(line)
        preguntas.append(line) # GUARDANDO PREGUNTAS

# RESPUESTAS
respuestas_re = re.compile(r'^\d{0}[a-d][)]')
for line in text.split('\n'):
    if respuestas_re.match(line):
        respuestas.append(line) # GUARDANDO RESPUESTAS