'''
Created on Oct 26, 2018
@author: terry
'''
#import
import logging
import time
import nltk
import sys
import argparse #for command line arguments
import os

#python module absolute path
pydir_name = os.path.dirname(os.path.abspath(__file__))
ppydir_name = os.path.dirname(pydir_name)
#python path definition
sys.path.append(os.path.join(os.path.dirname(__file__),os.path.pardir))

from datetime import timedelta
from stop_words import get_stop_words
from default import file_manipulation as fm

#show logs
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s',
    level=logging.INFO)

#main program
if __name__ == '__main__': 
     
    #===========================================================================
    # #IF you want to use COMMAND LINE for folder path
    # parser = argparse.ArgumentParser(description="POS_Tagger - Generic Tagger for Text Documents")
    # parser.add_argument('--info', type=str, help='<files/> folder should be at the same level as default package')
    # parser.add_argument('--input', type=str, action='store', dest='inf', metavar='<folder>', required=True, help='input folder to read document(s)')
    # parser.add_argument('--output', type=str, action='store', dest='ouf', metavar='<folder>', required=True, help='output folder to write document(s)')
    # args = parser.parse_args()   
    #   
    # #COMMAND LINE  folder paths
    # input_folder = args.inf #dest=inf
    # output_folder = args.ouf #dest=ouf
    #   
    # #in/ou relative location - #input/output/model folders are under synset/module/
    # in_foname = os.path.join(ppydir_name, input_folder) 
    # ou_foname = os.path.join(ppydir_name, output_folder)
    #===========================================================================
    
    #IDE - Path Definitions
    in_foname = 'C:/Users/terry/Documents/Programming/eclipse-workspace/POS_Tagger/files/input'
    ou_foname = 'C:/Users/terry/Documents/Programming/eclipse-workspace/POS_Tagger/files/output'
    #'C:/Users/terry/Documents/Datasets/ArXiv/output'
     
    
    #Doc and File list
    doc_paths =  fm.doclist_multifolder(in_foname)
    doc_names = fm.fname_splitter(doc_paths)
    
    for index, fname in enumerate(doc_paths):
        fm.cleanText(doc_names[index], fname, ou_foname)
   