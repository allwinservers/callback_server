from rest_framework import (viewsets)

from education.settings import ServerUrl
from apps.user.models import Users,BalList
from utils.exceptions import PubErrorCustom
from   django_redis  import   get_redis_connection
import json
from libs.utils.log import logger

from libs.utils.mytime import UtilTime

class GenericViewSetCustom(viewsets.ViewSet):
    pass

def url_join(path=None):
    return "{}{}".format(ServerUrl,path) if path else ServerUrl

# class AccountHandler(object):
#
#     def __init__(self,**kwargs):
#         # 是否充值
#         self.isPay = kwargs.get('isPay', False)
#
#         # 是否提现
#         self.isCashout = kwargs.get('isCashout', False)
#
#         # 是否提现拒绝
#         self.isCashoutCanle = kwargs.get('isCashoutCanle', False)
#
#         # 是否提现确认
#         self.isCashoutConfirm = kwargs.get('isCashoutConfirm', False)
#
#         # 是否冻结
#         self.isStop = kwargs.get('isStop', False)
#
#         # 是否解冻
#         self.isStopCanle  = kwargs.get('isStopCanle', False)
#
#         userid = kwargs.get('userid', None)
#         if not userid:
#             raise PubErrorCustom("用户代码不能为空!")
#
#         self.amount = kwargs.get('amount', None)
#         if not self.amount:
#             raise PubErrorCustom("交易金额不能为空!")
#         else:
#             self.amount = float(self.amount)
#
#         self.ordercode = kwargs.get('ordercode', 0)
#
#         try:
#             self.user = Users.objects.select_for_update().get(userid=userid)
#         except Users.DoesNotExist:
#             raise PubErrorCustom("无对应用户信息({})".format(userid))
#
#         self.today = UtilTime().arrow_to_string(format_v="YYYYMMDD")
#
#     def isUpdDate(self):
#         if self.user.upd_bal_date >= self.today:
#             return False
#         else:
#             return True
#
#     def AccountListInsert(self,memo):
#         BalList.objects.create(**{
#             "userid" : self.user.userid,
#             "amount" : self.amount,
#             "bal" : self.user.bal,
#             "confirm_bal" : float(self.user.bal) + float(self.amount),
#             "memo" : memo,
#             "ordercode": self.ordercode
#         })
#
#     def run(self):
#
#         logger.info("""动账前: userid:{} amount:{} ordercode:{} upd_bal_date:{} bal:{} cashout_bal:{} stop_bal:{} lastday_bal:{}
#                     today_bal:{} lastday_pay_amount:{} today_pay_amount:{} tot_pay_amount:{} lastday_cashout_amount:{} today_cashout_amount:{}
#                         tot_cashout_amount:{}""".format(
#             self.user.userid,
#             self.amount,
#             self.ordercode,
#             self.user.upd_bal_date,
#             self.user.bal,
#             self.user.cashout_bal,
#             self.user.stop_bal,
#             self.user.lastday_bal,
#             self.user.today_bal,
#             self.user.lastday_pay_amount,
#             self.user.today_pay_amount,
#             self.user.tot_pay_amount,
#             self.user.lastday_cashout_amount,
#             self.user.today_cashout_amount,
#             self.user.tot_cashout_amount))
#
#         if self.isUpdDate():
#             self.user.today_bal = 0.0
#             self.user.lastday_bal = self.user.bal
#
#             self.user.today_pay_amount = 0.0
#             self.user.lastday_pay_amount = self.user.today_pay_amount
#
#             self.user.today_cashout_amount = 0.0
#             self.user.lastday_cashout_amount = self.user.tot_cashout_amount
#
#             self.user.upd_bal_date = self.today
#
#         if self.isPay:
#             logger.info("充值")
#             self.AccountListInsert("充值")
#             self.user.today_pay_amount = float(self.user.today_pay_amount) + self.amount
#             self.user.tot_pay_amount = float(self.user.tot_pay_amount) + self.amount
#
#             self.user.today_bal = float(self.user.today_bal) + self.amount
#             self.user.bal = float(self.user.bal) + self.amount
#
#         elif self.isCashout:
#             self.user.cashout_bal = float(self.user.cashout_bal) + self.amount
#
#         elif self.isCashoutCanle:
#             self.user.cashout_bal = float(self.user.cashout_bal) + self.amount * -1
#
#         elif self.isCashoutConfirm:
#             logger.info("提现")
#             self.amount = self.amount * -1
#             self.AccountListInsert("提现")
#
#             self.user.today_cashout_amount = float(self.user.today_cashout_amount) + self.amount * -1
#             self.user.tot_cashout_amount = float(self.user.tot_cashout_amount) + self.amount * -1
#
#             self.user.cashout_bal = float(self.user.cashout_bal) + self.amount
#             self.user.today_bal = float(self.user.today_bal) + self.amount
#             self.user.bal = float(self.user.bal) + self.amount
#         elif self.isStop:
#             logger.info("冻结")
#             self.amount = self.amount * -1
#             self.AccountListInsert("冻结")
#
#             self.user.stop_bal = float(self.user.stop_bal) + self.amount * -1
#
#             self.user.today_bal = float(self.user.today_bal) + self.amount
#             self.user.bal = float(self.user.bal) + self.amount
#
#         elif self.isStopCanle:
#             logger.info("解冻")
#             self.AccountListInsert("解冻")
#
#             self.user.stop_bal = float(self.user.stop_bal) + self.amount * -1
#
#             self.user.today_bal = float(self.user.today_bal) + self.amount
#             self.user.bal = float(self.user.bal) + self.amount
#
#         else:
#             raise PubErrorCustom("账务标识有误!")
#
#         logger.info("""动账后: upd_bal_date:{} bal:{} cashout_bal:{} stop_bal:{} lastday_bal:{}
#                     today_bal:{} lastday_pay_amount:{} today_pay_amount:{} tot_pay_amount:{} lastday_cashout_amount:{} today_cashout_amount:{}
#                         tot_cashout_amount:{}""".format(
#             self.user.upd_bal_date,
#             self.user.bal,
#             self.user.cashout_bal,
#             self.user.stop_bal,
#             self.user.lastday_bal,
#             self.user.today_bal,
#             self.user.lastday_pay_amount,
#             self.user.today_pay_amount,
#             self.user.tot_pay_amount,
#             self.user.lastday_cashout_amount,
#             self.user.today_cashout_amount,
#             self.user.tot_cashout_amount))
#
#
#
#         self.user.save()
#         return self.user


# def upd_bal(**kwargs):
#
#     userid = kwargs.get('userid',None)
#     bal = kwargs.get('bal',None)
#     cashout_bal = kwargs.get('cashout_bal',None)
#     up_bal = kwargs.get('up_bal',None)
#     upd_bal = kwargs.get('flag',None)
#     upd_business_agent_tot = kwargs.get('upd_business_agent_tot',None)
#
#     today  = UtilTime().arrow_to_string(format_v="YYYYMMDD")
#
#     if bal:
#         bal=float(bal)
#     if cashout_bal:
#         cashout_bal=float(cashout_bal)
#     if up_bal:
#         up_bal = float(up_bal)
#
#     memo = kwargs.get("memo","修改余额")
#
#
#
#     if bal :
#         BalList.objects.create(**{
#             "userid" : user.userid,
#             "amount" : bal,
#             "bal" : user.bal,
#             "confirm_bal" : float(user.bal) + float(bal),
#             "memo" : memo,
#             "ordercode":  kwargs.get("ordercode",0)
#         })
#
#         # print("用户ID:{},更新日期:{},当日日期:{},昨日余额:{},当天余额:{},发生额{},总余额{}".format(user.userid,user.upd_bal_date,today,user.lastday_bal,user.today_bal,bal,user.bal))
#
#         if isPay:
#             if user.upd_bal_date > today:
#                 user.lastday_pay_amount = user.tot_pay_amount
#                 user.today_bal = bal
#                 user.upd_bal_date = today
#             else:
#                 user.today_bal = float(user.today_bal) + float(bal)
#         elif isCashout:
#         elif isStop:
#         else:
#             raise PubErrorCustom("动账标识有误!")
#
#         if not user.upd_bal_date:
#             user.lastday_bal = user.bal
#             user.today_bal = bal
#             user.upd_bal_date = today
#         elif len(user.upd_bal_date)==0:
#             user.lastday_bal = user.bal
#             user.today_bal = bal
#             user.upd_bal_date = today
#         elif today > user.upd_bal_date:
#             user.lastday_bal = user.bal
#             user.today_bal = bal
#             user.upd_bal_date = today
#         else:
#             user.today_bal = float(user.today_bal) + float(bal)
#
#         user.bal = float(user.bal) + float(bal)
#
#         # print("更新日期:{},当日日期:{},昨日余额:{},当天余额:{},发生额{},总余额{}".format(user.upd_bal_date,today,user.lastday_bal,user.today_bal,bal,user.bal))
#
#     if cashout_bal:
#         user.cashout_bal = float(user.cashout_bal) + float(cashout_bal)
#
#     if up_bal:
#         user.up_bal = float(user.up_bal) + float(up_bal)
#
#     user.save()
#
#     return user

class RedisHandler(object):
    def __init__(self,**kwargs):
        self.redis_client = get_redis_connection(kwargs.get("db"))
        self.key = kwargs.get("key")

    def redis_dict_insert(self,value):
        self.redis_client.set(self.key,json.dumps(value))

    def redis_dict_get(self):
        res = self.redis_client.get(self.key)
        return json.loads(res) if res else res

class RedisOrderCount(RedisHandler):

    def __init__(self,**kwargs):
        kwargs.setdefault('key',"ordercount")
        kwargs.setdefault('db','orders')
        super().__init__(**kwargs)

    def redis_dict_insert(self,userid,value):
        self.redis_client.hset(self.key,userid,json.dumps(value))

    def redis_dict_get(self,userid):
        res = self.redis_client.hget(self.key,userid)
        return json.loads(res) if res else res


