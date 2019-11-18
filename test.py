
from requests import request
import json
import hashlib



def testRequest():
    url = "http://localhost:9001/api_new/business/create_order"
    secret = "4S4G7CBWJHYAD5ZE"

    data=dict(
        businessid = "5",
        paytypeid = "1",
        down_ordercode = "118121dd111dd2211241",
        amount = 100,
        client_ip = "192.168.0.1",
        notifyurl = "http://www.baidu.com",
        ismobile = "1"
    )

    encrypted = "{}{}{}{}{}{}{}".format(
        secret,
        str(data['businessid']),
        str(data['paytypeid']),
        str(data['down_ordercode']),
        str(data['client_ip']),
        str(data['amount']),
        secret
    ).encode("utf-8")

    data['sign'] = hashlib.md5(encrypted).hexdigest()

    res = request(url=url,data=data,method='POST')

    print(res.text)



if __name__ == '__main__':
    testRequest()