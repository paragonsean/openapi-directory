from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_sip_sip_credential_list_sip_credential import ApiV2010AccountSipSipCredentialListSipCredential
from openapi_server.models.list_sip_credential_response import ListSipCredentialResponse
from openapi_server import util


async def create_sip_credential(request: web.Request, account_sid, credential_list_sid, password, username) -> web.Response:
    """create_sip_credential

    Create a new credential resource.

    :param account_sid: The unique id of the Account that is responsible for this resource.
    :type account_sid: str
    :param credential_list_sid: The unique id that identifies the credential list to include the created credential.
    :type credential_list_sid: str
    :param password: The password that the username will use when authenticating SIP requests. The password must be a minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg &#x60;IWasAtSignal2018&#x60;)
    :type password: str
    :param username: The username that will be passed when authenticating SIP requests. The username should be sent in response to Twilio&#39;s challenge of the initial INVITE. It can be up to 32 characters long.
    :type username: str

    """
    return web.Response(status=200)


async def delete_sip_credential(request: web.Request, account_sid, credential_list_sid, sid) -> web.Response:
    """delete_sip_credential

    Delete a credential resource.

    :param account_sid: The unique id of the Account that is responsible for this resource.
    :type account_sid: str
    :param credential_list_sid: The unique id that identifies the credential list that contains the desired credentials.
    :type credential_list_sid: str
    :param sid: The unique id that identifies the resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_sip_credential(request: web.Request, account_sid, credential_list_sid, sid) -> web.Response:
    """fetch_sip_credential

    Fetch a single credential.

    :param account_sid: The unique id of the Account that is responsible for this resource.
    :type account_sid: str
    :param credential_list_sid: The unique id that identifies the credential list that contains the desired credential.
    :type credential_list_sid: str
    :param sid: The unique id that identifies the resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_sip_credential(request: web.Request, account_sid, credential_list_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sip_credential

    Retrieve a list of credentials.

    :param account_sid: The unique id of the Account that is responsible for this resource.
    :type account_sid: str
    :param credential_list_sid: The unique id that identifies the credential list that contains the desired credentials.
    :type credential_list_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_sip_credential(request: web.Request, account_sid, credential_list_sid, sid, password=None) -> web.Response:
    """update_sip_credential

    Update a credential resource.

    :param account_sid: The unique id of the Account that is responsible for this resource.
    :type account_sid: str
    :param credential_list_sid: The unique id that identifies the credential list that includes this credential.
    :type credential_list_sid: str
    :param sid: The unique id that identifies the resource to update.
    :type sid: str
    :param password: The password that the username will use when authenticating SIP requests. The password must be a minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg &#x60;IWasAtSignal2018&#x60;)
    :type password: str

    """
    return web.Response(status=200)
