from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_list_view_model import CustomerListViewModel
from openapi_server.models.customer_privacy_view_model import CustomerPrivacyViewModel
from openapi_server.models.customer_view_model import CustomerViewModel
from openapi_server import util


async def setup_v1_customers_get(request: web.Request, location_id=None, group_id=None, email=None, lastname=None, deleted=None, offset=None, limit=None) -> web.Response:
    """List Customers

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Customers&lt;/b&gt;. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

    :param location_id: id of business location, defaults to primary business location
    :type location_id: str
    :param group_id: Filter by groupId
    :type group_id: str
    :param email: Filter by email address.
    :type email: str
    :param lastname: Search by lastname.
    :type lastname: str
    :param deleted: Filter by deleted status.
    :type deleted: bool
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    return web.Response(status=200)


async def setup_v1_customers_id_get(request: web.Request, id) -> web.Response:
    """Get Customer

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;Customer&lt;/b&gt; object. A valid &lt;b&gt;customer id&lt;/b&gt; is required. Find customer id&#39;s by using the &lt;i&gt;GET /setup/v1/customers&lt;/i&gt; endpoint.&lt;/p&gt;

    :param id: id of customer object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_customers_id_privacy_get(request: web.Request, id) -> web.Response:
    """Get Customer Data

    &lt;p&gt;Use this endpoint to return the &lt;b&gt;Customer&lt;/b&gt; object. A valid &lt;b&gt;customer id&lt;/b&gt; is required. Find customer id&#39;s using the &lt;i&gt;GET /setup/v1/customers&lt;/i&gt; endpoint.&lt;/p&gt;

    :param id: id of customer object
    :type id: str

    """
    return web.Response(status=200)
