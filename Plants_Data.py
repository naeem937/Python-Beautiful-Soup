import requests
import bs4

res = requests.get('https://pfaf.org/user/plant.aspx?LatinName=Cercis+Canadensis')

soup = bs4.BeautifulSoup(res.text, 'lxml')

data = []

keys = ['CommonName','Family','USDAHardiness','KnownHazards','Habitats','Range','WeedPotential', 'Summary', 'PhysicalCharacterstics']

data += (soup.select('#ctl00_ContentPlaceHolder1_lblCommanName'))
data += (soup.select('#ctl00_ContentPlaceHolder1_lblFamily'))
data += (soup.select('#ctl00_ContentPlaceHolder1_lblUSDAhardiness'))
data += (soup.select('#ctl00_ContentPlaceHolder1_lblKnownHazards'))
data += (soup.select('#ctl00_ContentPlaceHolder1_txtHabitats'))
data += (soup.select('#ctl00_ContentPlaceHolder1_lblRange'))
data += (soup.select('#ctl00_ContentPlaceHolder1_lblWeedPotential'))
data += (soup.select('#ctl00_ContentPlaceHolder1_txtSummary'))
data += (soup.select('#ctl00_ContentPlaceHolder1_lblPhystatment'))

a = 0

for i in data:    
    print(keys[a],':')
    print(i.getText(), "\n\n")
    a+=1