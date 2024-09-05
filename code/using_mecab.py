from konlpy.tag import Mecab

mecab = Mecab()

tokens = [mecab.morphs(word) for word in df['content']]

tokens = list(map(lambda x : " ".join(x), tokens))
