from typing import List, Dict
from aiohttp import web

from openapi_server.models.node import Node
from openapi_server.models.view_only_links import ViewOnlyLinks
from openapi_server import util


async def view_only_links_node_list(request: web.Request, link_id) -> web.Response:
    """List all nodes

     The list of nodes which this view only link gives read-only access to. #### Permissions Only project administrators may retrieve the nodes of a view only link. Attempting to retrieve a view only link without appropriate permissions will result in a 403 Forbidden response. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys. The &#x60;data&#x60; key contains an array of up to 10 nodes. Each resource in the array is a separate node object and contains the full representation of the node, meaning additional requests to a node&#39;s detail view are not necessary.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param link_id: The unique identifier of the view only link.
    :type link_id: str

    """
    return web.Response(status=200)


async def view_only_links_read(request: web.Request, link_id) -> web.Response:
    """Retrieve a view only link

    Retrieves details about a specific view only link. #### Permissions Only project administrators may retrieve the details of a view only link. Attempting to retrieve a view only link without appropriate permissions will result in a 403 Forbidden response. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested view only link, if the request is successful. If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

    :param link_id: The unique identifier of the view only link.
    :type link_id: str

    """
    return web.Response(status=200)
