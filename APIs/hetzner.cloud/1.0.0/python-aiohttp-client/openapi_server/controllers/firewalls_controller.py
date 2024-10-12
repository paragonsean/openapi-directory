from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_firewall_request import CreateFirewallRequest
from openapi_server.models.create_firewall_response import CreateFirewallResponse
from openapi_server.models.firewall_response import FirewallResponse
from openapi_server.models.firewalls_response import FirewallsResponse
from openapi_server.models.update_firewall_request import UpdateFirewallRequest
from openapi_server import util


async def firewalls_get(request: web.Request, sort=None, name=None, label_selector=None) -> web.Response:
    """Get all Firewalls

    Returns all Firewall objects.

    :param sort: Can be used multiple times.
    :type sort: str
    :param name: Can be used to filter resources by their name. The response will only contain the resources matching the specified name
    :type name: str
    :param label_selector: Can be used to filter resources by labels. The response will only contain resources matching the label selector.
    :type label_selector: str

    """
    return web.Response(status=200)


async def firewalls_id_delete(request: web.Request, id) -> web.Response:
    """Delete a Firewall

    Deletes a Firewall.  #### Call specific error codes  | Code                 | Description                               | |--------------------- |-------------------------------------------| | &#x60;resource_in_use&#x60;    | Firewall must not be in use to be deleted | 

    :param id: ID of the resource
    :type id: int

    """
    return web.Response(status=200)


async def firewalls_id_get(request: web.Request, id) -> web.Response:
    """Get a Firewall

    Gets a specific Firewall object.

    :param id: ID of the resource
    :type id: int

    """
    return web.Response(status=200)


async def firewalls_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update a Firewall

    Updates the Firewall.  Note that when updating labels, the Firewall&#39;s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.  Note: if the Firewall object changes during the request, the response will be a “conflict” error. 

    :param id: ID of the resource
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateFirewallRequest.from_dict(body)
    return web.Response(status=200)


async def firewalls_post(request: web.Request, body=None) -> web.Response:
    """Create a Firewall

    Creates a new Firewall.  #### Call specific error codes  | Code                          | Description                                                   | |------------------------------ |-------------------------------------------------------------- | | &#x60;server_already_added&#x60;        | Server added more than one time to resource                   | | &#x60;incompatible_network_type&#x60;   | The Network type is incompatible for the given resource       | | &#x60;firewall_resource_not_found&#x60; | The resource the Firewall should be attached to was not found | 

    :param body: 
    :type body: dict | bytes

    """
    body = CreateFirewallRequest.from_dict(body)
    return web.Response(status=200)
