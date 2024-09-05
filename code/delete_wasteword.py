import pandas as pd
import re

def preprocess_text(text):
    text = text.strip()

    text = re.sub(r'[^\w\s]', '', text)

    text = re.sub(r'[^가-힣0-9\s]', '', text)

# 인터넷 용어 특성상 ㅋㅋ, ㄷㄷ 와 같은 반복되는 단어가 많이 발생
    text = re.sub(r'ㅋ{2,}', 'ㅋㅋ', text)
    text = re.sub(r'ㄷ{2,}', 'ㄷㄷ', text)

    text = re.sub(r'\s+', ' ', text)

    return text
