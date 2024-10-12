from typing import List, Dict
from aiohttp import web

from openapi_server.models.complete_codename_lsit import CompleteCodenameLsit
from openapi_server.models.detailed_ordering_level_info import DetailedOrderingLevelInfo
from openapi_server.models.detailed_product_information import DetailedProductInformation
from openapi_server.models.product_listing_level_info import ProductListingLevelInfo
from openapi_server.models.unsuccessful_operation import UnsuccessfulOperation
from openapi_server import util


async def get_code_name(request: web.Request, locale_geo_id) -> web.Response:
    """5. Get list of codename details for Intel products.

    Use this to get codename details for Intel products. No pagination supported.

    :param locale_geo_id: Locale and Geo code used to get localised data.&lt;br/&gt;&lt;br/&gt;
    :type locale_geo_id: str

    """
    return web.Response(status=200)


async def get_product_info(request: web.Request, locale_geo_id, product_id, include_reference=None) -> web.Response:
    """2. Get complete product info with product id.

    Use this to get complete product info. No pagination supported.

    :param locale_geo_id: Locale and Geo code used to get localised data.&lt;br/&gt;&lt;br/&gt;
    :type locale_geo_id: str
    :param product_id: Product id&#39;s that needs to be filtered. Only max of 40 products are supported now. Values must be enclosed in [ square brackets ] and each value must be in \&quot;double quotes\&quot;. Use comma to add multiple values.&lt;br/&gt;&lt;br/&gt;Example: [\&quot;223\&quot;,\&quot;224\&quot;]
    :type product_id: str
    :param include_reference: If send \&quot;true\&quot;, this will fetch variant/compatible info into result set. Default is false.
    :type include_reference: str

    """
    return web.Response(status=200)


async def get_product_list(request: web.Request, locale_geo_id, category_id=None, product_id=None, highlights=None, sort=None, filters=None, per_page=None, page_no=None) -> web.Response:
    """1. Find products by product id or category id

    Use this to get basic details of products with pagination. Can be used to generate listing page for products.

    :param locale_geo_id: Locale and Geo code used to get localised data.&lt;br/&gt;&lt;br/&gt;
    :type locale_geo_id: str
    :param category_id: Filter products based on one or multiple category id. Either category id or product id is mandatory for any request. Values must be enclosed in [ square brackets ] and each value must be in \&quot;double quotes\&quot;. Use comma to add multiple values. &lt;br/&gt;&lt;br/&gt;Example: [\&quot;873\&quot;]&lt;br/&gt;&lt;br/&gt;Categories Available:&lt;br/&gt; Processors &#x3D; 873, Server Products &#x3D; 1201, Mini PC&#39;s &#x3D; 98414, Wireless Networking &#x3D; 59485, Ethernet Products &#x3D; 36773, Fabric products &#x3D; 70021, Memory and Storage &#x3D; 35125, Chipsets &#x3D; 53, Graphics Drivers &#x3D; 80939 &lt;br/&gt;&lt;br/&gt;
    :type category_id: str
    :param product_id: Filter products based on one or multiple product id. Either category id or product id is mandatory for any request. Values must be enclosed in [ square brackets ] and each value must be in \&quot;double quotes\&quot;. Use comma to add multiple values. &lt;br/&gt;&lt;br/&gt;Example: [\&quot;123003\&quot;]&lt;br/&gt;&lt;br/&gt;
    :type product_id: str
    :param highlights: Specification values which needs to be pulled from product data. Values must be enclosed in [ square brackets ] and each value must be in \&quot;double quotes\&quot;. Use comma to add multiple values. &lt;br/&gt;&lt;br/&gt;Example: [\&quot;CoreCount\&quot;, \&quot;StatusCodeText\&quot;]&lt;br/&gt;&lt;br/&gt;
    :type highlights: str
    :param sort: Indicates sorting fields. Accepts array of objects in format like: [{\&quot;field\&quot;:\&quot;name\&quot;,\&quot;order\&quot;:\&quot;ASC\&quot;}].&lt;br/&gt;&lt;br/&gt;Any specification that we get from get-product-info can be used to sort result. Other generic sort field is \&quot;name\&quot;.&lt;br/&gt;&lt;br/&gt;
    :type sort: str
    :param filters: Allows to filter data.&lt;br/&gt;&lt;br/&gt;Format of filter: [{\&quot;type\&quot;:\&quot;specvalue\&quot;,\&quot;name\&quot;:\&quot;ThreadCount\&quot;,\&quot;gteq\&quot;:\&quot;4\&quot;}]&lt;br/&gt;&lt;br/&gt;&lt;b&gt;Available operators are:&lt;/b&gt; \&quot;eq\&quot;: equal to, \&quot;neq\&quot;: not equal to, \&quot;lteq\&quot;: less than or equal to, \&quot;gteq\&quot;: greater than or equal to, \&quot;swc\&quot;: starts with characters, \&quot;nswc\&quot;: not starting with characters, \&quot;cts\&quot;: contains, \&quot;ncts\&quot;: not contains&lt;br/&gt;&lt;br/&gt;&lt;b&gt;Conditions:&lt;/b&gt; By default all objects works on an AND condition. But inside an object we have the capability to put an \&quot;OR\&quot; or \&quot;AND\&quot; condition.&lt;br/&gt;Example conditions: [{\&quot;type\&quot;:\&quot;specvalue\&quot;,\&quot;name\&quot;:\&quot;ThreadCount\&quot;,\&quot;ncts\&quot;:\&quot;4,5\&quot;,\&quot;cond\&quot;:\&quot;AND\&quot;}]&lt;br/&gt;&lt;br/&gt;&lt;br/&gt;
    :type filters: str
    :param per_page: Filter number of products in response to desired size.
    :type per_page: int
    :param page_no: Indicates page number for pagination of results.
    :type page_no: int

    """
    return web.Response(status=200)


async def getorderinginfo(request: web.Request, product_id, locale_geo_id) -> web.Response:
    """3. Get ordering info for product id&#39;s requested.

    Use this to fetch ordering info details for Intel products. No pagination supported.

    :param product_id: Filter ordering info details based on one or multiple product id&#39;s. Values must be enclosed in [ square brackets ] and each value must be in \&quot;double quotes\&quot;. Use comma to add multiple values. &lt;br/&gt;&lt;br/&gt;Example: [\&quot;123003\&quot;]
    :type product_id: str
    :param locale_geo_id: Locale and Geo code used to get localised data.&lt;br/&gt;&lt;br/&gt;
    :type locale_geo_id: str

    """
    return web.Response(status=200)
