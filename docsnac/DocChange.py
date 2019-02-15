#script to swap out words with synonyms in a novel of text or text file

#want to be able to process other text like documents

from thesaurus import Word
import random
#should have the option of overwriting the file the input is taken from
class DocChange:
    def __init__(self,input):
        self.input = input

    """
      - DocChange.change_words() is a method that allows 
      the user to swap words out with either text or 
      text documents. 
      

      DocChange.change_words(self, IS_FILE=True,file_mode='w')
      

    """
    def change_words(self, IS_FILE=False, file_mode='w'):
        if IS_FILE:
            """
            read the input as if it was a file
            """
            random_file_name = random.choice(Word("box").synonyms())

            with open(random_file_name, 'w') as dest_file:
                #get new word, if theres an error add the word anyways
                with open(self.input, 'r') as input_file:
                    for word in input_file.read().split(" "):
                        try:
                            input_file_word = random.choice(Word(word).synonyms())
                            dest_file.write(" " + input_file_word)
                        
                        except Exception as e:
                            dest_file.write(word)
            
                        
                        
                      
                       

                    

        else:
          new_text_list = []
          
          for word in input.split(" "):
            try:
              new_word = random.choice(Word(word).synonyms())
              new_text_list.append(new_word)
            except Exception as e:
              new_text_list.append(word)


        else:
            for word in input:
                 new_word = random.choice(Word(word).synonyms())
