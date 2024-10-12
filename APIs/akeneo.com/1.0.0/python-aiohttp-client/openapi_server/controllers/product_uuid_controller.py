from typing import List, Dict
from aiohttp import web

from openapi_server.models.patch_products_uuid200_response import PatchProductsUuid200Response
from openapi_server.models.patch_products_uuid_request import PatchProductsUuidRequest
from openapi_server.models.post_products_uuid_request import PostProductsUuidRequest
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server.models.products2 import Products2
from openapi_server import util


async def delete_products_uuid_uuid(request: web.Request, uuid) -> web.Response:
    """Delete a product

    This endpoint allows you to delete a given product. In the Enterprise Edition, permissions based on your user groups are applied to the product you try to delete.

    :param uuid: Uuid of the resource
    :type uuid: str

    """
    return web.Response(status=200)


async def get_draft_uuid_uuid(request: web.Request, uuid) -> web.Response:
    """Get a draft

    This endpoint allows you to get the information about a given draft.

    :param uuid: Uuid of the resource
    :type uuid: str

    """
    return web.Response(status=200)


async def get_products_uuid(request: web.Request, search=None, scope=None, locales=None, attributes=None, pagination_type=None, page=None, search_after=None, limit=None, with_count=None, with_attribute_options=None, with_quality_scores=None, with_completenesses=None) -> web.Response:
    """Get list of products

    This endpoint allows you to get a list of products. Products are paginated and they can be filtered. In the Enterprise Edition, permissions based on your user groups are applied to the set of products you request.

    :param search: Filter products, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html\&quot;&gt;Filters&lt;/a&gt; section
    :type search: str
    :param scope: Filter product values to return scopable attributes for the given channel as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#via-channel\&quot;&gt;Filter product values via channel&lt;/a&gt; section
    :type scope: str
    :param locales: Filter product values to return localizable attributes for the given locales as well as the non localizable/non scopable attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#via-locale\&quot;&gt;Filter product values via locale&lt;/a&gt; section
    :type locales: str
    :param attributes: Filter product values to only return those concerning the given attributes, for more details see the &lt;a href&#x3D;\&quot;/documentation/filter.html#filter-product-values\&quot;&gt;Filter on product values&lt;/a&gt; section
    :type attributes: str
    :param pagination_type: Pagination method type, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type pagination_type: str
    :param page: Number of the page to retrieve when using the &#x60;page&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html#pagination\&quot;&gt;Pagination&lt;/a&gt; section
    :type page: int
    :param search_after: Cursor when using the &#x60;search_after&#x60; pagination method type. &lt;strong&gt;Should never be set manually&lt;/strong&gt;, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type search_after: str
    :param limit: Number of results by page, see &lt;a href&#x3D;\&quot;/documentation/pagination.html\&quot;&gt;Pagination&lt;/a&gt; section
    :type limit: int
    :param with_count: Return the count of items in the response. Be carefull with that, on a big catalog, it can decrease performance in a significative way
    :type with_count: bool
    :param with_attribute_options: Return labels of attribute options in the response. (Only available since the 5.0 version)
    :type with_attribute_options: bool
    :param with_quality_scores: Return product quality scores in the response. (Only available since the 5.0 version)
    :type with_quality_scores: bool
    :param with_completenesses: Return product completenesses in the response. (Only available since the 6.0 version)
    :type with_completenesses: bool

    """
    return web.Response(status=200)


async def get_products_uuid_uuid(request: web.Request, uuid, with_attribute_options=None, with_quality_scores=None, with_completenesses=None) -> web.Response:
    """Get a product

    This endpoint allows you to get the information about a given product. In the Entreprise Edition, permissions based on your user groups are applied to the product you request.

    :param uuid: Uuid of the resource
    :type uuid: str
    :param with_attribute_options: Return labels of attribute options in the response. (Only available since the 5.0 version)
    :type with_attribute_options: bool
    :param with_quality_scores: Return product quality scores in the response. (Only available since the 5.0 version)
    :type with_quality_scores: bool
    :param with_completenesses: Return product completenesses in the response. (Only available since the 6.0 version)
    :type with_completenesses: bool

    """
    return web.Response(status=200)


async def patch_products_uuid(request: web.Request, body=None) -> web.Response:
    """Update/create several products

    This endpoint allows you to update and/or create several products at once. Learn more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no product exists for the given uuid, it creates it. In the Enterprise Edition, permissions based on your user groups are applied to the products you try to update. It may result in the creation of drafts if you only have edit rights through the product&#39;s categories.

    :param body: 
    :type body: dict | bytes

    """
    body = PatchProductsUuidRequest.from_dict(body)
    return web.Response(status=200)


async def patch_products_uuid_uuid(request: web.Request, uuid, body) -> web.Response:
    """Update/create a product

    This endpoint allows you to update a given product. Learn more about &lt;a href&#x3D;\&quot;/documentation/update.html#update-behavior\&quot;&gt;Update behavior&lt;/a&gt;. Note that if no product exists for the given uuid, it creates it. In the Entreprise Edition, permissions based on your user groups are applied to the product you try to update. It may result in the creation of a draft if you only have edit rights through the product&#39;s categories.

    :param uuid: Uuid of the resource
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostProductsUuidRequest.from_dict(body)
    return web.Response(status=200)


async def post_products_uuid(request: web.Request, body=None) -> web.Response:
    """Create a new product

    This endpoint allows you to create a new product. In the Enterprise Edition, permissions based on your user groups are applied to the product you try to create. If no uuid is provided, the PIM will generate one for you.

    :param body: 
    :type body: dict | bytes

    """
    body = PostProductsUuidRequest.from_dict(body)
    return web.Response(status=200)


async def post_proposal_uuid(request: web.Request, uuid) -> web.Response:
    """Submit a draft for approval

    This endpoint allows you to submit a draft for approval.

    :param uuid: Uuid of the resource
    :type uuid: str

    """
    return web.Response(status=200)
