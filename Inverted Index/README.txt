Information Retreival Assignment-3
----------------------------------

Name: Tushar Gupta
NUID: 001250096

-----------------------------------

How to compile/run the source code?

-----------------------------------

-> Please read the complete text before compiling/running the submission.

-> The code is built on Python 2.7

-> It utilizes BeautifulSoup 4 Library for text parsing. It is not included in the python package,
so you might need to install that before proceeding, if it is not already present.

-> Unzip the contents of the submission file at one place. 

-> Make sure that all the folders as described below exist in the folder(even if they are empty).
   Otherwise, the program will throw an error.

-> First run the Task1.py file. It will generate the tokenized files. Then run the Task2-3.py file.
   It will generate the six tables as required in the deliverables.

------------------------------------

Contents of the Submission Zip File:

------------------------------------


-> The submission consists of the following folders:
	1. InputFiles : 	This folder consists of the 1000 html pages downloaded in the first task,
				which are used to generate the token files.
	2. Web pages : 		This is the folder where the tokenized corpus is stored. The files are stored
				as the title name of the wikipedia page. An unforseen problem faced here, was
				that there are some pages in the InputFiles generated from URL's which
				ultimately point to the same Wiki Page. So, I have preserved them also by
				giving the duplicate pages a different filename.
	3. Inverted_Index : 	This consists of three text files. They store Inverted Index for Unigrams,
				Bigrams and Trigrams
	3. Document_Frequency : This consists of three text files. They store Document Frequencies for Unigrams,
				Bigrams and Trigrams sorted lexicographically based on term.
	3. Term_Frequency : 	This consists of three text files. They store Term Frequencies for Unigrams,
				Bigrams and Trigrams sorted from most to least frequent.


-> The submission consists of the following files:
	1. Task1.py :		It consists of the source code for Task 1. It takes Paragraph Tags <p> and
				some Unordered List Tags <ul> and ignores all the others. Only those <ul> tags
				which represent some bullet points in the main body are considered. Unordered 
				lists inside tables or other tags are ignored. The file is saved as the title
				of the wiki page, sans whitespaces or '-' , '_' etc. It tokenizes the html
				pages from InputFiles folder, and stores them in Web Pages folder.
	2. Task2-3.py :		It consists of the source code for Task 2 and Task 3. It takes the tokenized
				files one by one, and does three jobs:
				1. It creates inverted index for Unigrams, Bigrams and Trigrams.
				2. It creates document frequency tables for Unigrams, Bigrams and Trigrams.
				3. It creates term frequency tables for Unigrams, Bigrams and Trigrams.
	3. Stoplist.txt :	This file contains the list of words I have taken as StopWords and my
				explanation for choosing them.
	4. README.txt :		This file.
	5. Zipf Curve for Unigrams.png , Zipf Curve for Bigrams.png , Zipf Curve for Trigrams.png 

---------------

Design Choices:

---------------

-> The input files are html files.
-> The token files are stored as text files.

-> I have taken Inverted Index to be dictionaries, where the key is the term(s), and the values consist of
   dictionaries containing DocID and the number of occurences of the term in that DocID.

-> Term Frequencies are also dictionaries which consist of the keys as term(s) which string or tuples, and the
   Frequency as Values.

-> Document Frequencies are also dictionaries which consist of the keys as term(s) and DocID's which is
   represented as string, and the Frequency which is the Value for the key.

-> All the above dictionaries are finally stored in text files. When they need to be retrieved for further processing,
   they can be stored as JSON Objects, which maintain the order of the dictionary as well. But, for this time,
   for easier readability, they have been stored as text files.

----------------------------------------------------------------------------------------------------------------------

IMPORTANT NOTE: DUE TO SOME ENCODING ISSUES, RANDOM CHARACTERS APPEAR WHILE TOKENIZING THE HTML PAGES. IT OCCURS DUE TO
UNICODE TO UTF-8 CONVERSIONS. PLEASE IGNORE IF SOME RANDOM CHARACTERS APPEAR DURING TOKENIZING.






		




