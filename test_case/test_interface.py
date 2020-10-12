import unittest
import requests
from ddt import ddt, data, unpack,idata
import sys,os
base_dir = os.path.dirname((os.path.dirname(__file__)))
sys.path.append(base_dir)
from api.send_request import sendRequest as query
# from api.excel_read import ReadExcel  as rExcel
from api.excel_read import excel
from api.test_log import Logger
logger =Logger()

test_case_file = os.path.join(base_dir,'data','test_data.xlsx')
# test_datas = rExcel(test_case_file).read_data()
test_datas = excel(test_case_file).read_data()
# test_datas=((1, 2, 3), (4, 5, 6), (7, 8, 9))
# # test_case = er("test_data.xlsx").read_data()
@ddt
class TestIce(unittest.TestCase):
    
     # 一条测试用例，必须test_开头
    # @data(test_datas)
    # @unpack
    
    @idata(test_datas)
    def test_frame(self,test_data):
        ''' 
        接口测试__
        
        '''
        '''第一步'''
        logger.info("---%s用例开始执行---"%test_data['testcase_name'])
        response = query().sendRequest(test_data)
        self.assertEqual(int(test_data["status_code"]), response.status_code)  # 断言
        logger.info("---%s用例执行结束---"%test_data['testcase_name'])


if __name__ == "__main__":
    unittest.main()