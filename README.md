# summarizer

An application of the summa module that implements TextRank module to create a commandline utility that quickly summarizes text, .docx , .pdf and urls. 

## Dependancies:
- Summa 
- PyPDF2
- BeautifulSoup4

## Usage:

````python
pip3 install summa
````
````bash
echo "alias summarize='python3 path/to/code/summa_py_textank.py ">> ~/.bash_profile
````
````bash
summarize 'http:// url.to.summarize' url
````
 or
 ````bash
summarize 'path/to/file/file.pdf' pdf
 ````
 or
  ````bash
summarize 'path/to/file/file.txt' txt
````
