#start here
#in order to use this you must have a 2.x version of Python
#you also need nltk: which stands for natural language toolkit


import nltk
sentence = """ insert sentence, or paragraph here """
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)


from collections import defaultdict
l = tagged
d = defaultdict(list)
for v,k in l:
  d[k].append(v)

#from here: d['part_of_speech']
#will return the words present
#search d['JJS']: highlight all red
#search d['RBS']: highlight all red
#search d['JJ']: highlight all green

#I could put this all in a textbox on a local webpage
#it would be in a file, editable

#thesis is here:modal auxiliary MD


#planned feature: detect homonyms. Homonyms indicate ambiguity.
#if I could find words not used correctly, that would be another tool.