
import logging
import os
import time
import threading
base_dir = os.path.dirname(os.path.dirname(__file__))
log_file = os.path.join(base_dir,'log','test.log')
log_path = os.path.join(base_dir,'log')
now = time.strftime("%Y%m%d%H%M", time.localtime())
 
class Logger(logging.Logger):
    _instance_lock = threading.Lock()

    def __init__(self, filename=None):
        super(Logger, self).__init__(self)
        # 日志文件名
        if filename is None:
            self.filename = os.path.join(log_path,now+'.log')
        else:
            self.filename = log_file
        
        # 创建一个handler，用于写入日志文件 (每天生成1个，保留30天的日志)
        fh = logging.FileHandler(self.filename,encoding='utf-8')
        fh.setLevel(logging.DEBUG) 
 
        # 再创建一个handler，用于输出到控制台 
        ch = logging.StreamHandler() 
        ch.setLevel(logging.INFO) 
 
        # 定义handler的输出格式 
        formatter = logging.Formatter('[%(asctime)s] - %(filename)s [Line:%(lineno)d] - [%(levelname)s]-[thread:%(thread)s]-[process:%(process)s] - %(message)s') 
        fh.setFormatter(formatter) 
        ch.setFormatter(formatter) 
 
        # 给logger添加handler 
        self.addHandler(fh) 
        self.addHandler(ch)
    

    def __new__(cls, *args, **kwargs):
         with Logger._instance_lock:
            if not hasattr(cls, '_instance'):
                Logger._instance = super().__new__(cls)
         return Logger._instance


if __name__ == "__main__":
    logger = Logger()