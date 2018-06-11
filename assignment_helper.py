from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from summa.summarizer import summarize
from sys import argv
import requests
from lxml import html
import time
def summarize_link(link):
    ''' Here link is an URL.'''
    try:
        page = urlopen(link)
        soup = bs(page,'lxml')
        text = soup.find_all('p')
        text = '\n'.join([i.text for i in text])
        return summarize(text, ratio=0.2)
    except:
        return ''

def search(keywords, max_results=None):
	url = 'https://duckduckgo.com/html/'
	params = {
		'q': keywords,
		's': '0',
	}

	yielded = 0
	while True:
		res = requests.post(url, data=params)
		doc = html.fromstring(res.text)

		results = [a.get('href') for a in doc.cssselect('#links .links_main a')]
		for result in results:
			yield result
			time.sleep(0.1)
			yielded += 1
			if max_results and yielded >= max_results:
				return

		try:
			form = doc.cssselect('.results_links_more form')[-1]
		except IndexError:
			return
		params = dict(form.fields)

query = argv[1]
summarized_data = []
fw = open(query,'w')
for link in search(query,10):
    summarized_data.append(summarize_link(link))
fw.write('\n\n\n'.join(summarized_data))
