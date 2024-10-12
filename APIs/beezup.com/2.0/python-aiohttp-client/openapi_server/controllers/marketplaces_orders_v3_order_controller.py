from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.change_order_reporting import ChangeOrderReporting
from openapi_server.models.error_response_message import ErrorResponseMessage
from openapi_server.models.order_history import OrderHistory
from openapi_server.models.order_with_links import OrderWithLinks
from openapi_server.models.set_merchant_order_info_request import SetMerchantOrderInfoRequest
from openapi_server import util


async def change_order_v3(request: web.Request, marketplace_technical_code, account_id, beez_up_order_id, change_order_type, user_name, test_mode=None, body=None) -> web.Response:
    """Change your marketplace Order Information (accept, ship, etc.)

    

    :param marketplace_technical_code: The marketplace technical code
    :type marketplace_technical_code: str
    :param account_id: 
    :type account_id: int
    :param beez_up_order_id: The BeezUP Order identifier
    :type beez_up_order_id: str
    :type beez_up_order_id: str
    :param change_order_type: The Order change type
    :type change_order_type: str
    :param user_name: Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application&#39;s user login.
    :type user_name: str
    :param test_mode: If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
    :type test_mode: bool
    :param body: 
    :type body: Dict[str, str]

    """
    return web.Response(status=200)


async def clear_merchant_order_info_v3(request: web.Request, marketplace_technical_code, account_id, beez_up_order_id, test_mode=None) -> web.Response:
    """Clear an Order&#39;s merchant information

    

    :param marketplace_technical_code: The marketplace technical code
    :type marketplace_technical_code: str
    :param account_id: 
    :type account_id: int
    :param beez_up_order_id: The BeezUP Order identifier
    :type beez_up_order_id: str
    :type beez_up_order_id: str
    :param test_mode: If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
    :type test_mode: bool

    """
    return web.Response(status=200)


async def get_order_change_reporting_v3(request: web.Request, marketplace_technical_code, account_id, beez_up_order_id, order_change_execution_uuid) -> web.Response:
    """Get the order change reporting

    This operation will help you to know the status of your order change operation

    :param marketplace_technical_code: The marketplace technical code
    :type marketplace_technical_code: str
    :param account_id: 
    :type account_id: int
    :param beez_up_order_id: The BeezUP Order identifier
    :type beez_up_order_id: str
    :type beez_up_order_id: str
    :param order_change_execution_uuid: The order change execution id
    :type order_change_execution_uuid: str

    """
    return web.Response(status=200)


async def get_order_history_v3(request: web.Request, marketplace_technical_code, account_id, beez_up_order_id) -> web.Response:
    """Get an Order&#39;s harvest and change history

    

    :param marketplace_technical_code: The marketplace technical code
    :type marketplace_technical_code: str
    :param account_id: 
    :type account_id: int
    :param beez_up_order_id: The BeezUP Order identifier
    :type beez_up_order_id: str
    :type beez_up_order_id: str

    """
    return web.Response(status=200)


async def get_order_v3(request: web.Request, marketplace_technical_code, account_id, beez_up_order_id, if_none_match=None) -> web.Response:
    """Get full Order and Order Item(s) properties

    

    :param marketplace_technical_code: The marketplace technical code
    :type marketplace_technical_code: str
    :param account_id: 
    :type account_id: int
    :param beez_up_order_id: The BeezUP Order identifier
    :type beez_up_order_id: str
    :type beez_up_order_id: str
    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str

    """
    return web.Response(status=200)


async def harvest_account(request: web.Request, marketplace_technical_code, account_id, marketplace_order_id=None, beez_up_order_id=None) -> web.Response:
    """Send harvest request for an Account

    

    :param marketplace_technical_code: The marketplace technical code
    :type marketplace_technical_code: str
    :param account_id: 
    :type account_id: int
    :param marketplace_order_id: 
    :type marketplace_order_id: str
    :param beez_up_order_id: 
    :type beez_up_order_id: str

    """
    return web.Response(status=200)


async def harvest_order_v3(request: web.Request, marketplace_technical_code, account_id, beez_up_order_id) -> web.Response:
    """Send harvest request for a single Order

    

    :param marketplace_technical_code: The marketplace technical code
    :type marketplace_technical_code: str
    :param account_id: 
    :type account_id: int
    :param beez_up_order_id: The BeezUP Order identifier
    :type beez_up_order_id: str
    :type beez_up_order_id: str

    """
    return web.Response(status=200)


async def head_order_v3(request: web.Request, marketplace_technical_code, account_id, beez_up_order_id, if_none_match=None) -> web.Response:
    """Get the meta information about the order (ETag, Last-Modified)

    The purpose of this operation is to reduce the bandwith usage by getting just the meta information about the order (ETag, Last-Modified) with the body. This could be useful 

    :param marketplace_technical_code: The marketplace technical code
    :type marketplace_technical_code: str
    :param account_id: 
    :type account_id: int
    :param beez_up_order_id: The BeezUP Order identifier
    :type beez_up_order_id: str
    :type beez_up_order_id: str
    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str

    """
    return web.Response(status=200)


async def set_merchant_order_info_v3(request: web.Request, marketplace_technical_code, account_id, beez_up_order_id, body, test_mode=None) -> web.Response:
    """Set an Order&#39;s merchant information

    

    :param marketplace_technical_code: The marketplace technical code
    :type marketplace_technical_code: str
    :param account_id: 
    :type account_id: int
    :param beez_up_order_id: The BeezUP Order identifier
    :type beez_up_order_id: str
    :type beez_up_order_id: str
    :param body: 
    :type body: dict | bytes
    :param test_mode: If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
    :type test_mode: bool

    """
    body = SetMerchantOrderInfoRequest.from_dict(body)
    return web.Response(status=200)
