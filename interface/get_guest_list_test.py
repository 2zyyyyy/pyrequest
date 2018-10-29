import unittest
import requests
import os
import sys
from db_fixture import test_data

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)


class AddGuestTest(unittest.TestCase):
    ''' 获取嘉宾列表'''

    def setUp(self):
        self.base_url = "http://127.0.0.1:8001/api/get_guest_list/"

    def tearDown(self):
        print(self.result)

    def test_get_guest_list_eid_null(self):
        ''' eid为空 '''
        r = requests.get(self.base_url, params={'eid': ''})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'eid cannot be empty')

    def test_get_guest_list_eid_error(self):
        ''' 根据eid查询结果为空 '''
        r = requests.get(self.base_url, params={'eid': 101})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'query result is empty')

    def test_get_event_list_eid_success(self):
        ''' 根据 eid 查询结果成功 '''
        r = requests.get(self.base_url, params={'eid': 1})
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'success')
        self.assertEqual(self.result['data'][0]['realname'], 'tom')
        self.assertEqual(self.result['data'][0]['phone'], '13511001199')

    def test_get_event_list_eid_phone_null(self):
        ''' 根据eid和phone查询结果为空 '''
        r = requests.get(self.base_url, params={'eid': 1, 'phone': '10215412412'})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'query result is empty')


def test_get_event_list_eid_phone_success(self):
    ''' 根据 eid 和phone 查询结果成功 '''
    r = requests.get(self.base_url, params={'eid': 1, 'phone': '13511001100'})
    self.result = r.json()
    self.assertEqual(self.result['status'], 200)
    self.assertEqual(self.result['message'], 'success')
    self.assertEqual(self.result['data']['realname'], 'alen')
    self.assertEqual(self.result['data']['phone'], '13511001100')


if __name__ == '__main__':
    test_data.init_data()  # 初始化接口测试数据
    unittest.main()
