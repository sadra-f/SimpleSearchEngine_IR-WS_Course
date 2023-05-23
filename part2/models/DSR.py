class DatasetRecord:
    
    def __init__(self, i:int, t:str=None, b:str=None, w:str=str()):
        self.ID = int(i)
        self.t = t
        self.b = b
        self.text = w