class Prohibition:

    def __init__(self, dataFrame=None, column=None, row=None):
        self.dataFrame = dataFrame
        self.column = column
        self.row = row

    def check(self, new_dataFrame):
        if list(self.dataFrame[self.column]) == list(new_dataFrame[self.column]):
            self.dataFrame = new_dataFrame
            return new_dataFrame
        elif len(list(self.dataFrame[self.column])) < len(list(new_dataFrame[self.column])) and \
                list(new_dataFrame[self.column])[-1] == '':
            self.dataFrame = new_dataFrame
            return new_dataFrame
        else:
            return self.dataFrame

    def dFrame(self, flag):
        match (flag):
            case ('frame'):
                return self.dataFrame
            case ('columns'):
                return self.dataFrame.columns
