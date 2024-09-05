!pip install konlpy
!git clone https://github.com/SOMJANG/Mecab-ko-for-Google-Colab.git
cd Mecab-ko-for-Google-Colab
!bash install_mecab-ko_on_colab_light_220429.sh

from konlpy.tag import Mecab, Komoran, Hannanum, Okt, Kkma

mecab = Mecab()
komoran = Komoran()
hannanum = Hannanum()
okt = Okt()
kkma = Kkma()

def get_tags(text, tagger):
    return tagger.pos(text)

def analyze_with_tagger(df, tagger):
    results = []
    for text in df['Reaction']:
        tags = get_tags(text, tagger)
        results.append(tags)
    return results

# precision_score, recall_score, f1_score 등을 사용하여 성능이 좋은 형태소 분석기 선택
