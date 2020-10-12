import os,sys
import unittest,time
base_dir = os.path.dirname(__file__)
test_case_path = os.path.join(base_dir,'test_case')
report_dir= os.path.join(base_dir,'report')
sys.path.append(base_dir)
from package.HTMLTestRunner import HTMLTestRunner
from api.newReport import last_report
from api.send_email import email

def add_case(test_path):
    """加载所有的测试用例"""
    discover = unittest.defaultTestLoader.discover(test_path, pattern='test*.py')
    return discover

def run_case(all_case,report_path=report_dir):
    """执行所有的测试用例"""


    now = time.strftime("%Y%m%d%H%M%S")
    filename =  report_path + '/' + now + 'result.html'
    print(all_case)
    with  open(filename,'wb') as fp:
        runner = HTMLTestRunner(stream=fp,title='接口自动化测试报告',
                                description='环境：windows 10',
                                tester='Linth')
        runner.run(all_case)
#     report = new_report(report_path) #调用模块生成最新的报告

if __name__ =="__main__":
    cases = add_case(test_case_path)
    run_case(cases)