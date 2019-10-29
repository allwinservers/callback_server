

import time,random
from requests import request
from collections import OrderedDict
import hashlib
import json
from libs.utils.mytime import UtilTime

class LastPassBase(object):

    def __init__(self,**kwargs):
        self.secret = kwargs.get('secret')
        self.data = kwargs.get('data',{})

    def _sign(self):
        pass

class LastPass_MK(LastPassBase):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


        #生产环境
        self.create_order_url="https://new.themeeting.cn/Pay_Index.html"
        self.secret = "2pztqmsktehj76exsw1c9sjjtd4lfqmi"
        self.businessId = "10213"

        self.response = None

    def _sign(self):

        valid_data = {}
        # 去掉value为空的值
        for item in self.data:
            if str(self.data[item]) and len(str(self.data[item])):
                valid_data[item] = self.data[item]

        # 排序固定位置
        valid_data_keys = sorted(valid_data)
        valid_orders_data = OrderedDict()
        for key in valid_data_keys:
            valid_orders_data[key] = valid_data[key]

        valid_orders_data['key']=self.secret

        # 将数据变成待加密串
        encrypted = str()
        for item in valid_orders_data:
            encrypted += "{}={}&".format(item, valid_orders_data[item])
        encrypted = encrypted[:-1].encode("utf-8")
        self.data['pay_md5sign'] = hashlib.md5(encrypted).hexdigest().upper()

    def check_sign(self):
        sign = self.data.pop('sign',False)
        self._sign()
        if self.data['pay_md5sign'] != sign:
            raise PubErrorCustom("签名不正确")

    def Md5str(src):
        m = hashlib.md5(src.encode("utf8"))
        return m.hexdigest().upper()

    def obtaindate(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def _request(self):
        result = request(method='POST', url=self.create_order_url, data=self.data, verify=True)

        self.response = result.text
        logger.info(self.response)

    def run(self):
        self.data.setdefault('pay_memberid',self.businessId)
        self.data.setdefault('pay_applydate',self.obtaindate())
        # self.data.setdefault('pay_bankcode',"904")
        self.data.setdefault('pay_callbackurl',url_join("/pay/#/juli"))
        self._sign()

        self.data.setdefault('pay_productname',"商品")

        return self.data

    def call_run(self):
        self.check_sign()
        if not self.data.get("memberid") or self.data.get("memberid")!= self.businessId:
            raise PubErrorCustom("商户ID不存在!")
        if not self.data.get("amount") :
            raise PubErrorCustom("金额不能为空!")
        if not self.data.get("orderid"):
            raise PubErrorCustom("商户订单号为空!")

        if self.data.get("returncode") == '00':
            try:
                order = Order.objects.select_for_update().get(ordercode=self.data.get("orderid"))
            except Order.DoesNotExist:
                raise PubErrorCustom("订单号不正确!")

            if order.status == '0':
                raise PubErrorCustom("订单已处理!")

            PayCallLastPass().run(order=order)



if __name__=='__main__':
    md5params = "{}{}{}{}{}{}{}".format(
        '4S4G7CBWJHYAD5ZE',
        "5",
        "13",
        "fdsafs1fsdf1sf1ds21212312321dfd123ffd312df312121332131332",
        "192.168.0.1",
        "200.00",
        '4S4G7CBWJHYAD5ZE')
    md5params = md5params.encode("utf-8")

    sign = hashlib.md5(md5params).hexdigest()
    print(sign)
