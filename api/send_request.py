
import requests
import json
import sys
import os 
base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_dir)
from api.test_log import Logger
logger =Logger()

# logging.basicConfig(filename='logger.log', level=logging.INFO,format=' %(asctime)s -%(levelname)s - %(message)s')
class sendRequest():
    def sendRequest(self,api_data):
        # try:
            logger.info(api_data)
            method = api_data["method"]
            url = api_data["url"]
            payload = api_data["payload"]
            headers = api_data["headers"]
            params = api_data["params"]

            if api_data["headers"] :
                headers = json.loads(api_data["headers"])    

            if api_data["params"]:
                params = json.loads(api_data["params"])
                
            type_ = api_data["type_"]
            if type_ == "json":
                payload = json.dumps(payload)
                logger.debug(payload)
            response = requests.request(method=method, url=url,headers=headers, params=params, data=payload)
            logger.info(response.url)
       
      
            return response
        # except Exception as e:
        #     logger.error(e)

if __name__ == "__main__":
    #  api_data = {
    #      "method": "get",
    #      "url":"http://172.20.82.58/auth/login/login",
    #      "params":{"username":"admin","password":"admin"},
    #      "headers":"",
    #      "payload":"",
    #      "type":""}

     api_data ={
     'url': 'http://172.20.82.58/auth/login/login', 
     'method': 'get', 
     'params': '{ "username": "admin",\n    "password": "admin"\n}',
     'headers': '', 
     'payload': '',
     'type_':''
      }
     sender = sendRequest()
     res =sender.sendRequest(api_data)