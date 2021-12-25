import numpy as np
import konlpy

##########데이터 로드

x_data = np.array([
    #부정
    '스토리가 진짜 너무 노잼',
    '심오한 똥이란 말이 딱이다',
    '쓰레기같은 영화 ㄹㅇ 시간아깝다',
    '점도 아깝다 ㄹㅇ쓰레기 영화',
    '이 드러운 기분을 어쩌지',
    #긍정
    '이건 명작임',
    '이런 느낌 영화 좋아요',
    '죽기전에 봐야할 영화',
    '뻔한 로코가아님 대사가 아주 좋아요',
    '안봤으면 후회했을거같다감동이다'
])

##########데이터 분석

##########데이터 전처리

#텍스트 정제 (형태소 분석)
for i, document in enumerate(x_data):
    okt = konlpy.tag.Okt()
    clean_words = []
    for word in okt.pos(document, stem=True): #어간 추출
        if word[1] in ['Noun', 'Verb', 'Adjective']: #명사, 동사, 형용사
            clean_words.append(word[0])
    print(clean_words) #['스토리', '진짜', '노잼']
    document = ' '.join(clean_words)
    print(document) #스토리 진짜 노잼
    x_data[i] = document
print(x_data)