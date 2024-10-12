from typing import List, Dict
from aiohttp import web

from openapi_server.models.capital_grant import CapitalGrant
from openapi_server.models.capital_grant_info import CapitalGrantInfo
from openapi_server.models.capital_grants import CapitalGrants
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server import util


async def get_grants(request: web.Request, counterparty_account_holder_id=None) -> web.Response:
    """Get a capital account

    Returns a list of grants with status and outstanding balances.

    :param counterparty_account_holder_id: The counterparty account holder id.
    :type counterparty_account_holder_id: str

    """
    return web.Response(status=200)


async def get_grants_id(request: web.Request, id) -> web.Response:
    """Get grant reference details

    Returns the details of a capital account specified in the path.

    :param id: The unique identifier of the grant.
    :type id: str

    """
    return web.Response(status=200)


async def post_grants(request: web.Request, body=None) -> web.Response:
    """Request a grant payout

    Requests the payout of the selected grant offer.

    :param body: 
    :type body: dict | bytes

    """
    body = CapitalGrantInfo.from_dict(body)
    return web.Response(status=200)
