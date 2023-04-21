class Document:
        _id_counter = 0
        def __init__(self, path:str, text:str):
            self.path = path
            self.text = text
            self.id = Document._id_counter
            Document._id_counter += 1