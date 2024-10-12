from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_floating_ip_request import CreateFloatingIPRequest
from openapi_server.models.floating_ips_get200_response import FloatingIpsGet200Response
from openapi_server.models.floating_ips_id_get200_response import FloatingIpsIdGet200Response
from openapi_server.models.floating_ips_post201_response import FloatingIpsPost201Response
from openapi_server.models.update_floating_ip_request import UpdateFloatingIPRequest
from openapi_server import util


async def floating_ips_get(request: web.Request, name=None, label_selector=None, sort=None) -> web.Response:
    """Get all Floating IPs

    Returns all Floating IP objects.

    :param name: Can be used to filter Floating IPs by their name. The response will only contain the Floating IP matching the specified name.
    :type name: str
    :param label_selector: Can be used to filter Floating IPs by labels. The response will only contain Floating IPs matching the label selector.
    :type label_selector: str
    :param sort: Can be used multiple times. Choices id id:asc id:desc created created:asc created:desc
    :type sort: str

    """
    return web.Response(status=200)


async def floating_ips_id_delete(request: web.Request, id) -> web.Response:
    """Delete a Floating IP

    Deletes a Floating IP. If it is currently assigned to a Server it will automatically get unassigned.

    :param id: ID of the Floating IP
    :type id: int

    """
    return web.Response(status=200)


async def floating_ips_id_get(request: web.Request, id) -> web.Response:
    """Get a Floating IP

    Returns a specific Floating IP object.

    :param id: ID of the Floating IP
    :type id: int

    """
    return web.Response(status=200)


async def floating_ips_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update a Floating IP

    Updates the description or labels of a Floating IP. Also note that when updating labels, the Floating IP’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.

    :param id: ID of the Floating IP
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateFloatingIPRequest.from_dict(body)
    return web.Response(status=200)


async def floating_ips_post(request: web.Request, body=None) -> web.Response:
    """Create a Floating IP

    Creates a new Floating IP assigned to a Server. If you want to create a Floating IP that is not bound to a Server, you need to provide the &#x60;home_location&#x60; key instead of &#x60;server&#x60;. This can be either the ID or the name of the Location this IP shall be created in. Note that a Floating IP can be assigned to a Server in any Location later on. For optimal routing it is advised to use the Floating IP in the same Location it was created in.

    :param body: The &#x60;type&#x60; argument is required while &#x60;home_location&#x60; and &#x60;server&#x60; are mutually exclusive.
    :type body: dict | bytes

    """
    body = CreateFloatingIPRequest.from_dict(body)
    return web.Response(status=200)
