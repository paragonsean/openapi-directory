from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_credential_list_response import ListCredentialListResponse
from openapi_server.models.trunking_v1_trunk_credential_list import TrunkingV1TrunkCredentialList
from openapi_server import util


async def create_credential_list(request: web.Request, trunk_sid, credential_list_sid) -> web.Response:
    """create_credential_list

    

    :param trunk_sid: The SID of the Trunk to associate the credential list with.
    :type trunk_sid: str
    :param credential_list_sid: The SID of the [Credential List](https://www.twilio.com/docs/voice/sip/api/sip-credentiallist-resource) that you want to associate with the trunk. Once associated, we will authenticate access to the trunk against this list.
    :type credential_list_sid: str

    """
    return web.Response(status=200)


async def delete_credential_list(request: web.Request, trunk_sid, sid) -> web.Response:
    """delete_credential_list

    

    :param trunk_sid: The SID of the Trunk from which to delete the credential list.
    :type trunk_sid: str
    :param sid: The unique string that we created to identify the CredentialList resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_credential_list(request: web.Request, trunk_sid, sid) -> web.Response:
    """fetch_credential_list

    

    :param trunk_sid: The SID of the Trunk from which to fetch the credential list.
    :type trunk_sid: str
    :param sid: The unique string that we created to identify the CredentialList resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_credential_list(request: web.Request, trunk_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_credential_list

    

    :param trunk_sid: The SID of the Trunk from which to read the credential lists.
    :type trunk_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
