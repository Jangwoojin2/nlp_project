from soynlp.hangle._hangle import decompose
import re


doublespace_pattern = re.compile('\s+')

def jamo_sentence(sent):

    def transform(char):
        if char == ' ':
            return char
        cjj = decompose(char)
        if len(cjj) == 1:
            return cjj
        cjj_ = ''.join(c if c != ' ' else '-' for c in cjj)
        return cjj_

    sent_ = ''.join(transform(char) for char in sent)
    sent_ = doublespace_pattern.sub(' ', sent_)
    return sent_

s = re.compile('[^ㄱ-힣 ]')
t = re.compile('ㆍ')
with open("./req_jamo_corpus.txt",'w') as wf:    
    for x in text:
        x = re.sub(s,"",x)
        x = x.strip()
        x = re.sub(t,"",x)
        # print(x)
        jamo = jamo_sentence(x)
        # print(jamo)
        wf.write(jamo+'\n')
                                                                                           