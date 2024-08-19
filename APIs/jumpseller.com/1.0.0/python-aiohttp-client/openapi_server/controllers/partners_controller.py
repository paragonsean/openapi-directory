from typing import List, Dict
from aiohttp import web

from openapi_server.models.partner_error import PartnerError
from openapi_server.models.partner_store_code import PartnerStoreCode
from openapi_server.models.partner_store_create import PartnerStoreCreate
from openapi_server.models.store_check_status_json_get200_response import StoreCheckStatusJsonGet200Response
from openapi_server.models.type import Type
from openapi_server import util


async def partners_stores_json_get(request: web.Request, partner_code, auth_token, _from, to, page=None) -> web.Response:
    """Retrieve statistics.

    

    :param partner_code: Partner code.
    :type partner_code: str
    :param auth_token: Partner authentication token.
    :type auth_token: str
    :param _from: Statistics start date. Should be in format &#39;Y-m-d&#39;.
    :type _from: str
    :param to: Statistics end date. Should be in format &#39;Y-m-d&#39;.
    :type to: str
    :param page: List page
    :type page: int

    """
    return web.Response(status=200)


async def store_check_status_json_get(request: web.Request, partner_code, auth_token, store_code, locale=None) -> web.Response:
    """Retrive store creation status.

    

    :param partner_code: Partner code.
    :type partner_code: str
    :param auth_token: Partner authentication token.
    :type auth_token: str
    :param store_code: Store Code
    :type store_code: str
    :param locale: ISO 3166-2 code of the language used in the response messages.
    :type locale: str

    """
    return web.Response(status=200)


async def store_create_json_post(request: web.Request, partner_code, auth_token, body) -> web.Response:
    """Create a Partnered Store

    

    :param partner_code: Partner code.
    :type partner_code: str
    :param auth_token: Partner authentication token.
    :type auth_token: str
    :param body: New partnered Store parameters.
    :type body: dict | bytes

    """
    body = PartnerStoreCreate.from_dict(body)
    return web.Response(status=200)
