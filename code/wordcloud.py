import re
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk

# 불용어 리스트 불러오기
nltk.download('stopwords')
from nltk.corpus import stopwords
# 한글 특성상 nltk 불용어 리스트로도 stopwords 처리가 잘 되지 않아 간단한 불용어 리스트 구축
# Wordcloud로 시각화 한 뒤 미처 제거하지 못한 stopwords 추가해가며 제거
stop_words = set([
    '이', '그', '저', '에서', '의', '가', '을', '를', '에', '은', '는', '와', '과', '도', '으로', '하다'
, '허들', '허들이','허들을','허들은','수','너무','더','좀','많이','너무','결국','차','다','허들도','근데','있는','진짜','그냥','이제','개','대한','지금','기존',
    '하고','그리고'])

# 불필요한 기호와 숫자 제거하고 소문자로 변환
cleaned_text = ' '.join(results).lower()
cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)  # 구두점 제거
cleaned_text = re.sub(r'\d+', '', cleaned_text)  # 숫자 제거

# 단어 리스트로 변환
word_list = cleaned_text.split()

#stopwords 제거
filtered_words = [word for word in word_list if word not in stop_words]

# 단어 빈도 계산
word_freq = Counter(filtered_words)

# 1. 워드클라우드 시각화
wordcloud = WordCloud(font_path='NEXONLv1GothicRegular.ttf', width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
