from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.contacts_destroy400_response import ContactsDestroy400Response
from openapi_server.models.mac_address import MacAddress
from openapi_server.models.mac_address_request import MacAddressRequest
from openapi_server import util


async def macs_create(request: web.Request, body=None) -> web.Response:
    """macs_create

    Register a mac address.

    :param body: MAC-Address Request
    :type body: dict | bytes

    """
    body = MacAddressRequest.from_dict(body)
    return web.Response(status=200)


async def macs_destroy(request: web.Request, id) -> web.Response:
    """macs_destroy

    Remove a mac address.

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)


async def macs_list(request: web.Request, id=None, managing_account=None, consuming_account=None, external_ref=None, network_service_config=None, address=None, assigned_at=None, valid_not_before=None, valid_not_after=None) -> web.Response:
    """macs_list

    List all mac addresses managed by the authorized customer.

    :param id: Filter by id
    :type id: List[str]
    :param managing_account: Filter by managing_account
    :type managing_account: str
    :param consuming_account: Filter by consuming_account
    :type consuming_account: str
    :param external_ref: Filter by external_ref
    :type external_ref: str
    :param network_service_config: Filter by network_service_config
    :type network_service_config: str
    :param address: Filter by address
    :type address: str
    :param assigned_at: Filter by assigned_at
    :type assigned_at: str
    :param valid_not_before: Filter by valid_not_before
    :type valid_not_before: str
    :param valid_not_after: Filter by valid_not_after
    :type valid_not_after: str

    """
    return web.Response(status=200)


async def macs_read(request: web.Request, id) -> web.Response:
    """macs_read

    Get a single mac address by it&#39;s id.

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)
