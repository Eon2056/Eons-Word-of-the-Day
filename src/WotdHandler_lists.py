
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
        self.unusedWords = None
        self.usedWords = None
        self.bootGood = self._read_files()
    
    def _check_paths(self):
        '''
        Check if the file paths exist. They must both exist for the paths to be considered good.
        '''
        unusedFileExists = path.exists(self.filePaths[0])
        usedFileExists = path.exists(self.filePaths[1])
        return (unusedFileExists and usedFileExists)
    
    def _sort_lists(self):
        self.unusedWords.sort()
        self.usedWords.sort()
        
    def _repetitions_exist_in(self, wordList:list):
        '''
        Check if there are any repetitions using a set of the list
        '''
        return wordList!=sorted(list(set(wordList)))
    
    def _count_words(self, list:list):
        '''
        To count our words, we convert the lists read from the files into dictionaries.
        This allows us to have one reference for each word, with a count of how many occur.
        Ideally, these are all 1. 
        Of course, if that would happen, we don't want to waste time with dictionaries. 
        That is why we first checked if the list equals the set first.
        We only reach this function if the count of any word would be >1. 
        '''
        wordDict = dict.fromkeys(set(list),0)
        for word in list:
            wordDict[word] +=1
        return wordDict

    def _find_repetitions_within(self, wordList:list):
        '''
        We first check if repetitions exist in the list. 
        If words repeat, we change the list to a dictionary to log instances of each word.
        The repeated words are those for which the instance count is >1
        '''
        
        if self._repetitions_exist_in(wordList):
            wordDict = self._count_words(wordList)
            return [word for word in wordDict if wordDict[word]>1]
        else:
            return []
    
    def _remove_repetitions_within(self, wordList:list):
        wordList = list(set(wordList))

    def _repetitions_between(self):

        '''
        We want to find the words present in the Unused list which already exist in the Used list.
        Therefore, the Used list is our reference, and the Unused list is the one which we check and modify.

        This method should only be invoked after inner repetitions are purged with _repetitions_within()
        '''

        # repetitions = []
        # for word in self.unusedWords:
        #     if word in self.usedWords:
        #         repetitions.append(word)

        return [word for word in self.unusedWords if word in self.usedWords]

    def _remove_repetitions_between():
        return

    def _read_files(self):
        '''
        If our paths are good, then we open them and read the files, stripping them of trailing spaces and newlines.
        We return whether this was successful or not.
        '''

        if self.pathsGood:
            try:
                with open(self.filePathUnused,"r") as file:
                    self.unusedWords = [line.strip() for line in file]
                    # self.unusedWords = self._count_words(unusedWords)
                with open(self.filePathUsed,"r") as file:
                    self.usedWords = [line.strip() for line in file]
                    # self.usedWords = self._count_words(usedWords)
                self._sort_lists()
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
        randChoose = randint(0,len(self.unusedWords)-1)
        # print("randChoose: ", randChoose)
        # print("unused len: ", len(self.unusedWords))

        print(f"unused before wotd: {self.unusedWords}")
        print(f"used before wotd: {self.usedWords}")

        word = self.unusedWords.pop(randChoose)

        print(f"Word of the day: {word}")
        print(f"unused after wotd: {self.unusedWords}")

        self.usedWords.append(word)

        print(f"used after wotd: {self.usedWords}")
        # self._sort_lists()
        return word

    def _new_unused_word(self, word:str):
        '''
        Take a new word and attempt to retrieve definition.
        If this fails, make note and return the respective boolean
        '''
        
        check, wdef = self._get_definition(word)
        
        if check and wdef!=None:
            return True
        else: return False
    
    def _get_definition(self, word:str):
        
        check = False # dummy variable for now
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
                self._sort_lists()
                rep_within_unused = self._find_repetitions_within(self.unusedWords)
                rep_within_used = self._find_repetitions_within(self.usedWords)
                rep_between = self._repetitions_between()
                wotd = self._wotd()
                print(f"Writing success : {self._write_files()}")
            else:
                wotd = None
        else:
            wotd = None
        
        return wotd
  

WotD = WordHandler()

WotD.run_wotd()

# print(path.abspath(WordHandler.filePathUnused))
