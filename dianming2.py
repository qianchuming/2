f=open('C:/Users/user/Desktop/Walden.txt','r',encoding='utf-8')
line = f.read()
words = line.split()
new_words = []
for word in words:
    new_words.append(word.replace(',','').replace('.','').replace(':','').replace(';','').lower())
words_set = set(new_words)
words_dict= {}
for word in words_set:
    #print(word,words.count(word))
    words_dict[word] = new_words.count(word)
sorted(words_dict.items(),key=lambda x:x[1], reverse=True)
#print(words_dict.items())
