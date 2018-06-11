from sys import argv
from summa.summarizer import summarize
import PyPDF2
pdfdoc = open(argv[1], 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfdoc)
count = pdfReader.numPages
for i in range(count):
    page = pdfReader.getPage(i)
    print('Page Number: ',i,'\n')
    print(summarize(page.extractText(),ratio=0.2))
    print('\n\n')
