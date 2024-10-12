from typing import List, Dict
from aiohttp import web

from openapi_server.models.attributes import Attributes
from openapi_server.models.patch_asset_categories200_response import PatchAssetCategories200Response
from openapi_server.models.patch_attributes_request import PatchAttributesRequest
from openapi_server.models.post_attributes_request import PostAttributesRequest
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def get_attributes(request: web.Request, search=None, page=None, limit=None, with_count=None, with_table_select_options=None) -> web.Response:
    """Get list of attributes

    This endpoint allows you to get a list of attributes. Attributes are paginated and sorted by code.

    :param search: Filter attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-attributes\&quot;&gt;Filters&lt;/a&gt; section.
    :type search: str
    :param page: Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section
    :type page: int
    :param limit: Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type limit: int
    :param with_count: Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    :type with_count: bool
    :param with_table_select_options: Return the options of &#39;select&#39; column types (of a table attribute) in the response. (Only available since the 7.0 version)
    :type with_table_select_options: bool

    """
    return web.Response(status=200)


async def get_attributes_code(request: web.Request, code, with_table_select_options=None) -> web.Response:
    """Get an attribute

    This endpoint allows you to get the information about a given attribute.

    :param code: Code of the resource
    :type code: str
    :param with_table_select_options: Return the options of &#39;select&#39; column types (of a table attribute) in the response. (Only available since the 7.0 version)
    :type with_table_select_options: bool

    """
    return web.Response(status=200)


async def patch_attributes(request: web.Request, body=None) -> web.Response:
    """Update/create several attributes

    This endpoint allows you to update and/or create several attributes at once.

    :param body: 
    :type body: dict | bytes

    """
    body = PatchAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def patch_attributes_code(request: web.Request, code, body) -> web.Response:
    """Update/create an attribute

    This endpoint allows you to update a given attribute. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no attribute exists for the given code, it creates it.

    :param code: Code of the resource
    :type code: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostAttributesRequest.from_dict(body)
    return web.Response(status=200)


async def post_attributes(request: web.Request, body=None) -> web.Response:
    """Create a new attribute

    This endpoint allows you to create a new attribute.

    :param body: 
    :type body: dict | bytes

    """
    body = PostAttributesRequest.from_dict(body)
    return web.Response(status=200)
