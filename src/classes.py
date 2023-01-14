class Directory:
    def __init__(self, **args):
        self.valueList  # = list of values from args
    # holds all directories Paths in system
        self.dictDirPath
    # holds all files Paths in system
        self.dictFilesPath
    # holds the format keys we will generate (mp4, mp3, exe, txt, word,.)
        self.formatsKeys = []
    # holds the name keys we will generate (encoded number 1, encoded number 2, encoded number 3,.)
        self.fileNameKeys = []
    # holds the name keys of directories uses same encoding as above
        self.dirNameKeys = []
    # first dict, divides ds in directories and files
        self.dictA = {0: self.dictDir, 1: self.dictFile}
    # directory dict which divides ONLY directories via similar file names
        self.dictDir = self.generateDictionary(
            self.dirNameKeys, self.dictDirPath)
    # file dict, divides ds in formats
        self.dictFile = self.generateDictionary(self.formatsKeys, self.dictC)
    # third dict, divides ds by names
        # 'encoding number 1' holds compressed data about the names of the files it holds, just by sending encoded
        # number to a special function decode() we get a general idea about what file names to expect in
        # the dict this key 'encoding number 1' holds, then decide if its worth it to search through all of the dict
        self.dictC = self.generateDictionary(
            self.fileNameKeys, self.dictFilesPath)

        return (self)

    def generateDictionary(self, keyList, valueList):
        return dict.fromkeys(keyList, valueList)

    def generateKeys(self, valueList):
        # write a function to create encoded list of keys and return them
        pass
