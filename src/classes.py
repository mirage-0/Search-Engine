class Directory:
    def __init__(self, **args):
        self.valueList  # = list of values from args
        self.dictionary = self.generateDictionary(self.valueList)
        self.parent
        self.children
        self.directory
        return (self)

    def generateDictionary(self):
        return dict(self.generateKeys(self.valueList), self.valueList)

    def generateKeys(self, valueList):
        # write a function to create encoded list of keys and return them
        pass


class File:
    def __init__(self, **args):
        # a file probably doesnt need a parent as it is accessed from parent variable itself as in, directory.children[0].name
        # where directory IS the parent.
        # self.parent
        self.name
        self.size
        self.format
        self.dateAdded
        self.dateModified
        self.duration
        return (self)

    def setValues(self):
        pass
