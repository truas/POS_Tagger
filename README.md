# POS_Tagger
===============

Generic POS Tagger for text documents.
Folder used to read/write should be in the same level at 'default' package

	python3 postagger.py --input <input-folder-location> --output <output--folder-location>


UPDATES:
==========
[2018-11-29]
1. makeLowerCase and applyStemmer ignore words beginning with <math->
[2018-11-28]
1. Several pre-processing functions implemented
2. NLTK tagger working
3. General refactorings

[2018-11-14]
1. cleanString implemented to get rid of specific chars

[2018-10-29]
1. Reading/writing files - line-by-line, 
2. Text clean and stopwords removal
3. POS tagger using NLTK prototype

[2018-10-26]
1. Project creation
2. File/Folder structure implementation
3. Command line arguments added

