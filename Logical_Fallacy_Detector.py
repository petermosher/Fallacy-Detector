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
#my friend did exactly what I wanted to do with the certain website.. highlight stuff on the website, highlight matches. That is why I am not so far along. I let him carry. I let him carry twice. Once in Databases. Once in Operating Systems. But I didn't care for those projects too much anyway. I wish I had understood how he made that website though.
#but he built the website himself. so... how does this work out? he built his own database. What i want to do, is do this all on the fly. So there's a difference. I could however do what he did, and make it on the fly... eventually. 


#planned feature: detect homonyms. Homonyms indicate ambiguity.
#if I could find words not used correctly, that would be another tool.