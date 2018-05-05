import nltk, re

from stanfordcorenlp import StanfordCoreNLP
from nltk.tree import *

import sentences

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

def main(sentences):
    final_set = set([])
    for sentence in sentences:
        if check_ones(sentence):
            final_set.add(sentence)
            continue
        if check_special_occurence(sentence, ["mine", "yours", "theirs", "hers"]):
            final_set.add(sentence)
            continue
        else:
            x = nlp.parse(sentence)
            y = Tree.fromstring(x)
            NPs = Extractor(y, ['NP', 'ADJP'])
            for NP in NPs:
                if Extractor(NP, ["JJ", "DT", "CD"]) and not Extractor(NP, ["NNS", "NNP", "NN", "NNPS",
                                                                                                "PRP"]):
                    final_set.add(sentence)
                    continue
                else:
                    continue
    print(final_set)
    print(len(final_set))

if __name__ == "__main__":
    from sentences import sentences as s
    result = main(s)
    print(result)
