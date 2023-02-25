from bs4 import BeautifulSoup
import  nltk
nltk.download('stopwords')
from nltk.corpus import  stopwords
request=open('1.txt','r')
html=request.read()
soup=BeautifulSoup(html,'html5lib')
text=soup.getText(strip=True)
tokens=[t for t in text.split()]
sr=stopwords.words('english')
clean_token=tokens[:]
for token in tokens:
    if token in stopwords.word('english'):
        clean_token.remove(token)
freq=nltk.FreqDist(clean_token)
for key,val in freq.items():
    print(str(key)+':'+str(val))
freq.plot(20,cumulative=False
