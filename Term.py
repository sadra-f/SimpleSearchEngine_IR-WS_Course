class Term:
    def __init__(self, text, frq=0):
        self.text = text
        self.frq = frq
    
    def __eq__(self, __value: object) -> bool:
        if __value is not None:
            if __value.__class__.__name__ == self.__class__.__name__:
                if self.text == self.text:
                    return True
        
        return False