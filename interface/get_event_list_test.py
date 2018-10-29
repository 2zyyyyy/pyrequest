import unittest
import requests
import os
import sys
from db_fixture import test_data

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class AddGuestTest(unittest.TestCase):
    ''' 获取发布会列表'''

    def setUp(self):
        self.base_url = "http://127.0.0.1:8001/api/get_event_list/"

    def tearDown(self):
        print(self.result)

    def test_get_event_list_parameter_error(self):
        ''' 参数错误 '''
        r = requests.get(self.base_url, params={})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_get_event_list_eid_error(self):
        ''' 查询结果为空 '''
        r = requests.get(self.base_url, params={'eid': 101})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'query result is empty')

    def test_get_event_eid_success(self):
        ''' 根据eid查询成功 '''
        r = requests.get(self.base_url, params={'eid': 1})
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'success')
        self.assertEqual(self.result['data']['name'], u'红米Pro发布会')
        self.assertEqual(self.result['data']['address'], u'北京会展中心')

    def test_get_event_list_name_null(self):
        ''' 关键词'大帅逼'查询 '''
        r = requests.get(self.base_url, params={'name': '大帅逼'})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'query result is empty')

    def test_get_event_list_name_find(self):
        ''' 关键词'发布会'模糊查询 '''
        r = requests.get(self.base_url, params={'name': '发布会'})
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'success')
        self.assertEqual(self.result['data'][0]['name'], u'红米Pro发布会')
        self.assertEqual(self.result['data'][0]['address'], u'北京会展中心')

if __name__ == '__main__':
    test_data.init_data()  # 初始化接口测试数据
    unittest.main()