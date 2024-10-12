from typing import List, Dict
from aiohttp import web

from openapi_server.models.ssh_keys_get200_response import SshKeysGet200Response
from openapi_server.models.ssh_keys_id_put_request import SshKeysIdPutRequest
from openapi_server.models.ssh_keys_post201_response import SshKeysPost201Response
from openapi_server.models.ssh_keys_post_request import SshKeysPostRequest
from openapi_server import util


async def ssh_keys_get(request: web.Request, sort=None, name=None, fingerprint=None, label_selector=None) -> web.Response:
    """Get all SSH keys

    Returns all SSH key objects.

    :param sort: Can be used multiple times.
    :type sort: str
    :param name: Can be used to filter resources by their name. The response will only contain the resources matching the specified name
    :type name: str
    :param fingerprint: Can be used to filter SSH keys by their fingerprint. The response will only contain the SSH key matching the specified fingerprint.
    :type fingerprint: str
    :param label_selector: Can be used to filter resources by labels. The response will only contain resources matching the label selector.
    :type label_selector: str

    """
    return web.Response(status=200)


async def ssh_keys_id_delete(request: web.Request, id) -> web.Response:
    """Delete an SSH key

    Deletes an SSH key. It cannot be used anymore.

    :param id: ID of the SSH key
    :type id: str

    """
    return web.Response(status=200)


async def ssh_keys_id_get(request: web.Request, id) -> web.Response:
    """Get a SSH key

    Returns a specific SSH key object.

    :param id: ID of the SSH key
    :type id: int

    """
    return web.Response(status=200)


async def ssh_keys_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update an SSH key

    Updates an SSH key. You can update an SSH key name and an SSH key labels.  Please note that when updating labels, the SSH key current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body. 

    :param id: ID of the SSH key
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SshKeysIdPutRequest.from_dict(body)
    return web.Response(status=200)


async def ssh_keys_post(request: web.Request, body=None) -> web.Response:
    """Create an SSH key

    Creates a new SSH key with the given &#x60;name&#x60; and &#x60;public_key&#x60;. Once an SSH key is created, it can be used in other calls such as creating Servers.

    :param body: 
    :type body: dict | bytes

    """
    body = SshKeysPostRequest.from_dict(body)
    return web.Response(status=200)
