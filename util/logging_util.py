import logging
import sys 
sys.path.append('/Users/clarencestudy/Desktop/Tech/ETL/ETL')
from config.project_config import log_filename, log_root_path, level

class Logging:
    def __init__(self, level=20):
        self.logger = logging.getLogger()
        self.logger.setLevel(level)
    
def init_logger():
    logger = Logging(level).logger

    # 避免重复输出 避免缓存 避免重复log
    if logger.handlers:
        return logger

    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(
        filename=log_root_path+log_filename,
        # a 是追加log w是覆盖之前的log
        mode='a',
        encoding='utf8'
    )

    fmt = logging.Formatter('%(asctime)s - [%(levelname)s] - %(filename)s[%(lineno)d]: %(message)s')
    stream_handler.setFormatter(fmt)
    file_handler.setFormatter(fmt)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger