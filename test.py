
from requests import request
import json
import hashlib

import decimal
import demjson


def testRequest():

    res = request(url="http://allwin6666.com/api_new/business/DF_duizhang",method='GET',timeout=1000000)

    print(res.text)

class DecimalEncoder(json.JSONEncoder):
    def _iterencode(self, o, markers=None):
        if isinstance(o, decimal.Decimal):
            # wanted a simple yield str(o) in the next line,
            # but that would mean a yield on the line with super(...),
            # which wouldn't work (see my comment below), so...
            return (str(o) for o in [o])
        return super(DecimalEncoder, self)._iterencode(o, markers)

if __name__ == '__main__':
    # d={
    #     "a":decimal.Decimal('3.00')
    # }
    # print(demjson.encode(d))

    print(format(2.0010, '.2f'))
    print(type(format(2.0010, '.2f')))