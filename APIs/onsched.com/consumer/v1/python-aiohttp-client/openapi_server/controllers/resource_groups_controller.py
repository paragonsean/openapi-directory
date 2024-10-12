from typing import List, Dict
from aiohttp import web

from openapi_server.models.resource_group_list_view_model import ResourceGroupListViewModel
from openapi_server.models.resource_group_view_model import ResourceGroupViewModel
from openapi_server import util


async def consumer_v1_resourcegroups_get(request: web.Request, location_id=None, deleted=None, offset=None, limit=None) -> web.Response:
    """List Resource Groups

    &lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Resource Groups&lt;/b&gt; for the requested location. If not specified, the business location defaults to the primary business location.&lt;/p&gt;

    :param location_id: id of business location, defaults to primary business location
    :type location_id: str
    :param deleted: Filter results by deleted status
    :type deleted: bool
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    return web.Response(status=200)


async def consumer_v1_resourcegroups_id_get(request: web.Request, id) -> web.Response:
    """Get Resource Group

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;Resource Group&lt;/b&gt; object. A valid &lt;b&gt;resourceGroup id&lt;/b&gt; is required. Find resourceGroup id&#39;s by using the &lt;i&gt;GET /consumer/v1/resourceGroups&lt;/i&gt; endpoint.&lt;/p&gt;

    :param id: id of the resourceGroup object
    :type id: str

    """
    return web.Response(status=200)
