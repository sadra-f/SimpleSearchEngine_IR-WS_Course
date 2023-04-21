class Document:
        _id_counter = 0
        def __init__(self, path, content):
            self.path = path
            self.content = content
            self.id = Document._id_counter
            Document._id_counter += 1