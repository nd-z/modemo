from python_goose.goose import Goose

class ArticleCrawler(object):
	def __init__(self):
		self.goose = Goose()

	# grabs and processes the raw content from an article link
	# into a list of a list of sentences
	def url_content(self, url):
		a = self.goose.extract(url=url)
		u_txt = a.cleaned_text
		txt = u_txt.encode('ascii', 'ignore')
		txt = str(txt.decode('unicode_escape')).encode('utf-8')

		# now we have cleaned up the raw text; split into paragraphs
		paragraphs = txt.split('\n')
		temp = []

		for paragraph in paragraphs:
			if len(paragraph) != 0:
				temp.append(paragraph)

		paragraphs = temp

		# now we want to split each paragraph into sentences
		temp = []

		for paragraph in paragraphs:
			sentences = paragraph.split('.')
			temp2 = []

			for sentence in sentences:
				sentence = sentence.strip()
				if len(sentence) != 0:
					temp2.append(sentence)

			sentences = temp2
			temp.append(sentences)

		ret_content = temp

		return ret_content

