from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_request import CreateNetworkRequest
from openapi_server.models.networks_get200_response import NetworksGet200Response
from openapi_server.models.networks_post201_response import NetworksPost201Response
from openapi_server.models.update_network_request import UpdateNetworkRequest
from openapi_server import util


async def networks_get(request: web.Request, name=None, label_selector=None) -> web.Response:
    """Get all Networks

    Gets all existing networks that you have available.

    :param name: Can be used to filter networks by their name. The response will only contain the networks matching the specified name.
    :type name: str
    :param label_selector: Can be used to filter networks by labels. The response will only contain networks with a matching label selector pattern.
    :type label_selector: str

    """
    return web.Response(status=200)


async def networks_id_delete(request: web.Request, id) -> web.Response:
    """Delete a Network

    Deletes a network. If there are Servers attached they will be detached in the background.  Note: if the network object changes during the request, the response will be a “conflict” error. 

    :param id: ID of the network
    :type id: int

    """
    return web.Response(status=200)


async def networks_id_get(request: web.Request, id) -> web.Response:
    """Get a Network

    Gets a specific network object.

    :param id: ID of the network
    :type id: int

    """
    return web.Response(status=200)


async def networks_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update a Network

    Updates the network properties.  Note that when updating labels, the network’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.  Note: if the network object changes during the request, the response will be a “conflict” error. 

    :param id: ID of the network
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkRequest.from_dict(body)
    return web.Response(status=200)


async def networks_post(request: web.Request, body=None) -> web.Response:
    """Create a Network

    Creates a network with the specified &#x60;ip_range&#x60;.  You may specify one or more &#x60;subnets&#x60;. You can also add more Subnets later by using the [add subnet action](https://docs.hetzner.cloud/#network-actions-add-a-subnet-to-a-network). If you do not specify an &#x60;ip_range&#x60; in the subnet we will automatically pick the first available /24 range for you.  You may specify one or more routes in &#x60;routes&#x60;. You can also add more routes later by using the [add route action](https://docs.hetzner.cloud/#network-actions-add-a-route-to-a-network). 

    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkRequest.from_dict(body)
    return web.Response(status=200)
