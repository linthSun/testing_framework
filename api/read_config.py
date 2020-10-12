import yaml
import os
import sys
base_dir  = os.path.dirname(os.path.dirname(__file__))

configfile = os.path.join(base_dir,'config','conf.yml')

class read_yaml():
    def __init__(self,file = None):
        if file == None:
           self.file = configfile
        else :
            self.file = file
        with open(self.file,encoding = 'utf-8') as f:
            self.conf = yaml.load(f, Loader=yaml.FullLoader)
            
    @property
    def get_conf(self):
        return self.conf