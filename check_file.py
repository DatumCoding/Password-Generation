from essential_generators import DocumentGenerator
import jellyfish as jf
import random
sent = DocumentGenerator().sentence()
print(sent)
sent_list = sent.split()
sent_list = sent_list[0 : min(3 , len(sent_list))]
word_list = []
for word in sent_list:
    word_list.append(jf.match_rating_codex(word))
    if(random.getrandbits(1)):
        word_list.append(str(random.randint(0 , 9)))
password = "".join(word_list)
for i , char in enumerate(password):
    if char.isalpha() and random.getrandbits(1):
        password = password[0:i] + char.lower() + password[i + 1:]
print(password)
