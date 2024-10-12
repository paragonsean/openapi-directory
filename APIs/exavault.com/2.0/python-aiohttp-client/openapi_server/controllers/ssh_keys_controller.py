from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_ssh_key_request_body import AddSSHKeyRequestBody
from openapi_server.models.ssh_key_collection_response import SSHKeyCollectionResponse
from openapi_server.models.ssh_key_response import SSHKeyResponse
from openapi_server import util


async def add_ssh_key(request: web.Request, ev_api_key, ev_access_token, body=None) -> web.Response:
    """Create a new SSH Key

    Create a new SSH Key for a user. Provide the Public Key as formatted from the ssh-keygen command (openssh format or RFC-4716 format).  If you&#39;d prefer to let us generate your key automatically, you can log in to your account via the web portal and set up new keys via the SSH Keys page. 

    :param ev_api_key: API key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddSSHKeyRequestBody.from_dict(body)
    return web.Response(status=200)


async def delete_ssh_key(request: web.Request, id, ev_api_key, ev_access_token) -> web.Response:
    """Delete an SSH Key

    Delete the specified SSH key. This will not delete or deactivate the user tied to the key.

    :param id: 
    :type id: str
    :param ev_api_key: API key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str

    """
    return web.Response(status=200)


async def get_ssh_key(request: web.Request, id, ev_api_key, ev_access_token) -> web.Response:
    """Get metadata for an SSH Key

    Return the information for a single SSH Key

    :param id: 
    :type id: str
    :param ev_api_key: API key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str

    """
    return web.Response(status=200)


async def get_ssh_keys_list(request: web.Request, ev_api_key, ev_access_token, user_id=None, limit=None, offset=None) -> web.Response:
    """Get metadata for a list of SSH Keys

    Returns a list of SSH Keys within the account. Can be filtered for a single user.

    :param ev_api_key: API key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param user_id:  Only return results for the given user ID. This is not the username, but the numeric ID of the user.
    :type user_id: str
    :param limit:  Limits the results by the given number. Cannot be set higher than 100.
    :type limit: int
    :param offset:  Determines which item to start on for pagination. Use zero (0) to start at the beginning of the list.
    :type offset: int

    """
    return web.Response(status=200)
