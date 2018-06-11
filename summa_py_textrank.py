from urllib.request import urlopen
from summa.summarizer import summarize 
from sys import argv
from bs4 import BeautifulSoup as bs
import PyPDF2
def from_link():
    page=urlopen(argv[1])
    soup=bs(page,'lxml')
    text=soup.find_all('p')
    text='\n'.join([ i.text for i in text])
    print(summarize(text,ratio=0.2))

def from_pdf():
    pdfdoc = open(argv[1], 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfdoc)
    count = pdfReader.numPages
    for i in range(count):
        page = pdfReader.getPage(i)
        print('Page Number: ',i,'\n')
        print(summarize(page.extractText(),ratio=0.2))
        print('\n\n')
def from_txt():
    file=open(argv[1],'r')
    text=file.read()
    print(summarize(text,ratio=0.2))
if __name__=="__main__":
    try:
        filetype = argv[2]
        if filetype=='url':
            from_link()
        elif filetype=='pdf':
            from_pdf()
        else:
            from_txt()
    except IndexError:
        print("\nUsage:\n \tsummarize 'http:// url.to.summarize' url \n or \n \tsummarize 'path/to/file/file.pdf' pdf \n or \n \tsummarize 'path/to/file/file.txt' txt ")
