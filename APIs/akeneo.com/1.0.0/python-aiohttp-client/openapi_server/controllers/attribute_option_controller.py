from typing import List, Dict
from aiohttp import web

from openapi_server.models.attribute_options import AttributeOptions
from openapi_server.models.patch_asset_categories200_response import PatchAssetCategories200Response
from openapi_server.models.patch_attributes_attribute_code_options_request import PatchAttributesAttributeCodeOptionsRequest
from openapi_server.models.post_attributes_attribute_code_options_request import PostAttributesAttributeCodeOptionsRequest
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def get_attributes_attribute_code_options(request: web.Request, attribute_code, page=None, limit=None, with_count=None) -> web.Response:
    """Get list of attribute options

    This endpoint allows you to get a list of attribute options. Attribute options are paginated and sorted by code.

    :param attribute_code: Code of the attribute
    :type attribute_code: str
    :param page: Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section
    :type page: int
    :param limit: Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type limit: int
    :param with_count: Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    :type with_count: bool

    """
    return web.Response(status=200)


async def get_attributes_attribute_code_options_code(request: web.Request, attribute_code, code) -> web.Response:
    """Get an attribute option

    This endpoint allows you to get the information about a given attribute option.

    :param attribute_code: Code of the attribute
    :type attribute_code: str
    :param code: Code of the resource
    :type code: str

    """
    return web.Response(status=200)


async def patch_attributes_attribute_code_options(request: web.Request, attribute_code, body=None) -> web.Response:
    """Update/create several attribute options

    This endpoint allows you to update several attribute options at once.

    :param attribute_code: Code of the attribute
    :type attribute_code: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchAttributesAttributeCodeOptionsRequest.from_dict(body)
    return web.Response(status=200)


async def patch_attributes_attribute_code_options_code(request: web.Request, attribute_code, code, body) -> web.Response:
    """Update/create an attribute option

    This endpoint allows you to update a given attribute option. Know more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no attribute option exists for the given code, it creates it.

    :param attribute_code: Code of the attribute
    :type attribute_code: str
    :param code: Code of the resource
    :type code: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostAttributesAttributeCodeOptionsRequest.from_dict(body)
    return web.Response(status=200)


async def post_attributes_attribute_code_options(request: web.Request, attribute_code, body=None) -> web.Response:
    """Create a new attribute option

    This endpoint allows you to create a new attribute option.

    :param attribute_code: Code of the attribute
    :type attribute_code: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostAttributesAttributeCodeOptionsRequest.from_dict(body)
    return web.Response(status=200)
