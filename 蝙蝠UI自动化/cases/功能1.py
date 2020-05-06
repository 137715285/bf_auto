def add_order(name):
    return {
            'ret': 0,
            'info': {
                'id': 100,
                'name': name
            }
        }

def rename_order(oid):
    return {'ret': 0}

def delete_order(oid):
    return {'ret': 0}


default_tags = ['优先级7']

force_tags = ['冒烟测试','订单功能']

def suite_setup():
    pass

def suite_teardown():
    pass

# 用例对应的类名，建议依次为 c1, c2, c3, ...
class c1:
    # 用例名，必填。 建议后面加上编号
    name = '添加订单 - 00001'
    # 用例标签，可选   
    tags = ['本次不测','now']

    # 用例的初始化
    def setup(self):
        ret = add_order('order name')

        # we could compare complicated data object easily,
        # but in Robot, that's hard
        assert ret == {
            'ret': 0,
            'info': {
                'id': 100,
                'name': 'order name'
            }
        }
        self.orderid = ret['info']['id']

    # 用例的清除
    def teardown(self):
        delete_order(self.orderid)


    # 测试用例 具体操作步骤
    def teststeps(self):
        # we could easily get data "orderid" from test setup
        ret1 = rename_order(self.orderid)

        assert ret1 == {'ret': 0}




class c2:
    # 用例名，必填。 建议后面加上编号
    name = '添加订单 - 00002' 


    def teststeps(self):
        pass

    def teardown(self):
        delete_order(1)