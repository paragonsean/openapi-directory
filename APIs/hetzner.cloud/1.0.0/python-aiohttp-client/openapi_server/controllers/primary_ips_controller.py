from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_primary_ip_request import CreatePrimaryIPRequest
from openapi_server.models.create_primary_ip_response import CreatePrimaryIPResponse
from openapi_server.models.primary_ip_response import PrimaryIPResponse
from openapi_server.models.primary_ips_response import PrimaryIPsResponse
from openapi_server.models.update_primary_ip_request import UpdatePrimaryIPRequest
from openapi_server import util


async def primary_ips_get(request: web.Request, name=None, label_selector=None, ip=None, sort=None) -> web.Response:
    """Get all Primary IPs

    Returns all Primary IP objects.

    :param name: Can be used to filter resources by their name. The response will only contain the resources matching the specified name
    :type name: str
    :param label_selector: Can be used to filter resources by labels. The response will only contain resources matching the label selector.
    :type label_selector: str
    :param ip: Can be used to filter resources by their ip. The response will only contain the resources matching the specified ip.
    :type ip: str
    :param sort: Can be used multiple times. Choices id id:asc id:desc created created:asc created:desc
    :type sort: str

    """
    return web.Response(status=200)


async def primary_ips_id_delete(request: web.Request, id) -> web.Response:
    """Delete a Primary IP

    Deletes a Primary IP.  The Primary IP may be assigned to a Server. In this case it is unassigned automatically. The Server must be powered off (status &#x60;off&#x60;) in order for this operation to succeed. 

    :param id: ID of the resource
    :type id: int

    """
    return web.Response(status=200)


async def primary_ips_id_get(request: web.Request, id) -> web.Response:
    """Get a Primary IP

    Returns a specific Primary IP object.

    :param id: ID of the resource
    :type id: int

    """
    return web.Response(status=200)


async def primary_ips_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update a Primary IP

    Updates the Primary IP.  Note that when updating labels, the Primary IP&#39;s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.  If the Primary IP object changes during the request, the response will be a “conflict” error. 

    :param id: ID of the resource
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UpdatePrimaryIPRequest.from_dict(body)
    return web.Response(status=200)


async def primary_ips_post(request: web.Request, body=None) -> web.Response:
    """Create a Primary IP

    Creates a new Primary IP, optionally assigned to a Server.  If you want to create a Primary IP that is not assigned to a Server, you need to provide the &#x60;datacenter&#x60; key instead of &#x60;assignee_id&#x60;. This can be either the ID or the name of the Datacenter this Primary IP shall be created in.  Note that a Primary IP can only be assigned to a Server in the same Datacenter later on.  #### Call specific error codes  | Code                          | Description                                                   | |------------------------------ |-------------------------------------------------------------- | | &#x60;server_not_stopped&#x60;          | The specified server is running, but needs to be powered off  | | &#x60;server_has_ipv4&#x60;             | The server already has an ipv4 address                        | | &#x60;server_has_ipv6&#x60;             | The server already has an ipv6 address                        | 

    :param body: The &#x60;type&#x60; argument is required while &#x60;datacenter&#x60; and &#x60;assignee_id&#x60; are mutually exclusive.
    :type body: dict | bytes

    """
    body = CreatePrimaryIPRequest.from_dict(body)
    return web.Response(status=200)
