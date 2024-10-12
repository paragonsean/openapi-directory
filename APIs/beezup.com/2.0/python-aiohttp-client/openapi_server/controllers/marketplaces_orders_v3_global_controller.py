from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_synchronization_list import AccountSynchronizationList
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.error_response_message import ErrorResponseMessage
from openapi_server.models.list_of_value_item import ListOfValueItem
from openapi_server import util


async def get_marketplace_accounts_synchronization_v3(request: web.Request, if_none_match=None, store_ids=None) -> web.Response:
    """get_marketplace_accounts_synchronization_v3

    Get current synchronization status between your marketplaces and BeezUP accounts

    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str
    :param store_ids: StoredIds to filter
    :type store_ids: List[str]

    """
    return web.Response(status=200)


async def get_order_management_ready_marketplace_business_code(request: web.Request, accept_language=None, store_ids=None) -> web.Response:
    """get_order_management_ready_marketplace_business_code

    Get the list of MarketplaceBusinessCode ready for Order Management

    :param accept_language: Indicates that the client accepts the following languages.
    :type accept_language: List[str]
    :param store_ids: StoredIds to filter
    :type store_ids: List[str]

    """
    return web.Response(status=200)


async def harvest_all_v3(request: web.Request, store_id=None) -> web.Response:
    """Send harvest request to all your marketplaces

    

    :param store_id: The StoreId to filter by
    :type store_id: str

    """
    return web.Response(status=200)
