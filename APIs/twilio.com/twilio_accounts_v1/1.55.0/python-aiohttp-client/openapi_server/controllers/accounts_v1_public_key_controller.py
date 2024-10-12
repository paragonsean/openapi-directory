from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_v1_credential_credential_public_key import AccountsV1CredentialCredentialPublicKey
from openapi_server.models.list_credential_public_key_response import ListCredentialPublicKeyResponse
from openapi_server import util


async def create_credential_public_key(request: web.Request, public_key, account_sid=None, friendly_name=None) -> web.Response:
    """create_credential_public_key

    Create a new Public Key Credential

    :param public_key: A URL encoded representation of the public key. For example, &#x60;-----BEGIN PUBLIC KEY-----MIIBIjANB.pa9xQIDAQAB-----END PUBLIC KEY-----&#x60;
    :type public_key: str
    :param account_sid: The SID of the Subaccount that this Credential should be associated with. Must be a valid Subaccount of the account issuing the request
    :type account_sid: str
    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)


async def delete_credential_public_key(request: web.Request, sid) -> web.Response:
    """delete_credential_public_key

    Delete a Credential from your account

    :param sid: The Twilio-provided string that uniquely identifies the PublicKey resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_credential_public_key(request: web.Request, sid) -> web.Response:
    """fetch_credential_public_key

    Fetch the public key specified by the provided Credential Sid

    :param sid: The Twilio-provided string that uniquely identifies the PublicKey resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_credential_public_key(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_credential_public_key

    Retrieves a collection of Public Key Credentials belonging to the account used to make the request

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_credential_public_key(request: web.Request, sid, friendly_name=None) -> web.Response:
    """update_credential_public_key

    Modify the properties of a given Account

    :param sid: The Twilio-provided string that uniquely identifies the PublicKey resource to update.
    :type sid: str
    :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)
