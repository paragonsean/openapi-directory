from typing import List, Dict
from aiohttp import web

from openapi_server.models.resource_group_input_model import ResourceGroupInputModel
from openapi_server.models.resource_group_list_view_model import ResourceGroupListViewModel
from openapi_server.models.resource_group_update_model import ResourceGroupUpdateModel
from openapi_server.models.resource_group_view_model import ResourceGroupViewModel
from openapi_server.models.resource_view_model import ResourceViewModel
from openapi_server import util


async def setup_v1_resourcegroups_get(request: web.Request, location_id=None, deleted=None, offset=None, limit=None) -> web.Response:
    """List Resource Groups

    &lt;p&gt;Use this endpoint to &lt;b&gt;List Resource Groups&lt;/b&gt; for the specified location. If not specified, the business location defaults to the primary business location. &lt;b&gt;Name&lt;/b&gt; is a required field.&lt;/p&gt;  &lt;p&gt;Use the offset and limit parameters to control the page start and size. Default offset is 0, limit is 20, maximum is 100. Use the query parameters to filter the results further.&lt;/p&gt;

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


async def setup_v1_resourcegroups_id_delete(request: web.Request, id) -> web.Response:
    """Delete Resource Group

    &lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a resourceGroup object. A valid &lt;b&gt;resourceGroup id&lt;/b&gt; is required. The resource group is not permanently deleted and can be recovered by using the &lt;i&gt;PUT ​/setup​/v1​/resourcegroups​/{id}​/recover&lt;/i&gt; endpoint.&lt;/p&gt;

    :param id: id of resourceGroup object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_resourcegroups_id_get(request: web.Request, id) -> web.Response:
    """Get Resource Group

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;Resource Group&lt;/b&gt; object. A valid &lt;b&gt;resourceGroup id&lt;/b&gt; is required. Find resourceGroup id&#39;s by using the &lt;i&gt;GET setup/v1/resourceGroups&lt;/i&gt; endpoint.&lt;/p&gt;

    :param id: id of resourceGroup object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_resourcegroups_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update Resource Group

    &lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a resourceGroup object. A valid &lt;b&gt;resourceGroup id&lt;/b&gt; is required. &lt;/p&gt;

    :param id: id of resourcGroup object
    :type id: str
    :param body: Resource Group Update Model
    :type body: dict | bytes

    """
    body = ResourceGroupUpdateModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_resourcegroups_id_recover_put(request: web.Request, id) -> web.Response:
    """Recover Resource Group

    &lt;p&gt;Use this endpoint to &lt;b&gt;Recover&lt;/b&gt; a deleted resourceGroup object. A valid &lt;b&gt;resourceGroup id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of resourceGroup object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_resourcegroups_post(request: web.Request, body=None) -> web.Response:
    """Create Resource Group

    &lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a resourceGroup object. Resource groups are used to categorize your resources.&lt;/p&gt;

    :param body: Resource input model
    :type body: dict | bytes

    """
    body = ResourceGroupInputModel.from_dict(body)
    return web.Response(status=200)
