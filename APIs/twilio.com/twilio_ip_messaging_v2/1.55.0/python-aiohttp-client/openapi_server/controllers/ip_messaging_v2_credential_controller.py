from typing import List, Dict
from aiohttp import web

from openapi_server.models.credential_enum_push_service import CredentialEnumPushService
from openapi_server.models.ip_messaging_v2_credential import IpMessagingV2Credential
from openapi_server.models.list_credential_response import ListCredentialResponse
from openapi_server import util


async def create_credential(request: web.Request, type, api_key=None, certificate=None, friendly_name=None, private_key=None, sandbox=None, secret=None) -> web.Response:
    """create_credential

    

    :param type: 
    :type type: str
    :param api_key: 
    :type api_key: str
    :param certificate: 
    :type certificate: str
    :param friendly_name: 
    :type friendly_name: str
    :param private_key: 
    :type private_key: str
    :param sandbox: 
    :type sandbox: bool
    :param secret: 
    :type secret: str

    """
    return web.Response(status=200)


async def delete_credential(request: web.Request, sid) -> web.Response:
    """delete_credential

    

    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_credential(request: web.Request, sid) -> web.Response:
    """fetch_credential

    

    :param sid: 
    :type sid: str

    """
    return web.Response(status=200)


async def list_credential(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_credential

    

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_credential(request: web.Request, sid, api_key=None, certificate=None, friendly_name=None, private_key=None, sandbox=None, secret=None) -> web.Response:
    """update_credential

    

    :param sid: 
    :type sid: str
    :param api_key: 
    :type api_key: str
    :param certificate: 
    :type certificate: str
    :param friendly_name: 
    :type friendly_name: str
    :param private_key: 
    :type private_key: str
    :param sandbox: 
    :type sandbox: bool
    :param secret: 
    :type secret: str

    """
    return web.Response(status=200)
