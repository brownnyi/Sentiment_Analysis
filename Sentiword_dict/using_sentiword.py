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
