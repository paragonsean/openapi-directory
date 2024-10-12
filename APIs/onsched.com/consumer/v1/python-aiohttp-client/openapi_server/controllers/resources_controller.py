from typing import List, Dict
from aiohttp import web

from openapi_server.models.resource_list_view_model import ResourceListViewModel
from openapi_server.models.resource_service_list_view_model import ResourceServiceListViewModel
from openapi_server.models.resource_view_model import ResourceViewModel
from openapi_server import util


async def consumer_v1_resources_get(request: web.Request, location_id=None, resource_group_id=None, email=None, name=None, sort_order=None, offset=None, limit=None) -> web.Response:
    """List Resources

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Resources&lt;/b&gt; associated with a business location. If not specified, the business location defaults to the primary business location. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

    :param location_id: id of business location, defaults to primary business location
    :type location_id: str
    :param resource_group_id: Filter by groupId
    :type resource_group_id: int
    :param email: Filter by email address
    :type email: str
    :param name: Search by name, supports Partial name search
    :type name: str
    :param sort_order: Specify sort order of response
    :type sort_order: str
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    return web.Response(status=200)


async def consumer_v1_resources_id_get(request: web.Request, id) -> web.Response:
    """Get Resource

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;Resource&lt;/b&gt; object. A valid &lt;b&gt;resource id&lt;/b&gt; is required. Find resource id&#39;s by using the &lt;i&gt;GET consumer/v1/resources&lt;/i&gt; endpoint. &lt;/p&gt;

    :param id: id of resource object
    :type id: int

    """
    return web.Response(status=200)


async def consumer_v1_resources_id_services_get(request: web.Request, id, offset=None, limit=None) -> web.Response:
    """Get Resource Linked Services

    &lt;p&gt;Use this endpoint to get a &lt;b&gt;List of Linked Services&lt;/b&gt; associated with the resource requested. The results are returned in pages. Use the offset and limit parameters to control the page start and size. Default offset is 0, limit is 20, the maximum limit is 100. Use the other query parameters to filter the results further.&lt;/p&gt;  &lt;p&gt;Resource linked services are used to explicitly define the services that can be booked for a specified resource. By default, all services are bookable for any resource. For more information: &lt;a href&#x3D;\&quot;https://docs.onsched.com/docs/linked-services\&quot;&gt;Linked Services Overview&lt;/a&gt;&lt;/p&gt;

    :param id: id of resource object
    :type id: int
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    return web.Response(status=200)
