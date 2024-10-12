from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_sip_sip_credential_list import ApiV2010AccountSipSipCredentialList
from openapi_server.models.list_sip_credential_list_response import ListSipCredentialListResponse
from openapi_server import util


async def create_sip_credential_list(request: web.Request, account_sid, friendly_name) -> web.Response:
    """create_sip_credential_list

    Create a Credential List

    :param account_sid: The unique id of the Account that is responsible for this resource.
    :type account_sid: str
    :param friendly_name: A human readable descriptive text that describes the CredentialList, up to 64 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)


async def delete_sip_credential_list(request: web.Request, account_sid, sid) -> web.Response:
    """delete_sip_credential_list

    Delete a Credential List

    :param account_sid: The unique id of the Account that is responsible for this resource.
    :type account_sid: str
    :param sid: The credential list Sid that uniquely identifies this resource
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_sip_credential_list(request: web.Request, account_sid, sid) -> web.Response:
    """fetch_sip_credential_list

    Get a Credential List

    :param account_sid: The unique id of the Account that is responsible for this resource.
    :type account_sid: str
    :param sid: The credential list Sid that uniquely identifies this resource
    :type sid: str

    """
    return web.Response(status=200)


async def list_sip_credential_list(request: web.Request, account_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sip_credential_list

    Get All Credential Lists

    :param account_sid: The unique id of the Account that is responsible for this resource.
    :type account_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_sip_credential_list(request: web.Request, account_sid, sid, friendly_name) -> web.Response:
    """update_sip_credential_list

    Update a Credential List

    :param account_sid: The unique id of the Account that is responsible for this resource.
    :type account_sid: str
    :param sid: The credential list Sid that uniquely identifies this resource
    :type sid: str
    :param friendly_name: A human readable descriptive text for a CredentialList, up to 64 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)
