from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_order_operation_response import BatchOrderOperationResponse
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.change_order_list_request import ChangeOrderListRequest
from openapi_server.models.change_order_list_request_v2 import ChangeOrderListRequestV2
from openapi_server.models.clear_merchant_order_info_list_request import ClearMerchantOrderInfoListRequest
from openapi_server.models.error_response_message import ErrorResponseMessage
from openapi_server.models.set_merchant_order_info_list_request import SetMerchantOrderInfoListRequest
from openapi_server import util


async def change_order_list_v2(request: web.Request, user_name, change_order_type, body, test_mode=None) -> web.Response:
    """Send a batch of operations to change your marketplace Order information: accept, ship, etc.  (max 100 items per call)

    The purpose of this operation is to reduce the amount of request to the API.  Max 100 items per call. 

    :param user_name: Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application&#39;s user login.
    :type user_name: str
    :param change_order_type: The Order change type
    :type change_order_type: str
    :param body: 
    :type body: dict | bytes
    :param test_mode: If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
    :type test_mode: bool

    """
    body = ChangeOrderListRequestV2.from_dict(body)
    return web.Response(status=200)


async def change_order_list_v3(request: web.Request, user_name, body, test_mode=None) -> web.Response:
    """Send a batch of operations to change your marketplace Order information: accept, ship, etc.  (max 100 items per call)

    The purpose of this operation is to reduce the amount of request to the API.  Max 100 items per call. 

    :param user_name: Sometimes the user in the e-commerce application is not the same as user associated with the current subscription key. We recommend providing your application&#39;s user login.
    :type user_name: str
    :param body: 
    :type body: dict | bytes
    :param test_mode: If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
    :type test_mode: bool

    """
    body = ChangeOrderListRequest.from_dict(body)
    return web.Response(status=200)


async def clear_merchant_order_info_list_v3(request: web.Request, body, test_mode=None) -> web.Response:
    """Send a batch of operations to clear an Order&#39;s merchant information (max 100 items per call)

    The purpose of this operation is to reduce the amount of request to the API.

    :param body: 
    :type body: dict | bytes
    :param test_mode: If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
    :type test_mode: bool

    """
    body = ClearMerchantOrderInfoListRequest.from_dict(body)
    return web.Response(status=200)


async def set_merchant_order_info_list_v3(request: web.Request, body, test_mode=None) -> web.Response:
    """Send a batch of operations to set an Order&#39;s merchant information  (max 100 items per call)

    The purpose of this operation is to reduce the amount of request to the API.

    :param body: 
    :type body: dict | bytes
    :param test_mode: If true, the operation will be not be sent to marketplace. But the validation will be taken in account.
    :type test_mode: bool

    """
    body = SetMerchantOrderInfoListRequest.from_dict(body)
    return web.Response(status=200)
