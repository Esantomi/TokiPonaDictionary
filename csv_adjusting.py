# 긁어 온 파일 '단어', '뜻' 순서로 리스트에 넣기
f = open('words_raw.csv', 'rt', encoding = 'utf-8')

nimi = []
pilin = []

for line in f:
    # print(line)
    if line[0] in 'aeioumnptkswlj':
        nimi.append(line.strip())
    else:
        pilin.append(line.strip())

lipu_pona = []
for i, j in zip(nimi, pilin):
    lipu_pona.append(i)
    lipu_pona.append(j)

# print(lipu_pona)


# csv 형식에 맞는 파일 생성
import csv

with open('words_ordered.csv', 'w') as new_f:
    writer = csv.DictWriter(new_f, fieldnames = ["단어", "뜻"])
    writer.writeheader()
    for line in lipu_pona:
        # print(line)
        if ',' in line:
            a = line.replace(',', '/')
            if a[0] in 'aeioumnptkswlj':
                new_f.write(a + ',')
            else:
                new_f.write(a + '\n')
        else:
            if line[0] in 'aeioumnptkswlj':
                new_f.write(line + ',')
            else:
                new_f.write(line + '\n')

f.close()


# 전체 단어 목록
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