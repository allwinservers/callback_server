

from apps.utils import GenericViewSetCustom
from rest_framework.decorators import list_route
from core.decorator.response import Core_connector
from utils.exceptions import PubErrorCustom,InnerErrorCustom
from utils.log import logger
from apps.lastpass.utils import LastPass_JLF,LastPass_TY,LastPass_DD,LastPass_YZL,LastPass_OSB,LastPass_BAOZHUANKA,\
    LastPass_LIMAFU,LastPass_JUXING,LastPass_MK,LastPass_TONGYU,LastPass_JIAE,LastPass_DONGFANG,\
        LastPass_XIONGMAO,LastPass_KUAILAI,LastPass_SHANGHU,LastPass_HAOYUN,LastPass_FENGNIAO,LastPass_LIANJINHAI,LastPass_JIUFU,LastPass_XINGYUANFU,LastPass_CHUANGYUAN,\
            LastPass_WXHFYS,LastPass_SDGY,LastPass_JIABAO,LastPass_QIANWANG,LastPass_CHUANGYUAN_YUANSHENG,LastPass_GUAISHOU,LastPass_TIGER,LastPass_CZKJ,LastPass_YUANLAI,\
                LastPass_JINGSHA,LastPass_XINGHE,LastPass_ANJIE,LastPass_hahapay,LastPass_SHUIJING,LastPass_ALLWIN,LastPass_SHUIJING_NEW,LastPass_YANXINGZHIFU,LastPass_BAWANGKUAIJIE,\
                    LastPass_JINGDONG,ShouGongHandler,LastPass_JIAHUI,LastPass_ZHONGXING,LastPass_ZHAOXING,LastPass_TIANCHENG,LastPass_IPAYZHIFUBAO,LastPass_YSLH,LastPass_JUXINGNEW,LastPassBase
from rest_framework.response import Response
from django.db import transaction
from functools import wraps
from django.shortcuts import HttpResponse
from core.http.response import HttpResponse as HttpResponseNew
import json

class Error_Core_connector:
    def __init__(self,**kwargs):
        pass
    def __run(self,func,outside_self,request,*args, **kwargs):
        with transaction.atomic():
            res = func(outside_self, request, *args, **kwargs)

    def __call__(self,func):
        @wraps(func)
        def wrapper(outside_self,request,*args, **kwargs):
            try:
                self.__run(func,outside_self,request,*args, **kwargs)
                return HttpResponse("OK")
            except PubErrorCustom as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),e.msg))
                a=1/0
            except Exception as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),str(e)))
                a=1/0
        return wrapper

class Gs_Core_connector:
    def __init__(self,**kwargs):
        pass
    def __run(self,func,outside_self,request,*args, **kwargs):
        with transaction.atomic():
            res = func(outside_self, request, *args, **kwargs)

    def __call__(self,func):
        @wraps(func)
        def wrapper(outside_self,request,*args, **kwargs):
            try:
                self.__run(func,outside_self,request,*args, **kwargs)
                return HttpResponse("success")
            except PubErrorCustom as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),e.msg))
                return HttpResponse("error")
            except Exception as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),str(e)))
                return HttpResponse("error")
        return wrapper

class Lmf_Core_connector1:
    def __init__(self,**kwargs):
        pass
    def __run(self,func,outside_self,request,*args, **kwargs):
        with transaction.atomic():
            res = func(outside_self, request, *args, **kwargs)

    def __call__(self,func):
        @wraps(func)
        def wrapper(outside_self,request,*args, **kwargs):
            try:
                self.__run(func,outside_self,request,*args, **kwargs)
                return HttpResponse("SUCCESS")
            except PubErrorCustom as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),e.msg))
                return HttpResponse("SUCCESS")
            except Exception as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),str(e)))
                return HttpResponse("SUCCESS")
        return wrapper

class Jl_HttpResponse(Response):

    def __init__(self,data=None):
        super().__init__(data=data)

class Jl_Core_connector:
    def __init__(self,**kwargs):
        pass
    def __run(self,func,outside_self,request,*args, **kwargs):
        with transaction.atomic():
            res = func(outside_self, request, *args, **kwargs)

    def __call__(self,func):
        @wraps(func)
        def wrapper(outside_self,request,*args, **kwargs):
            try:
                self.__run(func,outside_self,request,*args, **kwargs)
                return HttpResponse("success")
            except PubErrorCustom as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),e.msg))
                return HttpResponse("fail")
            except Exception as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),str(e)))
                return HttpResponse("fail")
        return wrapper

class ShouGong_Core_connector:
    def __init__(self,**kwargs):
        pass
    def __run(self,func,outside_self,request,*args, **kwargs):
        with transaction.atomic():
            res = func(outside_self, request, *args, **kwargs)

        if not isinstance(res, dict):
            res = {'data': None, 'msg': None, 'header': None}
        if 'data' not in res:
            res['data'] = None
        if 'msg' not in res:
            res['msg'] =  {}
        if 'header' not in res:
            res['header'] = None

        return HttpResponseNew(data= res['data'],headers=res['header'], msg=res['msg'])

    def __call__(self,func):
        @wraps(func)
        def wrapper(outside_self,request,*args, **kwargs):
            try:
                return self.__run(func,outside_self,request,*args, **kwargs)
            except PubErrorCustom as e:
                return HttpResponseNew(success=False, msg=e.msg, data=None)
            except Exception as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),str(e)))
                return HttpResponseNew("fail")
        return wrapper

class Ty_Core_connector:
    def __init__(self,**kwargs):
        pass
    def __run(self,func,outside_self,request,*args, **kwargs):
        with transaction.atomic():
            res = func(outside_self, request, *args, **kwargs)

    def __call__(self,func):
        @wraps(func)
        def wrapper(outside_self,request,*args, **kwargs):
            try:
                self.__run(func,outside_self,request,*args, **kwargs)
                return HttpResponse("OK")
            except PubErrorCustom as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),e.msg))
                return HttpResponse("fail")
            except Exception as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),str(e)))
                return HttpResponse("fail")
        return wrapper

class Yzl_Core_connector:
    def __init__(self,**kwargs):
        pass
    def __run(self,func,outside_self,request,*args, **kwargs):
        with transaction.atomic():
            res = func(outside_self, request, *args, **kwargs)

    def __call__(self,func):
        @wraps(func)
        def wrapper(outside_self,request,*args, **kwargs):
            try:
                self.__run(func,outside_self,request,*args, **kwargs)
                return HttpResponse("success")
            except PubErrorCustom as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),e.msg))
                return HttpResponse("fail")
            except Exception as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),str(e)))
                return HttpResponse("fail")
        return wrapper


class OSB_Core_connector:
    def __init__(self,**kwargs):
        pass
    def __run(self,func,outside_self,request,*args, **kwargs):
        with transaction.atomic():
            res = func(outside_self, request, *args, **kwargs)

    def __call__(self,func):
        @wraps(func)
        def wrapper(outside_self,request,*args, **kwargs):
            try:
                self.__run(func,outside_self,request,*args, **kwargs)
                return HttpResponse("success")
            except PubErrorCustom as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),e.msg))
                return HttpResponse("fail")
            except Exception as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),str(e)))
                return HttpResponse("fail")
        return wrapper

class BAOZHUANKA_Core_connector:
    def __init__(self,**kwargs):
        pass
    def __run(self,func,outside_self,request,*args, **kwargs):
        with transaction.atomic():
            res = func(outside_self, request, *args, **kwargs)

    def __call__(self,func):
        @wraps(func)
        def wrapper(outside_self,request,*args, **kwargs):
            try:
                self.__run(func,outside_self,request,*args, **kwargs)
                return HttpResponse("ok")
            except PubErrorCustom as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),e.msg))
                return HttpResponse("fail")
            except Exception as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),str(e)))
                return HttpResponse("fail")
        return wrapper

class ZHONGXING_Core_connector:
    def __init__(self,**kwargs):
        pass
    def __run(self,func,outside_self,request,*args, **kwargs):
        with transaction.atomic():
            res = func(outside_self, request, *args, **kwargs)

    def __call__(self,func):
        @wraps(func)
        def wrapper(outside_self,request,*args, **kwargs):
            try:
                self.__run(func,outside_self,request,*args, **kwargs)
                return HttpResponse("SUC")
            except PubErrorCustom as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),e.msg))
                return HttpResponse("fail")
            except Exception as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),str(e)))
                return HttpResponse("fail")
        return wrapper

class JUXING_Core_connector:
    def __init__(self,**kwargs):
        pass
    def __run(self,func,outside_self,request,*args, **kwargs):
        with transaction.atomic():
            res = func(outside_self, request, *args, **kwargs)

    def __call__(self,func):
        @wraps(func)
        def wrapper(outside_self,request,*args, **kwargs):
            try:
                self.__run(func,outside_self,request,*args, **kwargs)
                return HttpResponse("success")
            except PubErrorCustom as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),e.msg))
                return HttpResponse("fail")
            except Exception as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),str(e)))
                return HttpResponse("fail")
        return wrapper

class Lmf_Core_connector:
    def __init__(self,**kwargs):
        pass
    def __run(self,func,outside_self,request,*args, **kwargs):
        with transaction.atomic():
            res = func(outside_self, request, *args, **kwargs)

    def __call__(self,func):
        @wraps(func)
        def wrapper(outside_self,request,*args, **kwargs):
            try:
                self.__run(func,outside_self,request,*args, **kwargs)
                return HttpResponse("SUCCESS")
            except PubErrorCustom as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),e.msg))
                return HttpResponse("fail")
            except Exception as e:
                logger.error('[%s : %s  ] : [%s]'%(outside_self.__class__.__name__, getattr(func, '__name__'),str(e)))
                return HttpResponse("fail")
        return wrapper

class LastPassAPIView(GenericViewSetCustom):

    @list_route(methods=['POST'])
    @Jl_Core_connector()
    def juli_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_JLF(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @JUXING_Core_connector()
    def tianyi_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_TY(data=data).call_run()
        return None


    @list_route(methods=['POST'])
    @Ty_Core_connector()
    def mk_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_MK(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Ty_Core_connector()
    def dada_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_DD(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Yzl_Core_connector()
    def yzl_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_YZL(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @OSB_Core_connector()
    def osb_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_OSB(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @BAOZHUANKA_Core_connector()
    def baozhanka_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_BAOZHUANKA(data=data).call_run()
        return None

    @list_route(methods=['GET'])
    @Lmf_Core_connector()
    def limafu_callback(self, request, *args, **kwargs):
        data={}
        for item in request.query_params:
            data[item] = request.query_params[item]
        LastPass_LIMAFU(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @JUXING_Core_connector()
    def juxing_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_JUXING(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @JUXING_Core_connector()
    def haoyun_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_HAOYUN(data=data).call_run()
        return None

    @list_route(methods=['GET'])
    @Jl_Core_connector()
    def juli_callback_test(self, request, *args, **kwargs):
        return None

    @list_route(methods=['POST'])
    @Lmf_Core_connector()
    def tongyu_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        data1={}
        for item in data:
            data1=json.loads(item)
        data={}
        for item in data1:
            data[item] = data1[item]
        LastPass_TONGYU(data=data).call_run()
        return None


    @list_route(methods=['GET'])
    @Jl_Core_connector()
    def tianyi_callback_test(self, request, *args, **kwargs):
        return None


    @list_route(methods=['POST'])
    @JUXING_Core_connector()
    def jiae_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        print(data)
        LastPass_JIAE(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @JUXING_Core_connector()
    def xiongmao_callback(self, request, *args, **kwargs):
        data={}

        tmp = json.loads(request.data['return_type'])
        for item in tmp:
            data[item] = tmp[item]

        LastPass_XIONGMAO(data=data).call_run()
        return None


    @list_route(methods=['POST'])
    @Yzl_Core_connector()
    def dongfang_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_DONGFANG(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @JUXING_Core_connector()
    def kuailai_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        print(data)

        LastPass_KUAILAI(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Lmf_Core_connector()
    def shanghu_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        print(data)

        LastPass_SHANGHU(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @JUXING_Core_connector()
    def fengniao_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        print(data)

        LastPass_FENGNIAO(data=data).call_run()
        return None


    @list_route(methods=['POST'])
    @JUXING_Core_connector()
    def lianjinhai_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        print(data)

        LastPass_LIANJINHAI(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Ty_Core_connector()
    def jiufu_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_JIUFU(data=data).call_run()
        return None

    @list_route(methods=['GET'])
    @BAOZHUANKA_Core_connector()
    def xingyuanfu_callback(self, request, *args, **kwargs):
        data={}
        for item in request.query_params:
            data[item] = request.query_params[item]
        LastPass_XINGYUANFU(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @BAOZHUANKA_Core_connector()
    def chuangyuan_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        data1={}
        for item in data:
            data1=json.loads(item)
        data={}
        for item in data1:
            data[item] = data1[item]
        LastPass_CHUANGYUAN(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Lmf_Core_connector1()
    def wxhf_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]

        LastPass_WXHFYS(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Ty_Core_connector()
    def sdgy_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_SDGY(data=data).call_run()
        return None


    @list_route(methods=['POST'])
    @Ty_Core_connector()
    def jiabao_callback(self, request, *args, **kwargs):
        data={}
        # for item in request.data:
        #     data[item] = request.data[item]
        data['memberid'] = request.data['memberid']
        data['orderid'] = request.data['orderid']
        data['amount'] = request.data['amount']
        data['transaction_id'] = request.data['transaction_id']
        data['datetime'] = request.data['datetime']
        data['returncode'] = request.data['returncode']
        data['sign'] = request.data['sign']

        LastPass_JIABAO(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Error_Core_connector()
    def qianwang_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_QIANWANG(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Jl_Core_connector()
    def chuangyuan_yuansheng_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_CHUANGYUAN_YUANSHENG(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Gs_Core_connector()
    def guaishou_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_GUAISHOU(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Gs_Core_connector()
    def jingsha_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_JINGSHA(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Ty_Core_connector()
    def tiger_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_TIGER(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Jl_Core_connector()
    def czkj_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_CZKJ(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Jl_Core_connector()
    def yuanlai_callback(self, request, *args, **kwargs):

        data={}
        print(request.data)
        for item in request.data:
            data[item] = request.data[item]
        LastPass_YUANLAI(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Jl_Core_connector()
    def xinghe_callback(self, request, *args, **kwargs):
        data={}
        print(request.data)
        for item in request.data:
            data[item] = request.data[item]
        LastPass_XINGHE(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Jl_Core_connector()
    def anjie_callback(self, request, *args, **kwargs):
        data={}
        print(request.data)
        for item in request.data:
            data[item] = request.data[item]
        LastPass_ANJIE(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Ty_Core_connector()
    def hahapay_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_hahapay(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Jl_Core_connector()
    def shuijing_callback(self, request, *args, **kwargs):
        data={}
        print(request.data)
        for item in request.data:
            data[item] = request.data[item]
        LastPass_SHUIJING(data=data).call_run()
        return None


    @list_route(methods=['POST'])
    @Lmf_Core_connector1()
    def allwin_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_ALLWIN(data=data).call_run()
        return None


    @list_route(methods=['GET'])
    @Lmf_Core_connector()
    def shuijing_new_callback(self, request, *args, **kwargs):
        data={}
        for item in request.query_params:
            data[item] = request.query_params[item]
        print(data)
        LastPass_SHUIJING_NEW(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Ty_Core_connector()
    def yangxingzhifu_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_YANXINGZHIFU(data=data).call_run()
        return None


    @list_route(methods=['GET'])
    @Lmf_Core_connector()
    def bawangkuaijie_callback(self, request, *args, **kwargs):
        print("霸王快捷回调")
        data = {}
        for item in request.query_params:
            data[item] = request.query_params[item]
        print(data)
        LastPass_BAWANGKUAIJIE(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Jl_Core_connector()
    def jingdong_callback(self, request, *args, **kwargs):

        print("京东回调")
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_JINGDONG(data=data).call_run()
        return None


    @list_route(methods=['POST'])
    @ShouGong_Core_connector()
    def shougonghandler_callback(self, request, *args, **kwargs):

        print("手工回调")
        data={}
        for item in request.data:
            data[item] = request.data[item]
        ShouGongHandler(data=data).call_run()
        return None


    @list_route(methods=['POST'])
    @ShouGong_Core_connector()
    def messagehandler_callback(self, request, *args, **kwargs):

        print("手工通知")
        data={}
        for item in request.data:
            data[item] = request.data[item]
        ShouGongHandler(data=data).message_run()
        return None


    @list_route(methods=['POST'])
    @JUXING_Core_connector()
    def jiahui_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_JIAHUI(data=data).call_run()
        return None


    @list_route(methods=['POST'])
    @ZHONGXING_Core_connector()
    def zhongxing_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_ZHONGXING(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @BAOZHUANKA_Core_connector()
    def zhaoxing_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_ZHAOXING(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Ty_Core_connector()
    def tiancheng_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_TIANCHENG(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Gs_Core_connector()
    def ipayzhifubao_callback(self, request, *args, **kwargs):
        data = {}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_IPAYZHIFUBAO(data=data).call_run()
        return None

    @list_route(methods=['POST'])
    @Ty_Core_connector()
    def yslh_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_YSLH(data=data).call_run()
        return None


    @list_route(methods=['POST'])
    @Ty_Core_connector()
    def juxingnew_callback(self, request, *args, **kwargs):
        data={}
        for item in request.data:
            data[item] = request.data[item]
        LastPass_JUXINGNEW(data=data).call_run()
        return None

    @list_route(methods=['POST','GET'])
    def callback(self, request):

        try:
            with transaction.atomic():
                if request.method == 'POST':
                    data = {}
                    for item in request.data:
                        data[item] = request.data[item]
                else:
                    data = {}
                    for item in request.query_parms:
                        data[item] = request.query_parms[item]
                return HttpResponse(LastPassBase(data=data).call_run(request))
        except PubErrorCustom as e:
            logger.error(e.msg)
            return HttpResponse("error")
        except Exception as e:
            logger.error(str(e))
            return HttpResponse("error")

