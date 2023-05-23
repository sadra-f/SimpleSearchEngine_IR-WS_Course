#todo regex seperate by .I \d{0,4}
from statics.Paths import DATASET_PATH, QUERY_PATH
import re
from models.DSR import DSR

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
        return self._read_data_file(self.DATA_SET_PATH)

    def _read_data_file(self, path) -> str:
        result = []
        record_counter = -1
        with open(path, 'r') as file:
            in_w = False
            for line in file:
                if re.search(Reader.ID_PATTERN, line) is not None:
                    values = line.split(' ')
                    result.append(DSR(values[1].strip()))
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

    