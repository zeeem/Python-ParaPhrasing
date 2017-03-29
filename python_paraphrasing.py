#python34
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
import bs4 as bs
import urllib.request
import time

#function for js call
class Client(QWebPage):

	def __init__(self, url):
		self.app = QApplication(sys.argv)
		QWebPage.__init__(self)
		self.loadFinished.connect(self.on_page_load)
		self.mainFrame().load(QUrl(url))
		self.app.exec_()

	def on_page_load(self):
		self.app.quit()

def translate(targetLang,mainText):
	# targetLang = "zh-CN"
	# mainText = "main test text to paraphrase"
	url = "https://translate.google.com/#auto/" + targetLang + "/" + mainText
	client_response = Client(url)
	source = client_response.mainFrame().toHtml()
	soup = bs.BeautifulSoup(source, 'html.parser')
	result = soup.find("span", {"id":"result_box"})
	return result.text
#print (result.text)
def paraPhrase(givenText):
	newText = translate("en",translate("zh-CN",givenText))
	return (newText)

# textt = paraPhrase("")
# print (textt)