from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.ip_address import IpAddress
from openapi_server.models.ip_address_request import IpAddressRequest
from openapi_server.models.ip_address_update import IpAddressUpdate
from openapi_server.models.ip_address_update_partial import IpAddressUpdatePartial
from openapi_server import util


async def ips_create(request: web.Request, body=None) -> web.Response:
    """ips_create

    Add an ip host address or network prefix.

    :param body: IP-Address / Prefix allocation Request
    :type body: dict | bytes

    """
    body = IpAddressRequest.from_dict(body)
    return web.Response(status=200)


async def ips_list(request: web.Request, id=None, managing_account=None, consuming_account=None, external_ref=None, network_service=None, network_service_config=None, network_feature=None, network_feature_config=None, version=None, fqdn=None, prefix_length=None, valid_not_before=None, valid_not_after=None) -> web.Response:
    """ips_list

    List all ip addresses (and prefixes).

    :param id: Filter by id
    :type id: List[str]
    :param managing_account: Filter by managing_account
    :type managing_account: str
    :param consuming_account: Filter by consuming_account
    :type consuming_account: str
    :param external_ref: Filter by external_ref
    :type external_ref: str
    :param network_service: Filter by network_service
    :type network_service: str
    :param network_service_config: Filter by network_service_config
    :type network_service_config: str
    :param network_feature: Filter by network_feature
    :type network_feature: str
    :param network_feature_config: Filter by network_feature_config
    :type network_feature_config: str
    :param version: Filter by version
    :type version: int
    :param fqdn: Filter by fqdn
    :type fqdn: str
    :param prefix_length: Filter by prefix_length
    :type prefix_length: int
    :param valid_not_before: Filter by valid_not_before
    :type valid_not_before: str
    :param valid_not_after: Filter by valid_not_after
    :type valid_not_after: str

    """
    return web.Response(status=200)


async def ips_partial_update(request: web.Request, id, body=None) -> web.Response:
    """ips_partial_update

    Update parts of an ip address.   As with the &#x60;PUT&#x60; opertaion, IP addresses, where you don&#39;t have update rights, will yield a &#x60;resource access denied&#x60; error when attempting an update.  If the ip address was allocated for you, you might not be able to change anything but the &#x60;fqdn&#x60;.

    :param id: Get by id
    :type id: str
    :param body: IP-Address Update
    :type body: dict | bytes

    """
    body = IpAddressUpdatePartial.from_dict(body)
    return web.Response(status=200)


async def ips_read(request: web.Request, id) -> web.Response:
    """ips_read

    Get a single ip addresses by it&#39;s id.

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)


async def ips_update(request: web.Request, id, body=None) -> web.Response:
    """ips_update

    Update an ip address object.  You can only update IP addresses within your current scope. Not all addresses you can read you can update.  If the ip address was allocated for you, you might not be able to change anything but the &#x60;fqdn&#x60;.

    :param id: Get by id
    :type id: str
    :param body: IP-Address Update
    :type body: dict | bytes

    """
    body = IpAddressUpdate.from_dict(body)
    return web.Response(status=200)
