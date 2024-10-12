from typing import List, Dict
from aiohttp import web

from openapi_server.models.attribute_groups import AttributeGroups
from openapi_server.models.attribute_groups_post_request import AttributeGroupsPostRequest
from openapi_server.models.patch_asset_categories200_response import PatchAssetCategories200Response
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server.models.several_attribute_groups_patch_request import SeveralAttributeGroupsPatchRequest
from openapi_server import util


async def attribute_groups_get(request: web.Request, code) -> web.Response:
    """Get an attribute group

    This endpoint allows you to get the information about a given attribute group.

    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def attribute_groups_get_list(request: web.Request, search=None, page=None, limit=None, with_count=None) -> web.Response:
    """Get list of attribute groups

    This endpoint allows you to get a list of attribute groups. Attribute groups are paginated and sorted by code.

    :param search: Filter attribute groups, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-attribute-groups\&quot;&gt;Filters&lt;/a&gt; section.
    :type search: str
    :param page: Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section
    :type page: int
    :param limit: Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type limit: int
    :param with_count: Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    :type with_count: bool

    """
    return web.Response(status=200)


async def attribute_groups_patch(request: web.Request, code, body) -> web.Response:
    """Update/create an attribute group

    This endpoint allows you to update a given attribute group. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no attribute group exists for the given code, it creates it.

    :param code: Code of the resource
    :type code: str
    :param body: 
    :type body: dict | bytes

    """
    body = AttributeGroupsPostRequest.from_dict(body)
    return web.Response(status=200)


async def attribute_groups_post(request: web.Request, body=None) -> web.Response:
    """Create a new attribute group

    This endpoint allows you to create a new attribute group.

    :param body: 
    :type body: dict | bytes

    """
    body = AttributeGroupsPostRequest.from_dict(body)
    return web.Response(status=200)


async def several_attribute_groups_patch(request: web.Request, body=None) -> web.Response:
    """Update/create several attribute groups

    This endpoint allows you to update and/or create several attribute groups at once.

    :param body: 
    :type body: dict | bytes

    """
    body = SeveralAttributeGroupsPatchRequest.from_dict(body)
    return web.Response(status=200)
