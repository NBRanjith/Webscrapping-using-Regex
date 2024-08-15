from bs4 import BeautifulSoup
import re
import requests
import pandas as pd

url = 'http://analytictech.com/mb021/mlk.htm'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

speech1 = soup.find_all('p', soup)

for speech in speech1:
    speech.text
    print(speech)

speech2 = [speech.text for speech in speech1]

speech3 = ''.join(speech2)

speech4 = speech3.replace('\r\n', ' ')

speech5 = re.sub(r'[^\w\s]', '', speech4)

speech6 = speech5.lower()

speech6 = speech5.lower()

df = pd.DataFrame(speech7).value_counts()

df.to_csv(r'D:\MASTERS\pyth\Projects\Project6\mlkj_speech_count.csv', index_label='Word')