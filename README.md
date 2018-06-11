# summarizer
    An application of the summa module that implements TextRank module to create a commandline utility that quickly summarizes text, .docx , .pdf and urls. 

## Usage:

````python
pip3 install summa
````
````bash
echo "alias summarize='python3 path/to/code/summa_py_textank.py >> ~/.bash_profile
````
````python
 	summarize 'http:// url.to.summarize' url
 or
 	summarize 'path/to/file/file.pdf' pdf
 or
 	summarize 'path/to/file/file.txt' txt
````
