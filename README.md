# 자연어 처리 형태소 분석기인 Konlpy Mecab 활용하여 문장의 감정을 분석하는 프로젝트

## 형태소 선택
![image](https://github.com/user-attachments/assets/64cb1a6e-8c0b-4ae9-98a3-7ffa3ad9504c)
- 인터넷 용어 특성상 불규칙한 띄어쓰기, 유행어, 줄임말 등을 예측에 있어서 성능이 뛰어난 모델을 선정
- 예측률이 가장 높은 mecab 선택

## 데이터셋
![image](https://github.com/user-attachments/assets/239e2036-cac5-4ff8-a1bf-a2bfa358881a)

- 이전에 제작해둔 [BS_Scraper](https://github.com/brownnyi/BS_scraper)를 활용하여 인벤 사이트의 유저의 글들을 스크래핑 하여 감정분석 실시

## 시각화
![image](https://github.com/user-attachments/assets/ec66f728-058e-47a1-a198-ba2c09857feb)

- 부정 라벨링된 문장들을 WordCloud를 통해 시각화
