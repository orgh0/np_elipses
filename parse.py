from stanfordcorenlp import StanfordCoreNlp
from nltk.tree import *
import re
import sentences

nlp = StanfordCoreNLP(r'../stanford-corenlp-full-2018-02-27)
        
def Np_Extractor(parsed_sentence, tree_struct):
    return list(y.subtrees(filter=lambda x: x.label()=='NP')

def Constituent_Checker(chunk):
    return len(chunk.subtrees(filter=lambda x: x.label()=='NNS' or 'NNP' or 'NN' or 'NNPS'))

def Chunk_Validity_Checker(chunk):
    return len(chunk.subtrees(filter=lambda x:x.label() == 'JJ' or 'DT' or 'CD'))

def main():
    final_list[]
    sentence = "Hey there this is a sentence"
    for sentence in sentences:
        x = nlp.dependency_parse(sentence)
        y = Tree.fromstring(x)
        NPs = NP_extractor(x, y)
        for NP in NPs:
            if Constituent_Checker(NP) <= 0 :
                if Chunk_Validity_Checker >= 0:
                    final_list.append(sentence)

if __name__== "__main__":
  main()

