from Document import Document

def read_file(file_path) -> Document:
    with open(file_path) as f:
        return Document(file_path, f.read(file_path))


def read_dir(dir_path, file_extension=".txt") -> list[Document]:
    docs = []
    for file_path in os.listdir(dir_path):
        if file_path.endswith(file_extension):
            docs.append(read_file(file_path))
    
    return docs
