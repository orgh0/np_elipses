import nltk, re

from stanfordcorenlp import StanfordCoreNLP
from nltk.tree import *
from string import punctuation

import sentences1
from sentence_tester import sentences as s


nlp = StanfordCoreNLP(r'../stanford-corenlp-full-2018-02-27')

def check_special_occurence(sentence, word_list):
    sentence_word_list = re.sub("[^\w]", " ",  sentence).split()
    return bool(set(sentence_word_list) & set(word_list))


def check_ones(sentence):
    check_list = ['one', 'ones']
    check_tag_list = [('one', 'NN'), ('ones', 'NNS')]
    text = nltk.word_tokenize(sentence)
    if set(check_list).issubset(set(text)):
        text_tagged = nltk.pos_tag(text)
        if set(check_tag_list).issubset(set(text_tagged)):
            return true
        else:
            return false
                
def Extractor(parsed_tree, label_list):
    return list(parsed_tree.subtrees(filter=lambda x: x.label() in label_list))


def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

def main(sentences):
    print(len(sentences))
    print("this is the length ^^")
    final_set = set([])
    for sentence in sentences:
        sentence = strip_punctuation(sentence)
        if check_ones(sentence):
            final_set.add(sentence)
            print("RESULT :", sentence, NP)
            continue
        if check_special_occurence(sentence, ["mine", "yours", "theirs", "hers"]):
            final_set.add(sentence)
            print("RESULT :", sentence, NP)
            continue
        else:
            if sentence and len(sentence.split()) < 25:
                # print(sentence)
                x = nlp.parse(sentence)
                y = Tree.fromstring(x)
                NPs = Extractor(y, ['NP', 'ADJP'])
                for NP in NPs:
                    if Extractor(NP, ["JJ", "DT", "CD"]) and not Extractor(NP, ["NNS", "NNP", "NN", "NNPS",
                                                                                    "PRP"]):
                        final_set.add(sentence)
                        print("RESULT :", sentence, NP)
                        # print("this is the NP")
                
    print(final_set)
    print(len(final_set))

if __name__ == "__main__":
    result = main(s)
    print(result)
