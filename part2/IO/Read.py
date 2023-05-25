
from statics.Paths import DATASET_PATH, QUERY_PATH
import re
from models.DSR import DatasetRecord as DSR
from models.QR  import QueryRecord as QR

class Reader:
    ID_PATTERN = "^[.]I \d{1,4}$"
    T_PATTERN = "^[.]T$"
    A_PATTERN = "^[.]A$"
    B_PATTERN = "^[.]B$"
    W_PATTERN = "^[.]W$"

    def __init__(self):
        self.DATA_SET_PATH = DATASET_PATH
        self.QUERY_PATH = QUERY_PATH
    
    def read_dataset(self):
        return self._read_file(self.DATA_SET_PATH, True)

    def _read_file(self, path, is_dataset) -> str:
        result = []
        record_counter = -1
        with open(path, 'r') as file:
            in_w = False
            for line in file:
                if re.search(Reader.ID_PATTERN, line) is not None:
                    values = line.split(' ')
                    if is_dataset:
                        result.append(DSR(values[1].strip()))
                    else:
                        result.append(QR(values[1].strip()))
                    record_counter += 1
                    in_w = False
                if in_w:
                    result[record_counter].text += line.replace('\n', ' ')
                elif re.search(Reader.T_PATTERN, line) is not None:
                    pass
                elif re.search(Reader.A_PATTERN, line) is not None:
                    pass
                elif re.search(Reader.B_PATTERN, line) is not None:
                    pass
                elif re.search(Reader.W_PATTERN, line) is not None:
                    in_w = True
        return result

    def read_queries(self):
        return self._read_file(self.QUERY_PATH, False)