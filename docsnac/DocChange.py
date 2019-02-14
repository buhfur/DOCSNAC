#script to swap out words with synonyms in a novel of text or text file

#want to be able to process other text like documents

from thesaurus import Word
import random
#should have the option of overwriting the file the input is taken from
class DocChange:
    def __init__(self, IS_FILE, input):
        self.IS_FILE = IS_FILE
        self.input = input


    def change_words(self):
        if self.IS_FILE:
            """
            read the input as if it was a file
            """
            with open(self.input, 'r') as input_file:
                for word in input_file.read().split(" "):
                    try:
                        #generates a random name for the new file with new words
                        random_file_name = random.choice(Word("box").synonyms())


                        with open(random_file_name, 'w') as dest_file:
                            #get new word, if theres an error add the word anyways
                            try:
                                input_file_word = random.choice(Word(word).synonyms())
                                dest_file.write(input_file_word)
                            except Exception as e:
                                dest_file.write(word)

                    except Exception as e:
                        print(e)

        else:
            for word in input:
                 new_word = random.choice(Word(word).synonyms())
