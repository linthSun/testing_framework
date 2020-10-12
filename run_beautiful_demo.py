import os,sys
import unittest,time
base_dir = os.path.dirname(__file__)
test_case_path = os.path.join(base_dir,'test_case')
report_dir= os.path.join(base_dir,'report')
sys.path.append(base_dir)
from BeautifulReport import BeautifulReport
from api.last_file import last_report
from api.send_email import email
from api.read_config import read_yaml
from api.test_log import Logger
conf = read_yaml()
logger =Logger()

def add_case(test_path):
    """加载所有的测试用例"""
    discover = unittest.defaultTestLoader.discover(test_path, pattern='test*.py')
    return discover

def run_case(all_case,report_path=report_dir):
    """执行所有的测试用例"""


    now = time.strftime("%Y%m%d%H%M%S")
    filename = now + 'result.html'
    result = BeautifulReport(all_case)
    result.report(filename= filename, description = '自动化接口测试报告', report_dir = report_dir ,theme='theme_default')
    report = last_report(report_path) #调用模块生成最新的报告
    #发送邮件
    if conf.get_conf['email_enable']:
        email_text = '''hi all:
                附件为此次自动化测试结果
                    '''
        email_obj = email(email_text=email_text,email_append_files=[report])
        email_obj.send_email()

if __name__ =="__main__":
    cases = add_case(test_case_path)
    run_case(cases)