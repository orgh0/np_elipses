from stanfordcorenlp import StanfordCoreNLP
from nltk.tree import *


nlp = StanfordCoreNLP(r'../stanford-corenlp-full-2018-02-27')


def Extractor(parsed_tree, label_list):
    return list(parsed_tree.subtrees(filter=lambda x: x.label() in label_list))

def main(sentences):
    final_set = set([])
    for sentence in sentences:
        x = nlp.parse(sentence)
        print(x)
        y = Tree.fromstring(x)
        NPs = Extractor(y, ['NP', 'ADJP'])
        for NP in NPs:
            if not Extractor(NP, ["JJ", "DT", "CD"]) and Extractor(NP, ["NNS", "NNP", "NN", "NNPS"]):
                pass
            else:
                final_set.add(sentence)
    return final_set

if __name__ == "__main__":
    from sentences import sentences as s
    result = main(s)
    print(result)
