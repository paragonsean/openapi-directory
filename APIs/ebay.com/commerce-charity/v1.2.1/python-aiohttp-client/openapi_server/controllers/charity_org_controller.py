from typing import List, Dict
from aiohttp import web

from openapi_server.models.charity_org import CharityOrg
from openapi_server.models.charity_search_response import CharitySearchResponse
from openapi_server import util


async def get_charity_org(request: web.Request, charity_org_id, x_ebay_c_marketplace_id) -> web.Response:
    """get_charity_org

    This call is used to retrieve detailed information about supported charitable organizations. It allows users to retrieve the details for a specific charitable organization using its charity organization ID.

    :param charity_org_id: The unique ID of the charitable organization.
    :type charity_org_id: str
    :param x_ebay_c_marketplace_id: A header used to specify the eBay marketplace ID.&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Valid Values:&lt;/b&gt; &lt;code&gt;EBAY_GB&lt;/code&gt; and &lt;code&gt;EBAY_US&lt;/code&gt;
    :type x_ebay_c_marketplace_id: str

    """
    return web.Response(status=200)


async def get_charity_orgs(request: web.Request, x_ebay_c_marketplace_id, limit=None, offset=None, q=None, registration_ids=None) -> web.Response:
    """get_charity_orgs

    This call is used to search for supported charitable organizations. It allows users to search for a specific charitable organization, or for multiple charitable organizations, from a particular charitable domain and/or geographical region, or by using search criteria.&lt;br /&gt;&lt;br /&gt;The call returns paginated search results containing the charitable organizations that match the specified criteria.

    :param x_ebay_c_marketplace_id: A header used to specify the eBay marketplace ID.&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Valid Values:&lt;/b&gt; &lt;code&gt;EBAY_GB&lt;/code&gt; and &lt;code&gt;EBAY_US&lt;/code&gt;
    :type x_ebay_c_marketplace_id: str
    :param limit: The number of items, from the result set, returned in a single page.&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Valid Values:&lt;/b&gt; &lt;code&gt;1-100&lt;/code&gt;&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Default:&lt;/b&gt; &lt;code&gt;20&lt;/code&gt;
    :type limit: str
    :param offset: The number of items that will be skipped in the result set. This is used with the &lt;b&gt;limit&lt;/b&gt; field to control the pagination of the output.&lt;br /&gt;&lt;br /&gt;For example, if the &lt;b&gt;offset&lt;/b&gt; is set to &lt;code&gt;0&lt;/code&gt; and the &lt;b&gt;limit&lt;/b&gt; is set to &lt;code&gt;10&lt;/code&gt;, the method will retrieve items 1 through 10 from the list of items returned. If the &lt;b&gt;offset&lt;/b&gt; is set to &lt;code&gt;10&lt;/code&gt; and the &lt;b&gt;limit&lt;/b&gt; is set to &lt;code&gt;10&lt;/code&gt;, the method will retrieve items 11 through 20 from the list of items returned.&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Valid Values:&lt;/b&gt; &lt;code&gt;0-10,000&lt;/code&gt;&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Default:&lt;/b&gt; &lt;code&gt;0&lt;/code&gt;
    :type offset: str
    :param q: A query string that matches the keywords in name, mission statement, or description.
    :type q: str
    :param registration_ids: A comma-separated list of charitable organization registration IDs.&lt;br /&gt;&lt;br /&gt;&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note: &lt;/b&gt;Do not specify this parameter for query-based searches. Specify either the &lt;b&gt;q&lt;/b&gt; or &lt;b&gt;registration_ids&lt;/b&gt; parameter, but not both.&lt;/span&gt;&lt;br /&gt;&lt;br /&gt;&lt;b&gt;Maximum Limit:&lt;/b&gt; &lt;code&gt;20&lt;/code&gt;
    :type registration_ids: str

    """
    return web.Response(status=200)
