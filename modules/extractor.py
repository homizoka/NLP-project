# extractor.py
# named entity recognition, currently unused.

import nltk
 
with open('para.txt', 'r') as f:
   sample = f.read()
    

sentences = nltk.sent_tokenize(sample)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = nltk.batch_ne_chunk(tagged_sentences, binary=True)
 

def extract_entity_names(t):
    entity_names = []
    
    if hasattr(t, 'node') and t.node:
        if t.node == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
                
    return entity_names
 
entity_names = []
for tree in chunked_sentences:
    # Print results per sentence
    # print extract_entity_names(tree)
    for node in tree:
      print node
    entity_names.extend(extract_entity_names(tree))
 
# Print all entity names
#print entity_names
 
# Print unique entity names
print set(entity_names)

wantset = set(['PRP','VB','VBN','NN','NNS','CD'])


for (x,y) in tagged_sentences[0]:
  if y in wantset:
    entity_names.append(x)


print entity_names