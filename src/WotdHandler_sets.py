
from os import path, getcwd, chdir
from random import randint

# chdir("src")

class WordHandler:

    filePaths = ("unused_words.txt","used_words.txt")
    filePathUnused = path.abspath(filePaths[0])
    filePathUsed = path.abspath(filePaths[1])

    def __init__(self):

        '''
        We want to first check if the file pathways are good. If they are not, the bot can essentially do nothing.
        '''

        self.pathsGood = self._check_paths()
        self.unusedWords = {}
        self.usedWords = {}
        self.bootGood = self._read_files()
    
    def _check_paths(self):
        '''
        Check if the file paths exist. They must both exist for the paths to be considered good.
        '''
        unusedFileExists = path.exists(self.filePaths[0])
        usedFileExists = path.exists(self.filePaths[1])
        return (unusedFileExists and usedFileExists)

    def _read_files(self):
        '''
        If our paths are good, then we open them and read the files, stripping them of trailing spaces and newlines.
        We return whether this was successful or not.
        '''

        if self.pathsGood:
            try:
                with open(self.filePathUnused,"r") as file:
                    self.unusedWords = set(line.strip() for line in file)
                    # self.unusedWords = self._count_words(unusedWords)
                with open(self.filePathUsed,"r") as file:
                    self.usedWords = set(line.strip() for line in file)
                    # self.usedWords = self._count_words(usedWords)
                return True
            # except FileNotFoundError as e:
            except:
                return False
        else:
            print("Paths not good when reading attempted")
            return False
        
    def _write_files(self):
        '''
        If our paths are good, then we open them and write the current lists to the files.
        We return whether this was successful or not.
        '''
        if self._check_paths():
            try:
                unusedWrite = [word+'\n' for word in self.unusedWords]
                usedWrite = [word+'\n' for word in self.usedWords]
                # self.sort_lists()
                with open(self.filePathUnused, "w") as file:
                    file.writelines(unusedWrite)
                with open(self.filePathUsed, "w") as file:
                    file.writelines(usedWrite)
                return True
            # except FileNotFoundError as e:
            except:
                return False
        else:
            print("Paths not good when writing attempted")
            return False
 
    def _wotd(self):
        '''
        Choose a random word from the unused word list and remove it.
        Add that word to the used word list, re-sort the lists (just in case)
        Return the word as the word of the day
        '''
        word = self.unusedWords.pop()
        self.usedWords.add(word)
        word_def = self._fetch_definiton(word)
        return word, word_def

    def _fetch_definiton(self, word:str):
        '''
        Take a new word and attempt to retrieve definition.
        If this fails, make note and return the respective boolean
        '''

        returnInt = 1

        if word in self.unusedWords:
            returnInt = 2
        if word in self.usedWords:
            returnInt = 3
        
        if returnInt == 2:

            check, word_def = self._get_definition(word)
            
            if not check or word_def==None:
                returnInt=0
            return returnInt
    
    def _get_definition(self, word:str):
        
        check = False # dummy variables for now
        wdef = None

        return check, wdef

    def run_wotd(self):

        '''
        Control Flow of program:
        - Read word lists from files
        - Sort the lists to make sure it's in order
        - Check for repetitions (within lists and then between the lists)
        - return the word of the day (implicitly removing the word from the used list and adding it to the unused list)

        '''

        if self.bootGood:
            if len(self.unusedWords)>0:
                wotd = self._wotd()
                print(f"Writing success : {self._write_files()}")
            else:
                wotd = None
        else:
            wotd = None
        
        return wotd
  

WotD = WordHandler()

wotd = WotD.run_wotd()

print(wotd)
# print(path.abspath(WordHandler.filePathUnused))
