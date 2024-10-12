from typing import List, Dict
from aiohttp import web

from openapi_server.models.service_group_list_view_model import ServiceGroupListViewModel
from openapi_server.models.service_group_view_model import ServiceGroupViewModel
from openapi_server import util


async def consumer_v1_servicegroups_get(request: web.Request, location_id=None, offset=None, limit=None) -> web.Response:
    """List Service Groups

    &lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Service Groups&lt;/b&gt; for the requested location. If not specified, the business location defaults to the primary business location. Use the offset and limit parameters to control the page start and size. Default offset is 0, limit is 20, maximum is 100. Use the other query parameters to filter the results further.&lt;/p&gt;

    :param location_id: id of business location, defaults to primary business location
    :type location_id: str
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    return web.Response(status=200)


async def consumer_v1_servicegroups_id_get(request: web.Request, id) -> web.Response:
    """Get Service Group

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;Service Group&lt;/b&gt; object. A valid &lt;b&gt;serviceGroup id&lt;/b&gt; is required. Find serviceGroup id&#39;s by using the &lt;i&gt;GET /consumer/v1/serviceGroups&lt;/i&gt; endpoint.&lt;/p&gt;

    :param id: id of the serviceGroup object
    :type id: int

    """
    return web.Response(status=200)
