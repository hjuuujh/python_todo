class Todo():
    
    def __init__(self, id, title, contents, date, done):
        self.id = id
        self.title = title
        self.contents = contents
        self.date = date
        self.done = done
    
    def info(self):
        if(self.done == True):
            d = "do"
        else:
            d = "undo"
        return self.id  + "\t" +self.title + "\t" +self.contents + "\t" + self.date +"\t"+ d