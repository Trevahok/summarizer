# summarizer

An application of the summa module that implements TextRank module to create a commandline utility that quickly summarizes text, .docx , .pdf and urls. 
Using the same module, implementing a web scraper that gets the top hits for a query and summarizes the individual pages to create a raw document to start your assignments with.  

## Dependancies:
- Summa 
- PyPDF2
- BeautifulSoup4
- Lxml
- Requests


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
--------
For collecting information from the web results of DuckDuckGo and then summarizing the result: 
````python
python3 assignment_helper.py 'topic to search for'
````
