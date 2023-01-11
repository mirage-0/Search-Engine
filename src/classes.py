class Directory:
    def __init__(self, **args):
        self.parent
        self.children
        self.directory
        return (self)


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
