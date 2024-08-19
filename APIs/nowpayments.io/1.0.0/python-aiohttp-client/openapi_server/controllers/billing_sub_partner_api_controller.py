from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_all_transfers200_response import GetAllTransfers200Response
from openapi_server.models.get_sub_partner_balance200_response import GetSubPartnerBalance200Response
from openapi_server.models.get_transfer200_response import GetTransfer200Response
from openapi_server import util


async def get_all_transfers(request: web.Request, id=None, status=None, limit=None, offset=None, order=None) -> web.Response:
    """Get all transfers

    Returns the entire list of transfers created by your sub-partners.

    :param id: int or array of int (optional)
    :type id: str
    :param status: string or array of string  \&quot;WAITING\&quot;/\&quot;CREATED\&quot;/\&quot;FINISHED\&quot;/\&quot;REJECTED\&quot; (optional)
    :type status: str
    :param limit: (optional) default 10
    :type limit: str
    :param offset: (optional) default 0
    :type offset: str
    :param order: ASC / DESC (optional) default ASC
    :type order: str

    """
    return web.Response(status=200)


async def get_sub_partner_balance(request: web.Request, id, x_api_key=None) -> web.Response:
    """Get sub-partner balance

    This request can be made only from a whitelisted IP.   If IP whitelisting is disabled, this request can be made by any user that has an API key.

    :param id: 
    :type id: str
    :param x_api_key: 
    :type x_api_key: str

    """
    return web.Response(status=200)


async def get_sub_partners(request: web.Request, id=None, offset=None, limit=None, order=None) -> web.Response:
    """Get sub-partners

    This method returns the entire list of your sub-partners.

    :param id: int or array of int (optional)
    :type id: str
    :param offset: (optional) default 0
    :type offset: str
    :param limit: (optional) default 10
    :type limit: str
    :param order: ASC / DESC (optional) default ASC
    :type order: str

    """
    return web.Response(status=200)


async def get_transfer(request: web.Request, id) -> web.Response:
    """Get transfer

    Get the actual information about the transfer. You need to provide the transfer ID in the request.

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
