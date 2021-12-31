import os
import re
import collections
import json
import csv
# from glob import glob
from tf.fabric import Fabric
from tf.convert.walker import CV
# from tf.compose import modify

source_dirs = 'input' # "input" is the name of the input folder that contains the source file
output_dirs = 'output' # "output" is the name of the output folder to which the finished TF files will be dumped into

bo2book = {line.split()[0]:line.split()[1] for line in '''
NTt3 New_Testament
'''.split('\n') if line} # "OT" is the name of the file in the input folder AND "split()" splits at space

# patts = {'section': re.compile('(\d*):(\d*)\.(\d*)')}

def director(cv):
        
    '''
    Walks through NA1904 and triggers
    slot and node creation events.
    '''
        
    # process books in order
    for bo, book in bo2book.items():
        
        book_loc = os.path.join(source_dirs, f'{bo}.txt')
        
        print(f'\thandling {book_loc}...')
        
        with open(book_loc, 'r', encoding="utf8") as infile:
            text = [w for w in infile.read().split('\n') if w]
            
        this_book = cv.node('book')
            
        # keep track of when to trigger paragraph, chapter, and verse objects
        # para_track = 1 # keep counts of paragraphs
        prev_book = "Matt" # start at Genesis
        prev_chap = 1 # start at 1
        prev_verse = 1 # start at 1
        
        sentence_track = 1
        sentence_done = False
        clause_track = 1
        clause_done = False
        
        wrdnum = 0 # start at 0
        this_chap = cv.node('chapter')
        # this_para = cv.node('paragraph')
        this_verse = cv.node('verse')
        this_sentence = cv.node('sentence')
        this_clause = cv.node('clause')
        
        
        
        
        # iterate through words and construct objects
        for word in text:

            wrdnum += 1

            data = word.split('\t')
            # word_data, lemmas = data[:7], data[7:]

            word_data = data[:28] #the number here is the amount of columns
            morphology = ' '.join(data[28:]) #the number here is the amount of columns
            
            # segment out word data
            # bo_code, ref, brake, ketiv, qere, morph, strongs = word_data
            orig_order, book, chapter, verse, word, normalized, lemma, morph_form, morph_functional, strongs, lexeme_dict, gloss, sp, gn, nu, ps, case, tense, voice, mood, degree, extra, freq_lemma, bol_dict_abc, lemma_translit, abc_order, BOL_lemma_dict, BOL_gloss = word_data



            #try:
            #    verse = int(verse)
            #except ValueError:
            #    subverse = verse[-1:]
            #    verse = verse[:-1]

            if verse == "":
                print(f'{orig_order}: {verse} {subverse}')


            # strongs_lemma, anlex_lemma = ' '.join(lemmas).split('!') # reconstitute lemmas and split on !

            # chapt, verse, wrdnum = [int(v) for v in patts['section'].match(ref).groups()]

            # -- handle TF events --

            # detect book boundary
            if prev_book != book:

                # end subverse
                # cv.feature(this_subverse, subverse=prev_subverse)
                # cv.terminate(this_subverse)

                # end verse
                cv.feature(this_verse, verse=prev_verse)
                cv.terminate(this_verse)
                
                # end chapter
                cv.feature(this_chap, chapter=prev_chap)
                cv.terminate(this_chap)

                # end book
                cv.feature(this_book, book=prev_book)
                cv.terminate(this_book)
                
                # new book, chapter, verse, and subverse begin
                this_book = cv.node('book')
                prev_book = book
                this_chap = cv.node('chapter')
                prev_chap = chapter
                this_verse = cv.node('verse')
                prev_verse = verse
                #this_subverse = cv.node('subverse')
                #prev_subverse = subverse
                wrdnum = 1
            
            # detect chapter boundary
            elif prev_chap != chapter:

                # end subverse
                #cv.feature(this_subverse, subverse=prev_subverse)
                #cv.terminate(this_subverse)
                
                # end verse
                cv.feature(this_verse, verse=prev_verse)
                cv.terminate(this_verse)
                
                # end chapter
                cv.feature(this_chap, chapter=prev_chap)
                cv.terminate(this_chap)
                
                # new chapter, verse, and subverse begin
                this_chap = cv.node('chapter')
                prev_chap = chapter
                this_verse = cv.node('verse')
                prev_verse = verse
                #this_subverse = cv.node('subverse')
                #prev_subverse = subverse
                wrdnum = 1
            
            # detect verse boundary
            elif prev_verse != verse:

                # end subverse
                #cv.feature(this_subverse, subverse=prev_subverse)
                #cv.terminate(this_subverse)

                # end verse
                cv.feature(this_verse, verse=prev_verse)
                cv.terminate(this_verse)

                # new verse and subverse begin
                this_verse = cv.node('verse')
                prev_verse = verse
                #this_subverse = cv.node('subverse')
                #prev_subverse = subverse
                wrdnum = 1

            # detect subverse boundary
            #elif prev_subverse != subverse:
            #    cv.feature(this_subverse, subverse=prev_subverse)
            #    cv.terminate(this_subverse)
            #    this_subverse = cv.node('subverse')
            #    prev_subverse = subverse

                
            # detect paragraph boundary
            # if brake == 'P':
            #     cv.feature(this_para, para=para_track)
            #     cv.terminate(this_para)
            #     this_para = cv.node('paragraph') # start a new paragraph
            #     para_track += 1 # count paragraphs in the book
            
            
            if sentence_done:
                cv.feature(this_clause, clause=clause_track)
                cv.terminate(this_clause)
                cv.feature(this_sentence, sentence=sentence_track)
                cv.terminate(this_sentence)
                this_sentence = cv.node('sentence')
                sentence_track += 1
                this_clause = cv.node('clause')
                clause_track += 1

                sentence_done = False
                clause_done = False

            elif clause_done:
                cv.feature(this_clause, clause=clause_track)
                cv.terminate(this_clause)
                this_clause = cv.node('clause')
                clause_track += 1

                clause_done = False

            if text[-1:] == "." or text[-1:] == ";":
                sentence_done = True

            elif text[-1:] == "," or text[-1:] == "·":
                clause_done = True
            
            
                
            # make word object
            this_word = cv.slot()
            cv.feature(this_word, 
                        orig_order=orig_order,
                        book=book,
                        chapter=chapter,
                        verse=verse,
                        word=word,
                        normalized=normalized,
                        lemma=lemma,
                        morph_form=morph_form,
                        morph_functional=morph_functional,
                        strongs=strongs,
                        lexeme_dict=lexeme_dict,
                        gloss=gloss,
                        sp=sp,
                        gn=gn,
                        nu=nu,
                        ps=ps,
                        case=case,
                        tense=tense,
                        voice=voice,
                        mood=mood,
                        degree=degree,
                        extra=extra,
                        freq_lemma=freq_lemma,
                        bol_dict_abc=bol_dict_abc,
                        lemma_translit=lemma_translit,
                        abc_order=abc_order,
                        BOL_lemma_dict=BOL_lemma_dict,
                        BOL_gloss=BOL_gloss,
                       # ketiv=ketiv, 
                       # qere=qere, 
                       # strongs=strongs, 
                    #    str_lem=strongs_lemma.strip(),
                    #    anlex_lem=anlex_lemma.strip()
                      )
            cv.terminate(this_word)
        
        # end book and its objects
        # - end subverse
        #cv.feature(this_subverse, subverse=prev_subverse)
        #cv.terminate(this_subverse)
        
       # - end clause
        cv.feature(this_clause, clause=clause_track)
        cv.terminate(this_clause)

        # - end sentence
        cv.feature(this_sentence, sentence=sentence_track)
        cv.terminate(this_sentence)
        

        # - end verse
        cv.feature(this_verse, verse=prev_verse)
        cv.terminate(this_verse)
        
        # - end paragraph
        # cv.feature(this_para, para=para_track)
        # cv.terminate(this_para)
        
        # - end chapter
        cv.feature(this_chap, chapter=prev_chap)
        cv.terminate(this_chap)
        
        # - end book
        cv.feature(this_book, book=prev_book)
        cv.terminate(this_book)


slotType = 'word'
otext = {'fmt:text-orig-full':'{word} ',
         'sectionTypes':'book,chapter,verse',
         'sectionFeatures':'book,chapter,verse'}

generic = {'Name': 'NA1904',
           'Version': '1904',
           'Author': 'Nestle & Aland',
           'Editors': 'Ulrik Sandborg Petersen, Eliran Wong, Oliver Glanz, BOL',
           'Converter': 'Oliver Glanz', 
           'Source:':'https://github.com/biblicalhumanities/Nestle1904/blob/master/morph/Nestle1904.csv',
           'Note':'?'}

intFeatures = {'chapter', 'verse'}

featureMeta = {
                'orig_order': {'description': 'word order within corpus'},
                'book': {'description': 'book'},
                'chapter': {'description': 'book'},
                'verse': {'description': 'verse'},
                'sentence': {'description': 'sentence'},
                'clause': {'description': 'clause'},
                'word': {'description': 'word as it appears in the text'},
                'normalized': {'description': 'normalized word'},
                'lemma': {'description': 'lemma'},
                'morph_form': {'description': 'formal morphology coding'},
                'morph_functional': {'description': 'functional morphology coding'},
                'strongs': {'description': 'Strong\'s numbers'},
                'lexeme_dict': {'description': 'dictionary form of lemma'},
                'gloss': {'description': 'English translation'},
                'sp': {'description': 'part of speech'},
                'gn': {'description': 'gender'},
                'nu': {'description': 'number'},
                'ps': {'description': 'person'},
                'case': {'description': 'case'},
                'tense': {'description': 'tense'},
                'voice': {'description': 'voice'},
                'mood': {'description': 'mood'},
                'degree': {'description': 'degree'},
                'extra': {'description': 'extra notes'},
                'freq_lemma': {'description': 'word frequency in corpus'},
                'bol_dict_abc': {'description': 'BOL based alphabetic order of words'},
                'lemma_translit': {'description': 'lemma transliteration'},
                'abc_order': {'description': 'NA1904 alphabetic order of words'},
                'BOL_lemma_dict': {'description': 'BOL based dictionary form'},
                'BOL_gloss': {'description': 'BOL based English gloss'},
               #'subverse': {'description': 'Subverse information'},
               # 'para': {'description': 'A paragraph number'},
               # 'ketiv': {'descrption': 'The text as it is written in the printed Tischendorf'},
               # 'qere': {'description': 'The text as the editor thinks it should have been'},
               # 'strongs': {'description': 'A word\'s number in Strongs'},
               # 'str_lem': {'description': 'Word lemma that corresponds to The NEW Strong\'sComplete Dictionary of Bible Words'},
               # 'anlex_lem': {'description': 'Word lemma that corresponds to Friberg, Friberg and Miller\'s ANLEX'}
              }


# configure metadata/output
version = '1904'
generic['Version'] = version

output = os.path.join(output_dirs, version)

print(f'Processing Version {version}')
output_dir = output_dirs.format(version=version)

TF = Fabric(locations=output_dir, silent=True)
cv = CV(TF)

cv.walk(director,
                slotType,
                otext=otext,
                generic=generic,
                intFeatures=intFeatures,
                featureMeta=featureMeta,
                warn=True,
                force=False,)