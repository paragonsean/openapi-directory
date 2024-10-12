from typing import List, Dict
from aiohttp import web

from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server.models.list_source_account_response_v2 import ListSourceAccountResponseV2
from openapi_server.models.list_source_account_response_v3 import ListSourceAccountResponseV3
from openapi_server.models.set_notifications_request import SetNotificationsRequest
from openapi_server.models.set_notifications_request2 import SetNotificationsRequest2
from openapi_server.models.source_account_response_v2 import SourceAccountResponseV2
from openapi_server.models.source_account_response_v3 import SourceAccountResponseV3
from openapi_server.models.transfer_request_v2 import TransferRequestV2
from openapi_server.models.transfer_request_v3 import TransferRequestV3
from openapi_server import util


async def get_source_account_v2(request: web.Request, source_account_id) -> web.Response:
    """Get Source Account

    Get details about given source account.

    :param source_account_id: Source account id
    :type source_account_id: str
    :type source_account_id: str

    """
    return web.Response(status=200)


async def get_source_account_v3(request: web.Request, source_account_id) -> web.Response:
    """Get details about given source account.

    Get details about given source account.

    :param source_account_id: Source account id
    :type source_account_id: str
    :type source_account_id: str

    """
    return web.Response(status=200)


async def get_source_accounts_v2(request: web.Request, physical_account_name=None, physical_account_id=None, payor_id=None, funding_account_id=None, page=None, page_size=None, sort=None) -> web.Response:
    """Get list of source accounts

    List source accounts.

    :param physical_account_name: Physical Account Name
    :type physical_account_name: str
    :param physical_account_id: The physical account ID
    :type physical_account_id: str
    :type physical_account_id: str
    :param payor_id: The account owner Payor ID
    :type payor_id: str
    :type payor_id: str
    :param funding_account_id: The funding account ID
    :type funding_account_id: str
    :type funding_account_id: str
    :param page: Page number. Default is 1.
    :type page: int
    :param page_size: The number of results to return in a page
    :type page_size: int
    :param sort: List of sort fields e.g. ?sort&#x3D;name:asc Default is name:asc The supported sort fields are - fundingRef, name, balance 
    :type sort: str

    """
    return web.Response(status=200)


async def get_source_accounts_v3(request: web.Request, physical_account_name=None, physical_account_id=None, payor_id=None, funding_account_id=None, include_user_deleted=None, type=None, page=None, page_size=None, sort=None) -> web.Response:
    """Get list of source accounts

    List source accounts.

    :param physical_account_name: Physical Account Name
    :type physical_account_name: str
    :param physical_account_id: The physical account ID
    :type physical_account_id: str
    :type physical_account_id: str
    :param payor_id: The account owner Payor ID
    :type payor_id: str
    :type payor_id: str
    :param funding_account_id: The funding account ID
    :type funding_account_id: str
    :type funding_account_id: str
    :param include_user_deleted: A filter for retrieving both active accounts and user deleted ones
    :type include_user_deleted: str
    :param type: The type of source account.
    :type type: str
    :param page: Page number. Default is 1.
    :type page: int
    :param page_size: The number of results to return in a page
    :type page_size: int
    :param sort: List of sort fields e.g. ?sort&#x3D;name:asc Default is name:asc The supported sort fields are - fundingRef, name, balance 
    :type sort: str

    """
    return web.Response(status=200)


async def set_notifications_request(request: web.Request, source_account_id, body) -> web.Response:
    """Set notifications

    &lt;p&gt;Set notifications for a given source account&lt;/p&gt; &lt;p&gt;deprecated since 2.34 (use v3 version)&lt;/p&gt; 

    :param source_account_id: Source account id
    :type source_account_id: str
    :type source_account_id: str
    :param body: Body to included minimum balance to set
    :type body: dict | bytes

    """
    body = SetNotificationsRequest.from_dict(body)
    return web.Response(status=200)


async def set_notifications_request_v3(request: web.Request, source_account_id, body) -> web.Response:
    """Set notifications

    &lt;p&gt;Set notifications for a given source account&lt;/p&gt; &lt;p&gt;If the balance falls below the amount set in the request an email notification will be sent to the email address registered in the payor profile&lt;/p&gt; 

    :param source_account_id: Source account id
    :type source_account_id: str
    :type source_account_id: str
    :param body: Body to included minimum balance to set
    :type body: dict | bytes

    """
    body = SetNotificationsRequest2.from_dict(body)
    return web.Response(status=200)


async def transfer_funds_v2(request: web.Request, source_account_id, body) -> web.Response:
    """Transfer Funds between source accounts

    Transfer funds between source accounts for a Payor. The &#39;from&#39; source account is identified in the URL, and is the account which will be debited. The &#39;to&#39; (destination) source account is in the body, and is the account which will be credited. Both source accounts must belong to the same Payor. There must be sufficient balance in the &#39;from&#39; source account, otherwise the transfer attempt will fail.

    :param source_account_id: The &#39;from&#39; source account id, which will be debited
    :type source_account_id: str
    :type source_account_id: str
    :param body: Body
    :type body: dict | bytes

    """
    body = TransferRequestV2.from_dict(body)
    return web.Response(status=200)


async def transfer_funds_v3(request: web.Request, source_account_id, body) -> web.Response:
    """Transfer Funds between source accounts

    Transfer funds between source accounts for a Payor. The &#39;from&#39; source account is identified in the URL, and is the account which will be debited. The &#39;to&#39; (destination) source account is in the body, and is the account which will be credited. Both source accounts must belong to the same Payor. There must be sufficient balance in the &#39;from&#39; source account, otherwise the transfer attempt will fail.

    :param source_account_id: The &#39;from&#39; source account id, which will be debited
    :type source_account_id: str
    :type source_account_id: str
    :param body: Body
    :type body: dict | bytes

    """
    body = TransferRequestV3.from_dict(body)
    return web.Response(status=200)
