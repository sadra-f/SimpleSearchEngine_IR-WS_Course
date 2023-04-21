class Term:
    def __init__(self, text:str, frq:int=1):
        self.text = text
        self.frq = frq
    
    def __eq__(self, __value: object) -> bool:
        if __value is not None:
            if __value.__class__.__name__ == self.__class__.__name__:
                return self.text == __value.text
            if  __value is(str):
                return __value == self.text

        return False
    
    def __hash__(self) -> int:
        return hash(self.text)
    
    def __str__(self) -> str:
        return self.text

    def __lt__(self, term):
        return self.text < term.text
    
    def __gt__(self, term):
        return self.text > term.text
