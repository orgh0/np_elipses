import spacy

nlp = spacy.load('en')
sentence = "Some children like football and some  don't"

def calculate_noun_chunks(doc):
    np = []
    for np_chunk in doc.noun_chunks:
        np.append(np_chunk.text)
    print("the np list is ", np)
    return np   


def parse(line):
    doc = nlp(line)
    np_licensors = []
    np = calculate_noun_chunks(doc) ##Gets all the noun chunks in the sentences in a list
    for token in doc: #for every token check if token lies in [jj, dt, cd]
        # print("this is the token under consideration", token.text)
        if set(['JJ', 'DT', 'CD']) > set(list(token.tag_.split(" "))):
            np_licensors.append(token)
        else:
            print("Not applicabe token is:", token.text, token.tag_)
    for np_tokens in np_licensors:
        search_for_np_chunk_with(np_tokens, np) 


def search_for_np_chunk_with(token, np_chunks_list):
    for np_chunk in np_chunks_list:
        if set(np_chunk.split()) > set(list(token.text.split(" "))): ##checking if the token is in the np chunk
            list_of_tokens = np_chunk.split() 
            if check_for_same_next_utterance(list_of_tokens, token):
                print("Noun head found, not npe", token.text, np_chunk)
                break
            else:
                continue
        else:
            print("not in this np chunk", np_chunk)
            continue
    # print("clear case of npe")


def check_for_same_next_utterance(list_of_tokens, token):
    neighbour_in_chunk = list_of_tokens[list_of_tokens.index(token.text) + 1]
    if neighbour_in_chunk == token.nbor(1).text:
        return True
    else:
        return False

parse(sentence)
