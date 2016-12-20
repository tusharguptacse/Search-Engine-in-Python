import glob
global inverted_dict_unigram
inverted_dict_unigram = {}
global inverted_dict_bigram
inverted_dict_bigram = {}
global inverted_dict_trigram
inverted_dict_trigram = {}

def trigrams(file):
	filename = open(file,'r')
	current_file = []
	var2 = filename.read()
	var = var2.split()
	for i in var:
		current_file.append(i)
	docid = var[0]

	for i in xrange(1,(len(current_file)-2)):
		token1 = current_file[i]
		token2 = current_file[i+1]
		token3 = current_file[i+2]
		ngram3 = (token1,token2,token3)

		if ngram3 in inverted_dict_trigram:
			a = inverted_dict_trigram[ngram3]
			if docid in a:
				inverted_dict_trigram[ngram3][docid] += 1
			else:
				inverted_dict_trigram[ngram3][docid] = 1 
		else:
			inverted_dict_trigram[ngram3] = {}
			inverted_dict_trigram[ngram3][docid] = 1

def bigrams(file):
	filename = open(file,'r')
	current_file = []
	var2 = filename.read()
	var = var2.split()
	for i in var:
		current_file.append(i)
	docid = var[0]

	for i in xrange(1,(len(current_file)-1)):
		token1 = current_file[i]
		token2 = current_file[i+1]
		ngram2 = (token1,token2)

		if ngram2 in inverted_dict_bigram:
			a = inverted_dict_bigram[ngram2]
			if docid in a:
				inverted_dict_bigram[ngram2][docid] += 1
			else:
				inverted_dict_bigram[ngram2][docid] = 1 
		else:
			inverted_dict_bigram[ngram2] = {}
			inverted_dict_bigram[ngram2][docid] = 1

def unigrams(file):
	filename = open(file,'r')
	current_file = []
	var2 = filename.read()
	var = var2.split()
	for i in var:
		current_file.append(i)
	docid = var[0]

	for i in xrange(1,len(current_file)):
		token = current_file[i]
		if token in inverted_dict_unigram:
			a = inverted_dict_unigram[token]
			if docid in a:
				inverted_dict_unigram[token][docid] += 1
			else:
				inverted_dict_unigram[token][docid] = 1 
		else:
			inverted_dict_unigram[token] = {}
			inverted_dict_unigram[token][docid] = 1


for filename in glob.glob('Web Pages/*.txt'):
 	unigrams(filename)
	bigrams(filename)
	trigrams(filename)

f = open("Inverted_Index/Inverted Index- Unigrams.txt" , "w")
for key,value in inverted_dict_unigram.items():
	f.write('%s: %s\n' % (key, value))

print 'Inverted Index of Unigrams written to file.'

f = open("Inverted_Index/Inverted Index- Bigrams.txt" , "w")
for key,value in inverted_dict_bigram.items():
	f.write('%s: %s\n' % (key, value))

print 'Inverted Index of Bigrams written to file.'

f = open("Inverted_Index/Inverted Index- Trigrams.txt" , "w")
for key,value in inverted_dict_trigram.items():
	f.write('%s: %s\n' % (key, value))

print 'Inverted Index of Trigrams written to file.'

doc_freq_uni = {}

for term,name in zip(inverted_dict_unigram.itervalues(), inverted_dict_unigram.iteritems()):
	counter1 = 0
	for val in term.values():
		counter1 = counter1 + 1
	doc_freq_uni[str(name)] = counter1


f = open("Document_Frequency/Document Frequency- Unigrams.txt" , "w")
for key in sorted(doc_freq_uni):
	f.write('%s : %s\n' % (key, doc_freq_uni[key]))

print 'Document Frequency of Unigrams written to file.'


doc_freq_bi = {}

for term,name in zip(inverted_dict_bigram.itervalues(), inverted_dict_bigram.iteritems()):
	counter2 = 0
	for val in term.values():
		counter2 = counter2 + 1
	doc_freq_bi[str(name)] = counter2

f = open("Document_Frequency/Document Frequency- Bigrams.txt" , "w")
for key in sorted(doc_freq_bi):
	f.write('%s : %s\n' % (key, doc_freq_bi[key]))

print 'Document Frequency of Bigrams written to file.'

doc_freq_tri = {}

for term,name in zip(inverted_dict_trigram.itervalues(), inverted_dict_trigram.iteritems()):
	counter3 = 0
	for val in term.values():
		counter3 = counter3 + 1
	doc_freq_tri[str(name)] = counter3

f = open("Document_Frequency/Document Frequency- Trigrams.txt" , "w")
for key in sorted(doc_freq_tri):
	f.write('%s : %s\n' % (key, doc_freq_tri[key]))

print 'Document Frequency of Trigrams written to file.'


global term_frequency_uni
term_frequency_uni = {}

global term_frequency_bi
term_frequency_bi = {}

global term_frequency_tri
term_frequency_tri = {}


def term_freq_uni(file):
	filename = open(file,'r')
	current_file = []
	var2 = filename.read()
	var = var2.split()
	for i in var:
		current_file.append(i)

	for i in xrange(1,len(current_file)):
		token = current_file[i]
		if token in term_frequency_uni:
			term_frequency_uni[token] += 1
		else:
			term_frequency_uni[token] = 1 

def term_freq_bi(file):
	filename = open(file,'r')
	current_file = []
	var2 = filename.read()
	var = var2.split()
	for i in var:
		current_file.append(i)

	for i in xrange(1,(len(current_file) - 1)):
		token1 = current_file[i]
		token2 = current_file[i+1]
		ngram2 = (token1,token2)
		if ngram2 in term_frequency_bi:
			term_frequency_bi[ngram2] += 1
		else:
			term_frequency_bi[ngram2] = 1 

def term_freq_tri(file):
	filename = open(file,'r')
	current_file = []
	var2 = filename.read()
	var = var2.split()
	for i in var:
		current_file.append(i)

	for i in xrange(1,(len(current_file) - 2)):
		token1 = current_file[i]
		token2 = current_file[i+1]
		token3 = current_file[i+2]
		ngram3 = (token1,token2,token3)
		if ngram3 in term_frequency_tri:
			term_frequency_tri[ngram3] += 1
		else:
			term_frequency_tri[ngram3] = 1 


for filename in glob.glob('Web Pages/*.txt'):
	term_freq_uni(filename)
	term_freq_bi(filename)
	term_freq_tri(filename)

f = open("Term_Frequency/Term Frequency- Unigrams.txt" , "a")
for w in sorted(term_frequency_uni, key=term_frequency_uni.get, reverse=True):
	f.write('%s : %s\n' % (w, term_frequency_uni[w]))

print 'Term Frequency of Unigrams written to file.'

f = open("Term_Frequency/Term Frequency- Bigrams.txt" , "a")
for w in sorted(term_frequency_bi, key=term_frequency_bi.get, reverse=True):
	f.write('%s : %s\n' % (w, term_frequency_bi[w]))

print 'Term Frequency of Bigrams written to file.'

f = open("Term_Frequency/Term Frequency- Trigrams.txt" , "a")
for w in sorted(term_frequency_tri, key=term_frequency_tri.get, reverse=True):
	f.write('%s : %s\n' % (w, term_frequency_tri[w]))

print 'Term Frequency of Trigrams written to file.'