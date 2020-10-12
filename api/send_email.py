import yaml
import sys
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_dir)
from api.last_file import last_report
from api.test_log import Logger
from api.read_config import read_yaml
logger = Logger()


class email(read_yaml):
    
      def __init__(self,email_text=None,email_append_files=[],file_name=None):
          super().__init__(file=file_name)
          self.message = MIMEMultipart()
          self.email_text = email_text
          self.email_append_files = email_append_files
          self.host = ''
          self.sender = ''
          self.receivers = []
          self._password = ''
      @property
      def email_info(self):
          return self.conf['email'] 

      @property
      def email_body(self):
           self.message.attach(MIMEText(self.email_text, 'plain', 'utf-8'))
           return self

      @property
      def  eamil_header(self):
           self.sender = self.email_info['sender']
           self.receivers =self.email_info['receivers']
          #创建一个带附件的实例
           self.message['From'] = Header(self.sender, 'utf-8')
           self.message['To'] =  Header(";".join(self.receivers), 'utf-8')
           subject = '测试报告'
           self.message['Subject'] = Header(subject, 'utf-8')
           return self

      def email_append(self,append_file):
          att = MIMEText(open(append_file, 'rb').read(), 'base64', 'utf-8')
          att["Content-Type"] = 'application/octet-stream'
          # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
          
          (_, tempfilename) = os.path.split(append_file)
          att["Content-Disposition"] = 'attachment; filename="%s"'%tempfilename
          self.message.attach(att)

      def send_email(self):
          try:
            self.eamil_header.email_body
            self.host = self.email_info['server']
            self._password = self.email_info['password']
            for  append in self.email_append_files:
                  self.email_append(append)
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.host)
            smtpObj.login(user=self.sender,password = self._password)
            smtpObj.sendmail(self.sender, self.receivers, self.message.as_string())
            logger.info("邮件发送成功")
          except smtplib.SMTPException:
            logger.error ("Error: 无法发送邮件")

 
 


if __name__ == "__main__":
   test_report = os.path.join(base_dir,'report')
   report = last_report(test_report)
   email = email(email_text=' it is a test',email_append_files=[report])
   print(email.email_info)
   email.send_email()
   


 
 

