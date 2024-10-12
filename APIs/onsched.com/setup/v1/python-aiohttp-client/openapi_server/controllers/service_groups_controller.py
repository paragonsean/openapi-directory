from typing import List, Dict
from aiohttp import web

from openapi_server.models.service_group_input_model import ServiceGroupInputModel
from openapi_server.models.service_group_list_view_model import ServiceGroupListViewModel
from openapi_server.models.service_group_view_model import ServiceGroupViewModel
from openapi_server import util


async def setup_v1_servicegroups_get(request: web.Request, location_id=None, offset=None, limit=None) -> web.Response:
    """List Service Groups

    &lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Service Groups&lt;/b&gt; for the requested location. If no business location is specified it will default to the Primary Business Location of the company. Use the offset and limit parameters to control the page start and size. Default offset is 0, limit is 20, maximum is 100. Use the other query parameters to filter the results further.&lt;/p&gt;

    :param location_id: id of business location, defaults to primary business location
    :type location_id: str
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    return web.Response(status=200)


async def setup_v1_servicegroups_id_delete(request: web.Request, id) -> web.Response:
    """Delete Service Group

    &lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a Service Group object. A valid &lt;b&gt;serviceGroup id&lt;/b&gt; is required. The service group is not permanently deleted and can be recovered by using the &lt;i&gt;PUT ​/setup​/v1​/servicegroups​/{id}​/recover&lt;/i&gt; endpoint.&lt;/p&gt;

    :param id: id of serviceGroup object
    :type id: int

    """
    return web.Response(status=200)


async def setup_v1_servicegroups_id_get(request: web.Request, id) -> web.Response:
    """Get Service Group

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;Service Group&lt;/b&gt; object. A valid &lt;b&gt;serviceGroup id&lt;/b&gt; is required. Find service group id&#39;s by using the &lt;i&gt;GET /setup/v1/serviceGroups&lt;/i&gt; endpoint.&lt;/p&gt;

    :param id: id of serviceGroup object
    :type id: int

    """
    return web.Response(status=200)


async def setup_v1_servicegroups_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update Service Group

    &lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a Service Group object. A valid &lt;b&gt;serviceGroup id&lt;/b&gt; is required. &lt;/p&gt;

    :param id: id of serviceGroup object
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ServiceGroupInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_servicegroups_id_recover_put(request: web.Request, id) -> web.Response:
    """Recover Service Group

    &lt;p&gt;Use this endpoint to &lt;b&gt;Recover&lt;/b&gt; a deleted Service Group. A valid &lt;b&gt;serviceGroup id&lt;/b&gt; is required. &lt;/p&gt;

    :param id: id of serviceGroup object
    :type id: int

    """
    return web.Response(status=200)


async def setup_v1_servicegroups_post(request: web.Request, body=None) -> web.Response:
    """Create Service Group

    &lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a Service Group. If no locationId is specified in the body, the business location will default to the primary business location. Service groups are used to categorize services. Service groups are optional and only make sense if you have multiple services that will be easier read if categorized. Only the service group Type of 0 is supported by the API. It defaults to 0 if not supplied.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes

    """
    body = ServiceGroupInputModel.from_dict(body)
    return web.Response(status=200)
