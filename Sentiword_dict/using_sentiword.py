import pandas as pd

sentiword_dic = pd.read_csv('감성사전.txt', sep='\t', header=None, names=['word', 'polarity'])
idx = 0

for token in tokens: 
    sentiment = 0  
    for i in range(0, len(sentiword_dic)): 
        if sentiword_dic['word'][i] in token: 
            sentiment += int(sentiword_dic['polarity'][i])  
    df.loc[idx] = [token, sentiment]  
    idx += 1

def label_sentiment(sentiment):
    if sentiment > 0:
        return '긍정적'
    elif sentiment < 0:
        return '부정적'
    else:
        return '중립적'

# '감정' 컬럼을 추가
df['감정'] = df['sentiment'].apply(label_sentiment)

mid = len(df[df['감정'] == '중립적'])
neg = len(df[df['감정'] == '부정적'])
pos = len(df[df['감정'] == '긍정적'])
