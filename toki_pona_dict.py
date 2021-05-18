# 단어 csv 파일 가져오기
import csv

f = open('words.csv', 'r')
f_r = csv.reader(f)

nimi = []
pilin = []

for line in f_r:
    if line[0][0] in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        nimi.append(line)
    else:
        pilin.append(line)

for pair in zip(nimi, pilin):
    dict(zip(nimi, pilin))


# # 전체 단어 목록
# lipu_nimi = {'a':'감탄사 전반',\
#     'akesi':'파충류, 양서류, 징그러운 동물',\
#     'ala':'부정어, 아니, 영(0)',\
#     'alasa':'모으다, 사냥하다',\
#     'ale':'모든, 만물, 우주, 인생',\
#     'ali':'모든, 만물, 우주, 인생',\
#     'anpa':'아래, 바닥',\
#     'ante':'다른, 바꾸다'
#     'anu':'또는'
#     'awen':'남다, 머물다, 기다리다, 지키다',\
#     'e':'직접 목적어를 받는 단어',\
#     'en':'그리고',\
#     }

# print(lipu_nimi['a'])