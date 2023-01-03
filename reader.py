import pyttsx3
import PyPDF2

# load the Raven PDF file
book = open('Raven.pdf', 'rb')

Reader = PyPDF2.PdfReader(book)

# get number of pages in the PDF
pages = len(Reader.pages)

read_out = pyttsx3.init()

for num in range(1, pages):
    page = Reader.pages(num)
    text = page.extractText()
    read_out.say(text)