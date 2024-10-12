from typing import List, Dict
from aiohttp import web

from openapi_server.models.resource_list_view_model import ResourceListViewModel
from openapi_server.models.service_allocation_list_view_model import ServiceAllocationListViewModel
from openapi_server.models.service_allocation_view_model import ServiceAllocationViewModel
from openapi_server.models.service_list_view_model import ServiceListViewModel
from openapi_server.models.service_sort_order import ServiceSortOrder
from openapi_server.models.service_view_model import ServiceViewModel
from openapi_server.models.services_scope import ServicesScope
from openapi_server import util


async def consumer_v1_services_allocations_id_get(request: web.Request, id) -> web.Response:
    """Get Service Allocation

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;Service Allocation&lt;/b&gt; object. A valid &lt;b&gt;serviceAllocation id&lt;/b&gt; is required. Find service allocation id&#39;s by using the &lt;i&gt;GET/consumer​/v1​/services​/{id}​/allocations&lt;/i&gt; endpoint.&lt;/p&gt;

    :param id: id of serviceAllocation object
    :type id: str

    """
    return web.Response(status=200)


async def consumer_v1_services_get(request: web.Request, location_id=None, service_group_id=None, default_service=None, all_locations=None, scope=None, name=None, service_id=None, offset=None, limit=None, sort_order=None, sort_descending=None) -> web.Response:
    """List Services

    &lt;p&gt;Use this endpoint to &lt;b&gt;List Services&lt;/b&gt; available at your business location and/or company. If not specified, the business location defaults to the primary business location. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

    :param location_id: id of business location, defaults to primary business location
    :type location_id: str
    :param service_group_id: Filter by groupId
    :type service_group_id: int
    :param default_service: Filter by default service, default is false
    :type default_service: bool
    :param all_locations: Search All Locations, default is false
    :type all_locations: bool
    :param scope: Filter by scope, Company, Location or All, default is All
    :type scope: dict | bytes
    :param name: Filter by Name, supports Partial name search
    :type name: str
    :param service_id: Filter by ServiceId, using this parameter would ignore all other parameters
    :type service_id: str
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int
    :param sort_order: Sort results using Natural Sort or Sorted alphabetically by Service Names, default is natural
    :type sort_order: dict | bytes
    :param sort_descending: Sort results in Descending Order, default true
    :type sort_descending: bool

    """
    scope = .from_dict(scope)
    sort_order = .from_dict(sort_order)
    return web.Response(status=200)


async def consumer_v1_services_id_allocations_get(request: web.Request, id, location_id=None, resource_id=None, start_date=None, end_date=None, offset=None, limit=None) -> web.Response:
    """List Service Allocations

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Service Allocations&lt;/b&gt; associated with the requested service. A valid &lt;b&gt;service id&lt;/b&gt; is required. Allocations are used for Event type services/bookings. Retrieve all allocations for a location by passing in zero as the service id. Otherwise, to get allocations for a specific service supply the service id. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further. For more information: &lt;a href&#x3D;\&quot;https://docs.onsched.com/reference/post_setup-v1-services-id-allocations\&quot;&gt;Create Service Allocations&lt;/a&gt;&lt;/p&gt;

    :param id: id of service to list allocations for, 0 for all
    :type id: str
    :param location_id: id of the location, defaults to the primary location
    :type location_id: str
    :param resource_id: id of the resource to filter on
    :type resource_id: str
    :param start_date: Format YYYY-MM-DD: Filter allocations on/after startDate
    :type start_date: str
    :param end_date: Format YYYY-MM-DD. Filter allocations on/before endDate
    :type end_date: str
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def consumer_v1_services_id_get(request: web.Request, id) -> web.Response:
    """Get Service

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;Service&lt;/b&gt; object. A valid &lt;b&gt;service id&lt;/b&gt; is required. Find service id&#39;s by using the &lt;i&gt;GET /consumer/v1/services&lt;/i&gt; endpoint.&lt;/p&gt;

    :param id: id of service object
    :type id: int

    """
    return web.Response(status=200)


async def consumer_v1_services_id_resources_get(request: web.Request, id, location_id=None, offset=None, limit=None) -> web.Response:
    """List Resources for Service

    &lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Resources that provide the Service requested&lt;/b&gt;. A valid &lt;b&gt;service id&lt;/b&gt; is required. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

    :param id: id of service object
    :type id: str
    :param location_id: id of business location, defaults to primary business location
    :type location_id: str
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    return web.Response(status=200)
