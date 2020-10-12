import os

def last_report(testreport):
    """
    生成最新的测试报告文件
    :param testreport:
    :return:返回文件
    """
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport,lists[-1])
    return file_new


def last_file(file_path):
    """
    获取最后一个文件夹最新修改的文件
    ：param file_path:
    ：retrun: 返回文件名
    """
    return None


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir,'report')
    last_file =  last_report(file_path)
    print(last_file)